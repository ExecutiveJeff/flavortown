#!/usr/bin/python
import json
import sys
import random
import datetime
from twisted.internet import task
from twisted.internet import reactor
from twython import Twython
from markov_class import *
from sys import argv
import twitter


script = argv
inputfile = argv
TIMEOUT = datetime.timedelta(minutes=60).seconds
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET))


def main():
    # might break everything splice in autoblake markov chain code
    order = int(1)
    handle = "DoMeAFlavorTown"
    filetext = process_file()
    markov = MarkovDict(filetext, order, 180)
    markov.read_text()
    output = markov.output_text()
    print output
    tweet(output)


def process_file():
    f = open("flavortown.txt")
    filetext = f.read()
    f.close()
    return filetext

 
def tweet(sentence):
    """Tweet sentence to Twitter."""
    try:
        sys.stdout.write("{} {}\n".format(len(sentence), sentence))
        twitter.update_status(status=sentence)
    except:
        pass

if __name__ == '__main__':
    l = task.LoopingCall(main)
    l.start(TIMEOUT) 
    reactor.run()
