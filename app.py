#! /bin/env python2
import sys, ssl, httplib
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

    except httplib.BadStatusLine as e:
        click.echo(click.style("Description: Unkown status code", fg = 'red'))
        click.echo("Try again")
        
    except ValueError as e:
        click.echo(click.style("Description: " + str(e), fg='red'))
        click.echo("Try again adding/modifying 'http(s)://'.")

    except ssl.CertificateError as e:
        click.echo(click.style("Description: " + str(e), fg='red'))
        click.echo("Try again.")

    except urllib2.HTTPError as e :
        click.echo(click.style("Status Code: " + str(e.code) + "\nDescription: "
                                    + e.reason, fg = 'red'))
        click.echo("Try again.")

    except urllib2.URLError as e :
        click.echo(click.style("Description:" + str(e.reason), fg='red'))
        click.echo("Try again.")

    else :
        document = BeautifulSoup(''.join(data))
        domain = urlparse(url).netloc

        for link in document.findAll('a', attrs = {'href' : re.compile("(https:\/\/"
                                    + domain + "[\/\w \.-]*\/?)|(^[.|/])|(^[#])")}):
            # print link.get('href')
            ctr += 1

        click.echo(click.style("Size : " + str(len(data)) + " Bytes", fg = 'green'))
        click.echo(click.style("Domain : " + domain, fg = 'green'))
        click.echo(click.style("Links within the same domain : " + str(ctr), fg = 'yellow'))

if __name__ == '__main__' :
    parseData(sys.argv[1])
