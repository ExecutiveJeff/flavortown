#!/usr/bin/env python -tt

import urllib2
from lxml.html import fromstring
import sys
import time

urlprefix = "http://stuffhipsterssay.tumblr.com/"

# 709
for page in xrange(1, 10):
    try:
        out = "-> On page {} of {}....      {}%"
        print out.format(page, "10", str(round(float(page) / 10 * 100, 2)))
        response = urllib2.urlopen(urlprefix + str(page))
        html = response.read()
        dom = fromstring(html)
        sels = dom.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "post", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "short", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "post", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "short", " " ))]')
        for review in sels:
            if review.text:
                print review.text.rstrip()
        sys.stdout.flush()
        time.sleep(2)
    except:
        continue
