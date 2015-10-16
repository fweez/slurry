#/usr/bin/env -w python

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to
import re


@listen_to('HI SLURRY', re.IGNORECASE)
def hi(message):
    message.reply("Hello. I've hidden your keys.")

@listen_to('HEY SLURRY(.*)', re.IGNORECASE)
def hey(message, contents=None):
    if contents:
        message.reply("I'm not sure" + contents + " is a good idea. Maybe you should have a glass of water?")
    else:
        message.reply("Again, I see you there. You don't need to keep yelling at me.")

@respond_to('(.*)')
def splat(message, contents=None):
    # I don't want any @slurry responses, so:
    message.reply("Hush now. Let's just lie down on the couch for a bit and chill.")

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
