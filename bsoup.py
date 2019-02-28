#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib

riskURL = "https://finance.yahoo.com/quote/SHSAX/risk"
page = urllib.urlopen(riskURL)
content = page.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')

#import pdb; pdb.set_trace()

std=[]
std_span = next(x for x in soup.find_all('span') if x.text == "Standard Deviation")
parent_div = std_span.parent
for sibling in parent_div.next_siblings:
  for child in sibling.children:
     # do something
     #print(child.text)
     std.append((child.text).encode("utf-8"))



print std
print '--------------------'

alpha=[]
alpha_span = next(x for x in soup.find_all('span') if x.text == "Alpha")
parent_div = alpha_span.parent
for sibling in parent_div.next_siblings:
  for child in sibling.children:
     # do something
     #print(child.text)
     alpha.append((child.text).encode("utf-8"))

print alpha

print '--------------------'

beta=[]
beta_span = next(x for x in soup.find_all('span') if x.text == "Beta")
parent_div = beta_span.parent
for sibling in parent_div.next_siblings:
  for child in sibling.children:
     # do something
     #print(child.text)
     beta.append((child.text).encode("utf-8"))

print beta




