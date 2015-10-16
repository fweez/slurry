#/usr/bin/env -w python

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to
import re

@listen_to('HI SLURRY')
def hi(message):
    message.reply("Hello. I've hidden your keys.")

@respond_to('HI SLURRY')
def hir(message):
    message.reply("You need to stop yelling, it's late and our neighbors need to be up for work tomorrow morning.")

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
