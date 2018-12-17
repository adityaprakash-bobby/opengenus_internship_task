#! /bin/env python2
import sys
import urllib2
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import re

def getURLData (url) :
    response = urllib2.urlopen(url)
    return response.read()

def sameDomainLinks ():
    pass

def parseData (url) :
    try :
        data = getURLData(url)
        ctr = 0
    except urllib2.HTTPError as e :
        print "Status Code:", e.code, "\nDescription:", e.reason
        print "Try again."

    except urllib2.URLError as e :
        print "Description:", e.reason, "\nTry again."

    else :
        document = BeautifulSoup(''.join(data))
        # domain = url.split("//")[-1].split("/")[0]
        domain = urlparse(url).netloc
        # for link in document.findAll('a', attrs = {'href' : re.compile(u"(https:\/\/" + domain + "[\/\w \.-]*\/?)")}):
        #     print link.get('href')
        #
        # for link in document.findAll('a', attrs = {'href' : re.compile(r"[.|\/]$")}):
        #     print link.get('href')

        for link in document.findAll('a', attrs = {'href' : re.compile("^[#]")}):
            print link.get('href')
            ctr += 1

        print  "\nSize:", len(data),"\nDomain:", domain, "\nInlinks:", ctr

if __name__ == '__main__' :
    parseData(sys.argv[1])
