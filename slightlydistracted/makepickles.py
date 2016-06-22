import pickle
import random
import datetime
from twisted.internet import task
from twisted.internet import reactor
import json
import facebook

TIMEOUT = datetime.timedelta(minutes=60).seconds


def main():
    with open("access.json", 'r') as f:
        db = json.load(f)
    cfg = db
    api = get_api(cfg)
    output = buildPost()
    print len(output)
#     output += str(' #' + hashtag(output))
    status = api.put_wall_post(output)


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
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
    while len(output) < 350:
        output += (' ' + buildTweet())
        print output
    return output

if __name__ == '__main__':
    l = task.LoopingCall(main)
    l.start(TIMEOUT)
    reactor.run()
