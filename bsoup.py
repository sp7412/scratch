#!/usr/bin/python

from bs4 import BeautifulSoup, Comment
import urllib

riskURL = "https://finance.yahoo.com/quote/SHSAX/risk"
page = urllib.urlopen(riskURL)
content = page.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')

import pdb; pdb.set_trace()

stdevValue = float(soup.find("span",{"data-reactid":"124","class":"W(39%) Fl(start)"}).text)
stdevCat = float(soup.find("span",{"data-reactid":"125","class":"W(57%) Mend(5px) Fl(end)"}).text)

print stdevValue, stdevCat


