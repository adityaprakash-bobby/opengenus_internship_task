#! /bin/env python2
import sys
import urllib2
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import re
import click

userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : userAgent }

def getURLData (url) :
    """
    Send request to the webpage and fetch the page data, if exists.
    """
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    return response.read()

def parseData (url) :
    """
    Process the data from website using BeautifulSoup to fetch various details
    from the webpage.
    """
    try :
        data = getURLData(url)
        ctr = 0

    except urllib2.HTTPError as e :
        click.echo(click.style("Status Code:" + str(e.code) + "\nDescription:"
                                    + e.reason + "\nTry again.", fg = 'red'))

    except urllib2.URLError as e :
        click.echo(click.style("Description:" + str(e.reason)
                                    + "\nTry again.", fg='red'))

    else :
        document = BeautifulSoup(''.join(data))
        domain = urlparse(url).netloc

        for link in document.findAll('a', attrs = {'href' : re.compile("(https:\/\/"
                                    + domain + "[\/\w \.-]*\/?)")}):
            # print link.get('href')
            ctr += 1

        for link in document.findAll('a', attrs = {'href' : re.compile("^[.|/]")}):
            # print link.get('href')
            ctr += 1

        for link in document.findAll('a', attrs = {'href' : re.compile("^[#]")}):
            # print link.get('href')
            ctr += 1

        # print  "\nSize:", len(data), " Bytes", "\nDomain:", domain, "\nInlinks:", ctr
        click.echo(click.style("\nSize : " + str(len(data)) + " Bytes", fg = 'green'))
        click.echo(click.style("\nDomain : " + domain, fg = 'blue'))
        click.echo(click.style("\nLinks within the domain : " + str(ctr), fg = 'yellow'))

if __name__ == '__main__' :
    parseData(sys.argv[1])
