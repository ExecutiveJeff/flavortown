import pickle
import random
import sys


def main():
    output = buildPost()
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
    tweet = ' '.join(new_tweet)
    tweet = tweet + '\n'
    return tweet


def buildPost():
    output = ''
    while len(output) < 500:
        output += (' ' + buildTweet())
        print output, len(output)
    return output

if __name__ == '__main__':
    main()
