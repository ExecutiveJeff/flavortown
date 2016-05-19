#!/usr/bin/env python -tt

import urllib2
from lxml.html import fromstring
import sys
import time

urlprefix = "http://www.winespectator.com/dailypicks/category/catid/1/page/"

# 709
for page in xrange(1, 10):
    try:
        out = "-> On page {} of {}....      {}%"
        print out.format(page, "709", str(round(float(page) / 709 * 100, 2)))
        response = urllib2.urlopen(urlprefix + str(page))
        html = response.read()
        dom = fromstring(html)
        sels = dom.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "paragraph", " " ))]')
        for review in sels:
            if review.text:
                print review.text.rstrip()
        sys.stdout.flush()
        time.sleep(2)
    except:
        continue