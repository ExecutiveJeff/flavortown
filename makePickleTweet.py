import pickle
import random
import string
import datetime
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython
#import json
from access import twitter


TIMEOUT = datetime.timedelta(minutes=60).seconds

#def auth():
   # with open("access.json", 'r') as f:
   #     db = json.load(f)
   # akey = db["API_Key"]
   # asec = db["API_Secret"]
   # atok = db["Access_Token"]
   # atoks = db["Access_Token_Secret"]
   # print akey, asec, atok, atoks
 #   twitter = Twython(API_Key, API_Secret, Access_Token, Access_Token_Secret)
 #   return twitter

def main():
#    print auth()
#    twitter = auth()
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
    output = ''
    while len(output) < 120:
        output += (' ' + buildTweet())
        output = output.rpartition('.')[0]
        endingpunc = [".", ".", ".", ".", ".", "!", "?", "?!"]
        output += random.choice(endingpunc)
        output = output.lstrip('\"')
        output = output.lstrip(string.punctuation)
        print output
    return output


def hashtag(output):
    keywords = ["420braiseit", "flavortown", "badabing", "brother", "wow", "bbq", "rollingout", "guyfieri", "tripleD", "gangsta", "cheflife", "outofthisworld", "saucy", "shutthefrontdoor"]
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
#    l = task.LoopingCall(main)
#    l.start(TIMEOUT)
#    reactor.run()
    main()
