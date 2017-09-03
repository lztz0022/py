#coding=utf-8

import urllib.request
import sys
import os,tkinter.filedialog
import re
import json
import hashlib
import random

default_dir = r'D:\Py'
fileName = tkinter.filedialog.askopenfilename(initialdir=(os.path.expanduser(default_dir)))

with open(fileName,'r',errors='ignore') as raw:
    data=raw.read()
title=re.findall(r'"name headline">(.*?)</h1>',str(data))
ltitle=re.findall(r'"articleSell">(.*?)</span>',str(data))
findcontent=re.findall(r'<span class="drop-cap">(.*?)<script>',str(data))
contents=list(set(findcontent))
contents.sort(key=findcontent.index)
if os.path.exists('temp.txt'):
    os.remove("temp.txt")
with open ('temp.txt','a',errors='ignore') as txt:
    txt.write(title[0]+'\n')
    txt.write(ltitle[0]+'\n')
for content in contents:
    with open ('temp.txt','a',errors='ignore') as txt:
        txt.write(str(content)+'\n')
with open ('temp.txt','r',errors='ignore') as raw1:
    data1=raw1.read()
    regex='<a href=".*?>'
    data1=re.sub(regex,'',data1)
    pattern='<div.*?</div>'
    data1=re.sub(pattern,'',data1)
    data1=data1.replace('</p><h2>','\n')
    data1=data1.replace('</h2><p>','\n')
    data1=data1.replace('</p><p>','\n')
    data1=data1.replace('</span>','')
    data1=data1.replace('</a>','')
try:
    os.mkdir('E:\We the Media\%s' %title[0])
except FileExistsError:
    print('Path Exists')

with open ('E:\We the Media\%s\%s.txt' %(title[0],title[0]), 'w',errors='ignore') as raw2:
    raw2.write(data1)

with open ('E:\We the Media\%s\%s.txt' %(title[0],title[0]),'r',encoding='utf-8',errors='ignore') as fileIn:
    with open ('E:\We the Media\%s\\''Fy%s.txt' %(title[0],title[0]),'w',encoding='utf-8') as fileOut:
        appid='20170307000041649'
        secretKey = 'JcXq9a9QwvxN2l6AhIqH'
        myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        q = 'apple'
        fromLang = 'en'
        toLang = 'zh'
        salt = random.randint(32768, 65536)
        for eachline in fileIn:
            line=eachline.strip()
            if line:
                if line[0].isdigit():
#                    fileOut.write(line+'\n')
                else:
                    sign = appid+line+str(salt)+secretKey
                    sign = hashlib.md5(sign.encode()).hexdigest()
                    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(line)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
                    resultPage = urllib.request.urlopen(myurl)
#                    print (myurl)
                    resultJason = resultPage.read().decode('utf-8')
                    resultJasons = resultPage.read()
#                    print (resultJason)
                    try:
                        js = json.loads(resultJason)
#                        print ('dst')
                        dst = str(js['trans_result'][0]['dst'])
#                        outStr = dst
#                        print (dst)
                        if dst[0]:
                            outDst=dst.strip()+'\n'
                            fileOut.write(outDst)
                    except Exception as e:
                        fileOut.write('\n')
                        continue
                    else:
                        fileOut.write('\n')
