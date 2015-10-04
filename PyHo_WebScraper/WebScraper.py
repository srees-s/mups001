'''
Created on Oct 4, 2015

@author: Sreesankar
'''

import urllib2

from BeautifulSoup import BeautifulSoup


class PyBotWebScraper:
    
    def scrapeAndPrint(self,url,search):
        soup = BeautifulSoup(urllib2.urlopen(url).read())
        #print soup
        try:
            for divs in soup('div',{'class':'normalsection'}):
                for links in divs('a'):
                    try:
                        if (links.string.index(' ')>-1):
                            if(links.string.lower().index(search)):
                                print links.string.replace('\n','')
                    except:
                        pass
        except Exception, e:
            print 'Nothing found to scrape!'
            print e
            pass
        
PyBotWebScraper().scrapeAndPrint(url='http://www.msn.com/en-us/news',search='trump') #'https://twitter.com/')
        
