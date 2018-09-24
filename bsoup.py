#!/usr/bin/python

from bs4 import BeautifulSoup, Comment
import urllib

riskURL = "https://finance.yahoo.com/quote/SHSAX/risk"
page = urllib.urlopen(riskURL)
content = page.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')

import pdb; pdb.set_trace()


std_span = next(x for x in soup.find_all('span') if x.text == "Standard Deviation")
parent_div = std_span.parent
for sibling in parent_div.next_siblings:
  for child in sibling.children:
     # do something
     print(child.text)


std = soup.find("span", {"data-reactid" : "121"}).text
print std


print float(soup.find(class_="W(57%) Mend(5px) Fl(end)").text)
print float(soup.find("span",{"data-reactid":"124"}).text)
print float(soup.find("span",{"data-reactid":"125"}).text)




