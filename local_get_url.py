#coding=utf-8

import urllib.request
import sys
import os
import re

with open('data.txt','r',errors='ignore') as raw:
    data=raw.read()
    data=data.replace('small','big')
#以上替换small和big
title=re.findall(r'<h1.*?entry-title">(.*?)</h1>',str(data))
findlink=re.findall(r'img.*?src="(.*?)" alt="',str(data))
link=list(set(findlink))
link.sort(key=findlink.index)
a=1
print (title[0])
print ('Total',len(link),'pictures')
for lin in link:
    with open ('%s.txt' % title[0],'a',errors='ignore') as url:
        url.write(str(lin)+'\n')
    with open ('%sRename.bat' % title[0],'a',encoding='ANSI',errors='ignore') as ren:
        ren.write('rename '+str(lin).split('/')[-1]+' %03d.jpg' % a+'\n')
        #ren.write('rename',str(lin).split('/')[-1],'\t%03d.jpg' % a+'\n');其中\t表示Tab符，\000表示空格，%03d为格式化3位数字如001,018,158
    a=a+1
