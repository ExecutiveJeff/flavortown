#!/usr/bin/env python -tt

import urllib2
from lxml.html import fromstring
import sys
import time

urlprefix = "http://www.yelp.com/biz/the-night-light-oakland?osq=hipster+bars"

# 709
for page in xrange(1, 10):
    try:
        out = "-> On page {} of {}....      {}%"
        print out.format(page, "10", str(round(float(page) / 10 * 100, 2)))
        response = urllib2.urlopen(urlprefix + str(page))
        html = response.read()
        dom = fromstring(html)
        sels = dom.xpath('//li[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//p | //li[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//p | //*+[contains(concat( " ", @class, " " ), concat( " ", "clearfix", " " ))]//p')
        for review in sels:
            if review.text:
                print review.text.rstrip()
        sys.stdout.flush()
        time.sleep(2)
    except:
        continue
