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

twitter = Twython("n6ljSickvPnRyV4rhQnvUYDpZ",
                   "fOTyGq19WDhRtksbUguFuOsFKItFJyp3snSlhOv7dnkeg2ZDUe",
                   "714220672268894209-bVWFvFlkR77ZSwvT3nteQOkD82M7eRf",
                   "fQpeoPzDDwxOSZktVR6BKutyEYFm7YKGEAg4yOb5WfHH3")

#def auth():
#    f =  open("access.json", 'r')
#    db = json.load(f)
#    API_Key = db["API_Key"]
#    API_Secret = db["API_Secret"]
#    Access_Token = db["Access_Token"]
#    Access_Token_Secret = db["Access_Token_Secret"]
#    return Twython(API_Key, API_Secret, Access_Token, Access_Token_Secret)


def main():

    print twitter
    output = buildPost()
    output += str(' #' + hashtag(output))
    while len(output) > 140:
        output = buildPost()
        output += str(' #' + hashtag(output))
    tweet(output)


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
    # type: () -> object
    output = ''
    while len(output) < 120:
        output += (' ' + buildTweet())
        output = output.rpartition('.')[0]
        endingpunc = [".", "!", "?", "?!"]
        output += random.choice(endingpunc)
        output = output.lstrip('\"')
        output = output.lstrip(string.punctuation)
        print output
    return output


def hashtag(output):
    keywords = ["flavortown", "badabing", "brother", "wow", "bbq", "rollingout", "guyfieri", "tripleD", "gangsta", "cheflife", "outofthisworld", "saucy", "shutthefrontdoor"]
    hashtag = str(random.choice(keywords))
    print hashtag
    return hashtag


def tweet(sentence):
    try:
        sys.stdout.write("{} {}\n".format(len(sentence), sentence))
        twitter.update_status(status=sentence)
    except:
        pass

if __name__ == '__main__':
    l = task.LoopingCall(main)
    l.start(TIMEOUT)
    reactor.run()
