#coding=utf-8

import urllib.request
import sys
import os
import re

webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36  Gecko/20100101 Firefox/23.0'}
with open('/learngit/url.txt','r',errors='ignore') as raw:
    link=raw.readlines()
a=0
while a<len(link):
    imgreq=urllib.request.Request(url=link[a],headers=webheader)
    img=(urllib.request.urlopen(imgreq,timeout=20)).read()
    with open('/learngit/%d.jpg' %(a+1),'wb') as pic:
        pic.write(img)
    a=a+1
