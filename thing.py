import logging
import praw
import re
from credentials import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD
from settings import shortcuts, enableLogging

def processFlair(flair):
    hpextract = re.search(r'\d+/\d+', flair).group().split('/')
    stars = len(re.search(r'★+', flair).group())
    curhp = int(hpextract[0])
    maxhp = int(hpextract[1])
    maxdmg = round(0.08*curhp**0.15*maxhp**0.5*stars**1.7)
    return stars, curhp, maxhp, maxdmg

def processTitle(title):
    return title.replace(re.search(r' \[Health:.+\]', title).group(), '')

def loadBosses():
    global subreddit
    bosses = []
    totaldmg = 0
    for submission in subreddit.new(limit=100):
        if ("❤" in submission.link_flair_text) & ("[Slime Only]" not in submission.title):
            stars, curhp, maxhp, maxdmg = processFlair(submission.link_flair_text)
            title = processTitle(submission.title)
            totaldmg += maxdmg
            bosses.append({
                'submission': submission,
                'stars': stars,
                'curhp': curhp,
                'maxhp': maxhp,
                'maxdmg': maxdmg,
                'title': title
                })
    bosses = sorted(bosses, key=lambda d: d['curhp'])
    return bosses

if enableLogging:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    for logger_name in ("praw", "prawcore"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
    
reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT,
    username = USERNAME,
    password = PASSWORD
)

subreddit = reddit.subreddit("kickopenthedoor")
while True:
    bosses = loadBosses()
    for i in bosses:
        print(f'({bosses.index(i)+1}) L{i["stars"]} H{format(i["curhp"],"04d")}/{format(i["maxhp"],"04d")} D{format(i["maxdmg"],"03d")}: {i["title"]}')
    print(f'Total: D{sum(boss["maxdmg"] for boss in bosses)}')
    bossIndex = input('Choose boss to reply to:')
    if bossIndex == 'reload': continue
    if bossIndex == 'exit': break
    else:
        bossToHit = bosses[int(bossIndex)-1]['submission']
        commentBody = input('Input comment body:')
        if commentBody in shortcuts: commentBody = shortcuts[commentBody]
        bossToHit.reply(commentBody)
    
