import pickle
import random
import string
import datetime
import sys
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython, TwythonError
import json
import time

handleTime = datetime.timedelta(minutes=1).seconds
TIMEOUT = datetime.timedelta(minutes=60).seconds

def countdown():
    x = TIMEOUT
    for i in range(x + 1):
        time.sleep(1)
        print "   " + (formatTime(x)),"time left      \r",
        sys.stdout.flush()
        x -= 1
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
#    countdown()
    retweet()

def retweet():
    words_to_rt = ["#butter", "#flavortown", "#GroceryGames", "#guyfieri", "#foodnetwork", "#porkfat", "cheflife"]
    hashlist = " OR ".join(words_to_rt)
    twitter = auth()
    search_results = twitter.search(q=hashlist, count=10)
    try:
        for tweet in search_results["statuses"]:
            twitter.retweet(id = tweet["id_str"])
    except TwythonError as e:
        print e

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
    keywords = ["outofbounds", "DDD", "420braiseit", "flavortown", "badabing", "brother", "wow", "bbq", "rollingout", "guyfieri", "tripleD", "gangsta", "cheflife", "outofthisworld", "saucy", "shutthefrontdoor"]
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


def friendshipiscreepy():
    twitter = auth()
    targets = twitter.get_direct_messages(count=10)
    for target in targets:
        friendID = target['sender_id_str']
        parsetext = target['text']


        try:
            twitter.create_friendship(user_id=friendID, follow="true")
            twitter.send_direct_message(user_id=friendID, text=parsetext + "?" + " " + "You think this is a game?")
        except TwythonError as e:
            print(e)

def handlementions(lastMentionId=None):
    twitter = auth()
    mentions = twitter.get_mentions_timeline(since_id=lastMentionId)
    if mentions:
        # Remember the most recent tweet id, which will be the one at index zero.
        lastMentionId = mentions[0]['id_str']
        for mention in mentions:
            who = mention['user']['screen_name']
            text = mention['text']
            theId = mention['id_str']

            # we favorite every mention that we see
            try:
                twitter.create_favorite(id=theId)
                # create a reply to them.
                msg = buildTweet()
                # In order to post a reply, you need to be sure to include
                # their username in the body of the tweet.
                replyMsg = "@{0} {1}".format(who, msg)
                print replyMsg
                twitter.update_status(status=replyMsg, in_reply_to_status_id=theId)
            except TwythonError as e:
                print e

if __name__ == '__main__':
    h = task.LoopingCall(handlementions)
    f = task.LoopingCall(friendshipiscreepy)
    f.start(handleTime)
    h.start(handleTime)
    l = task.LoopingCall(main)
    l.start(TIMEOUT)
    reactor.run()

