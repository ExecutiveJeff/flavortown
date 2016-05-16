import pickle
import random
import string


def main():
    output = buildPost()
    output += str(' #' + hashtag(output))
    while len(output) > 140:
        output = buildPost()
        output += str(' #' + hashtag(output))
    print len(output)
    print output


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
        endingpunc = [".", "!", "?"]
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

if __name__ == '__main__':
    main()
