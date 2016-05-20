import pickle
import random
import string
import datetime
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython
import sys
import json
import facebook

TIMEOUT = datetime.timedelta(minutes=1).seconds


def main():
     cfg = {
        "page_id"       : "1613323642316370",
        "access_token"  : "EAAH16iIzzS0BAGJd02Y5t5arGZBe5vugHf37nbpe1Tta6r9lBRImmkVYy3VxNFp51YBMV2zaJzlTZBEFhborz6NIR0JE7dhz3vK1xgzCfq2Nyze6iKNhFlg8ciZAQhy4i3fIFujJXvKIgnLbV7S"
     }
     api = get_api(cfg)
     output = buildPost()
     print len(output)
     print output

def get_api(cfg):
     graph = facebook.GraphAPI(cfg['access_token'])
     resp = graph.get_object('me/accounts')
     page_access_token = None
     for page in resp['data']:
         if page ['id'] == cfg['page_id']:
             page_access_token = page['access_token']
     graph = facebook.GraphAPI(page_access_token)
     return graph

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
    l = task.LoopingCall(main)
    l.start(TIMEOUT)
    reactor.run()
