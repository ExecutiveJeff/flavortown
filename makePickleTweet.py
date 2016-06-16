import pickle
import random
import string
import datetime
import sys
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython
import json
import time

TIMEOUT = datetime.timedelta(minutes=60).seconds


#def countdown():
#    x = TIMEOUT
#    for i in range(x + 1):
#        time.sleep(1)
#        print "   " + (formatTime(x)),"time left      \r",
#        sys.stdout.flush()
#        x -= 1
#    return pass

def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))

def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    twitter = Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])
    return twitter

def main():
    output = buildPost()
    output += str(' #' + hashtag(output))
    while len(output) > 140:
        output = buildPost()
        output += str(' #' + hashtag(output))
    tweet(output)
 #   countdown()



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
    tweet = ' '.join(new_tweet)
    return tweet

def buildPost():
    output = ''
    while len(output) < 120:
        output += (' ' + buildTweet())
        output = output.rpartition('.')[0]
        endingpunc = [".", ".", ".", ".", ".", "!", "?", "?!"]
        output += random.choice(endingpunc)
        output = output.lstrip('\"')
        output = output.lstrip(string.punctuation)
        print output, len(output)
    return output


def hashtag(output):
    keywords = ["420braiseit", "flavortown", "badabing", "brother", "wow", "bbq", "rollingout", "guyfieri", "tripleD", "gangsta", "cheflife", "outofthisworld", "saucy", "shutthefrontdoor"]
    hashtag = str(random.choice(keywords))
    print "#" + hashtag
    return hashtag


def tweet(sentence):
    try:
        twitter = auth()
        sys.stdout.write("{} {}\n".format(len(sentence), sentence))
        twitter.update_status(status=sentence)
    except:
        pass

if __name__ == '__main__':
    l = task.LoopingCall(main)
    l.start(TIMEOUT)
    reactor.run()

