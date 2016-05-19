import pickle
import random
import string
import datetime
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython
import sys
import json

TIMEOUT = datetime.timedelta(minutes=60).seconds

def main():
    output = buildPost()
    print(output)
    print len(output)


def buildTweet():
    chain = pickle.load(open("chain.p", "rb"))
    new_tweet = []
    sword1 = "BEGIN"
    sword2 = "NOW"
    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        new_tweet.append(sword2)
        print new_tweet
    tweet = ' '.join(new_tweet)
    return tweet

def buildPost():
    output = ''
    while len(output) < 700:
        output += (' ' + buildTweet())
        print output
    return output

def tweet(sentence):
    try:
        sys.stdout.write("{} {}\n".format(len(sentence), sentence))
        twitter.update_status(status=sentence)
    except:
        pass

if __name__ == '__main__':
   main()
