import pickle
import random
import datetime
import sys
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython, TwythonError
import json


friendshiptime = datetime.timedelta(minutes=1).seconds
handleTime = datetime.timedelta(minutes=30).seconds
TIMEOUT = datetime.timedelta(minutes=60).seconds


def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    twitter = Twython(
        db["API_Key"],
        db["API_Secret"],
        db["Access_Token"],
        db["Access_Token_Secret"])
    return twitter


def main():
    output = buildPost()
    output += str(' #' + hashtag(output))
    while len(output) > 140:
        output = buildPost()
        output += str(' #' + hashtag(output))
    tweet(output)
    retweet()


def retweet():
    words_to_rt = [
        "#organic",
        "#craftbeer",
        "#brunch"]
    hashlist = " OR ".join(words_to_rt)
    twitter = auth()
    s = str(random.choice(words_to_rt))
    search_results = twitter.search(q=s, count=5)
    try:
        for tweet in search_results["statuses"]:
            twitter.retweet(id=tweet["id_str"])
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


#def randombar():
#    chain = pickle.load(open("bars.p", "rb"))
#    new_tweet = []
#    sword1 = "BEGIN"
#    sword2 = "NOW"
#    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
#    new_tweet.append(sword2)
#    tweet = ' '.join(new_tweet)
#    return tweet


def buildPost():
    output = ''
    while len(output) < 120:
        output += (' ' + buildTweet())
        print output, len(output)
    return output


def hashtag(output):
    keywords = [
        "organic",
        "craftbeer",
        "local",
        "brunch",
        "eggsfordays",
        "grassroots",
        "bro",
        "hella",
        "brunchlife",
        "dogpark",
        "afterhours",
        "getlitfam",
        "baearea",
        "yayarea"]
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
    last_sent_id = []
    lastsent = twitter.get_direct_messages(since_id=last_sent_id)
    friendId = lastsent[0]['id_str']
    who = lastsent[0]['sender_screen_name']
    dtext = lastsent[0]['text']
    if friendId in open('twitterdm.log').read():
        pass

    else:
        lf = open('twitterdm.log', 'a+')
        lf.write(str(friendId) + " " + who + " " + dtext + '\n')
        print friendId
        targets = twitter.get_direct_messages(count=1)
        for target in targets:
            friendID = target['sender_id_str']
            #parsetext = target['text']
            if friendId != friendID:
                try:
                    dmtext = buildTweet()
                    twitter.create_friendship(user_id=friendID, follow="true")
                    twitter.send_direct_message(user_id=friendID, text=dmtext)
                except TwythonError as e:
                    print(e)
        lf.close()


#def trash():
#    twitter = auth()
#    trump = ["@realDonaldTrump"]
#    search_results = twitter.search(q=trump, count=5)
#    trashlog = open('trashlog.log', 'a+')
#    try:
#        for tweet in search_results["statuses"]:
#            who = tweet['user']['screen_name'].encode("utf-8")
#            text = tweet['text'].encode("utf-8")
#            theid = tweet['id_str']
#            trashlog.write(str(theid) + " " + who + " " + text + '\n')
#            msg = buildTweet()
#            trashboat = "@{0} {1}".format(who, msg)
#            twitter.update_status(status=trashboat, in_reply_to_status_id=theid)
#            print trashboat
#
#    except TwythonError as e:
#        print e
#    trashlog.close()



def handlementions(lastMentionId=None):
    twitter = auth()
    mentions = twitter.get_mentions_timeline(since_id=lastMentionId)
    if mentions:
        # Remember the most recent tweet id, which will be the one at index
        # zero.
        lastMentionId = mentions[0]['id_str']
        for mention in mentions:
            who = mention['user']['screen_name']
            text = mention['text']
            theId = mention['id_str']
            rlog = open('twitterreply.log', 'a+')
            # we favorite every mention that we see
            try:
                if lastMentionId not in open('twitterreply.log').read():
                    rlog.write(str(theId) + " " + who + " " + text + '\n')
                    twitter.create_favorite(id=theId)
                    # create a reply to them.
                    msg = buildTweet()
                    # In order to post a reply, you need to be sure to include
                    # their username in the body of the tweet.
                    replyMsg = "@{0} {1}".format(who, msg)
                    print replyMsg
                    twitter.update_status(
                        status=replyMsg, in_reply_to_status_id=theId)
                else:
                    print "No new mentions"
            except TwythonError as e:
                print e
            rlog.close()

if __name__ == '__main__':
    h = task.LoopingCall(handlementions)
 #   t = task.LoopingCall(trash)
    f = task.LoopingCall(friendshipiscreepy)
 #   t.start(handleTime)
    f.start(friendshiptime)
    h.start(handleTime)
    l = task.LoopingCall(main)
    l.start(TIMEOUT)
    reactor.run()
