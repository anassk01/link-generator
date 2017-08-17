#!/usr/bin/python
# -*- coding: utf-8 -*-
from urlparse import urlparse
import re
import requests
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup as BS
from HTMLParser import HTMLParser
from itertools import tee, islice, chain, izip
from os import name,system

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def trash(rest):
    rest = strip_tags(rest)
    rest = re.sub("['<>]", "", rest)
    rest = re.sub('"', "", rest)
    rest = rest.replace("   ", " ")
    rest = re.sub(
        ur'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', u'', rest)
    return rest

def getcont(url):
   global content
   try:
     req=requests.get(url)
     content=str(req.content)
   except:
     try:
        req=urlopen(url)
 	content=req.read()
     except:
	print "requests error"

def getitle(lynk):
   global title
   getcont(lynk)
   try:
      try:
        soup = BS(urlopen(lynk, timeout=int(10)))
        title = (soup.title.string)
      except:
	title=re.findall(r'title" content="(.*?)"',content)
        title=''.join(title)
   except:
      try:
	items=re.findall("title.*$",content,re.MULTILINE)
	title=BS(str(items[0])).text
      except:
	title="aname"
   title=str(trash(title))

def valide(link):
  global domain
  parsed = urlparse(link)
  domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed)
  global content
  getcont(link)
  print link
  try:
    global check_json
    check_json=re.findall('json/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    check_json=(map(lambda x:domain+x if "http" not in x else json_link==check_json ,check_json))
    if check_json:
      for json in check_json:
        req=requests.get(json)
        jsonc=str(req.content)
        content=content+jsonc
  except:
      pass
linklist=[];ttlist=[];fnlist=[]

system('cls' if name == 'nt' else 'clear')

print('\x1b[1;31;40m' +
      ' \n \r [ Link 5awi ] Extraire Direct Link To Watching Episode  ! \n' + '\x1b[0m') 

lst = ["https://www.yourupload.com","https://streamango.com", "https://openload.co", "https://docs.google.com", "https://drive.google.com","http://samaup.com",
       "http://ok.ru", "http://megatobox.com", "https://www.file-upload.com", "https://www.solidfiles.com", "https://estream.to", "https://ok.ru", "http://www.cloudy.ec","https://www.rapidvideo.com","http://3rbup.com","https://www.mp4upload.com","https://vidstreaming.io","https://bestream.tv/","http://vidup.me","https://thevideo.me","http://watchers.to/",]
print ('\x1b[1;30;33m' + "\n list of search site : \n" + '\x1b[0m')

for i, j in enumerate(lst):
    print ('\x1b[1;30;34m' + str(i) + "-" + j + '\x1b[0m')


urlink=str(raw_input("here u are : ")).split("::")
listed = filter(lambda x: ">" in x , urlink)
nlisted=filter(lambda x: ">" not in x , urlink)
if listed:
  beg=int(raw_input("begin please --> "))
  end=int(raw_input("end please --> "))
  for ee in xrange(beg,end+1):
     inrot=(map(lambda x:str.replace(x,">",str(ee)) ,listed))
     linklist.extend(inrot)
if nlisted:
   linklist.extend(nlisted)


for cacs in linklist:
   valide(cacs) 
   for za in lst:
     urls = re.findall(za+'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
     urls = '\n'.join(urls)
     if urls.strip():
	urls=urls
        try:
	  getitle(cacs)
	except:
	  getitle(urls)
	ttlist.append(title)
	for previous, item, nxt in previous_and_next(ttlist):
            if item != nxt and item!= previous :
		print title
	urls=str(trash(urls));print urls


