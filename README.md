# kotd-client-py
A Reddit client made in Python that only works specifically on the subreddit r/KickOpenTheDoor

Are you a KOTD player looking for a helpful and revolutionary tool to make your game experience more enjoyable? Well you've come to the wrong place!

**What's r/KickOpenTheDoor?**

If you're asking this question I don't think you're in the right repository.

**What does this do?**

It's basically a Reddit client (if you're willing to stretch the definition of a "client" that far) that lets you send comments on r/KickOpenTheDoor. It can show current bosses that are alive, and it lets you send attacks to bosses without having to open Reddit in a browser or on your phone. Essentially it's [Slam's Active Boss list](https://slampisko.github.io/active-bosses/), with a button to send comments.

**What does this *not* do?**

It will not automatically attack for you when your cooldown is up. The raccoons are terrifying and I don't want them to come after me.

**Requirements, setup and how to use**

You need to have:
- Python 3.x (idk what version just try running it and if it doesn't work then upgrade your Python)
- PRAW (you have to install it yourself idk how to do that fancy deploying thing)
- Reddit app ID and secret (you can get them at https://www.reddit.com/prefs/apps)

To set the client up, just fill your info in the credentials.py file and run client.py.

The client should show a list of active bosses like this:
```
(1) L3 H0432/2487 D064: This guy knows how to party
(2) L1 H1045/1200 D008: The knoll
(3) L1 H1870/2000 D011: Deep one
(4) L1 H2286/7000 D021: Choose Wisely [P]
(5) L1 H2474/4000 D016: (B) Tome Seeker
(6) L5 H6874/7000 D389: The black fire
Total: D509
Choose boss to reply to:
```
Each line represents a boss. `L` is the number of stars, `H` is the current and maximum health, `D` is the maximum damage you can receive from attacking that boss, and after that is the title of the boss.

To send a comment, enter the index of the boss you want to comment on and then enter the comment body.

Additionally you can refresh the list by entering `reload` and exit by entering `exit` (or kill the program, whichever you prefer).

Many players have text replacement shortcuts on mobile that speed up typing attacks, and this client can also do the same thing! In settings.py, you can add any shortcuts you want to the `shortcuts` dictionary. For instance, if you edit:
```python
shortcuts = {'r0': '!ranged 0'}
```
and send `r0` as your comment body in the client, it will send `!ranged 0` instead!

**Is this thing actually good?**
So far, no it's horrible. But you can improve it! Just yell at this idiot named @halloooooo on the KOTD Discord server for new ideas.
