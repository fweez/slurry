#/usr/bin/env -w python

from slackbot.bot import Bot
from slackbot.bot import respond_to, listen_to
from collections import Counter
import random
import re

helloed = Counter()
bored = [
    "La la la I'm not listening",
    "Siri, how do I get this drunkard to stop bothering me?",
    "Lord, what fools these meat prisms be.",
    "Okay google, destroy all humans.",
]
question_words = ['who', 'where', 'what', 'when', 'why', 'how']
good_ideas = [
    'lie down for just a minute',
    'drink some water',
    'eat a taco',
    'count to one thousand by sevens',
    'let the room stop spinning',
    'take off your shoes',
    'check with your therapist',
    'chill the fuck out',
    'stop yelling, our neighbors can hear you',
    'have a slice of pizza',
    'drink a big glass of water',
    'think about what you just said',
    'go to the porch and talk to the smokers in a quiet voice',
]
message_words = ['tell', 'call', 'text', 'message', 'send']

@listen_to('HI SLURRY', re.IGNORECASE)
def hi(message):
    user = message.body['user']
    helloed[user] += 1
    if helloed[user] == 1:
        message.reply("Hello. I've hidden your keys.")
    elif helloed[user] == 2:
        message.reply("Yes, hello. Again.")
    elif helloed[user] == 3:
        message.reply("I'm going to ignore you unless you have something interesting to say.")
    else:
        message.send(random.choice(bored))

@listen_to('HEY SLURRY[,:\s]*(.*)', re.IGNORECASE)
def hey(message, contents=None):
    if contents:
        idea = random.choice(good_ideas)
        first_word = contents.split()[0].lower()
        if first_word in question_words:
            message.reply('We can talk about that after you {}.'.format(idea))
        elif first_word in message_words:
            message.reply("I'm not sure sending that right now is a good idea.")
        else:
            message.reply(unicode('''I'm researching "{}". Meanwhile maybe you should {}?''').format(unicode(contents, errors='replace'), idea))
    else:
        message.reply("Again, I see you there. You don't need to keep yelling at me.")

@respond_to('(.*)')
def splat(message, contents=None):
    # I don't want any @slurry responses, so:
    message.reply("Hush now. Let's just lie down on the couch for a bit and chill.")

if __name__ == "__main__":
    Bot().run()
