#coding=utf-8

import urllib.request
import sys
import os,tkinter.filedialog
import re
import json
import hashlib
import random,time

default_dir = r'E:\WeMedia Original'
fileName = tkinter.filedialog.askopenfilename(initialdir=(os.path.expanduser(default_dir)))

with open(fileName,'r',errors='ignore') as raw:
    data=raw.read()
titles=re.findall(r'headline">(.*?)</h1>',str(data))
if len(titles)==0:
    titles=re.findall(r'Recipe">(.*?)</a></h1>',str(data))
title=titles[0].replace(':','-')

ltitle=re.findall(r'"articleSell">(.*?)</span>',str(data))
if len(ltitle)==0:
    ltitle=re.findall(r'h2>(.*?)</h2>',str(data))
if 'itemprop="ingredients"' not in data:
    findcontent=re.findall(r'itemprop="articleBody">.*?">(.*?)<script>',str(data))
else:
    findcontent=re.findall(r'<p>(.*?)</p>',str(data))
    findingre=re.findall(r'itemprop="ingredients">(.*)',str(data))
    findinstr=re.findall(r'itemprop="recipeInstructions">(.*)',str(data))
    findcontent.extend(findingre)
    findcontent.extend(findinstr)
contents=list(set(findcontent))
contents.sort(key=findcontent.index)
if os.path.exists('temp.txt'):
    os.remove("temp.txt")
with open ('temp.txt','a',errors='ignore') as txt:
    txt.write(title+'\n')
    if len(ltitle) == 0:
        print ('no subhead')
    else:
        txt.write(ltitle[0]+'\n')
for content in contents:
    with open ('temp.txt','a',errors='ignore') as txt:
        txt.write(str(content)+'\n')
with open ('temp.txt','r',errors='ignore') as raw1:
    data1=raw1.read()
    data1=data1.replace('</p>','\n')
    data1=data1.replace('</ul>','\n')
    data1=data1.replace('</h2>','\n')
    pattern='<div.*?</div>'
    data1=re.sub(pattern,'',data1)
    regex='<.*?>'
    data1=re.sub(regex,'',data1)
#    data1=data1.replace('</p><h2.?>','\n')
#    data1=data1.replace('</h2><p.?>','\n')
#    data1=data1.replace('</p><p.?>','\n')
#    data1=data1.replace('</span>','')
#    data1=data1.replace('</a>','')
try:
    os.mkdir('E:\We the Media\%s' %title)
except FileExistsError:
    print('Path Exists')

localtime = time.strftime('%Y,%m,%d %H-%M',time.localtime())

with open ('E:\We the Media\%s\%s %s.txt' %(title,title,localtime), 'w',errors='ignore') as raw2:
    raw2.write(data1)

with open ('E:\We the Media\%s\%s %s.txt' %(title,title,localtime),'r',encoding='utf-8',errors='ignore') as fileIn:
    with open ('E:\We the Media\%s\\''Fy-%s %s.txt' %(title,title,localtime),'w',encoding='utf-8') as fileOut:
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
                sign = appid+line+str(salt)+secretKey
                sign = hashlib.md5(sign.encode()).hexdigest()
                myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(line)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
                resultPage = urllib.request.urlopen(myurl)
#                print (myurl)
                resultJason = resultPage.read().decode('utf-8')
                resultJasons = resultPage.read()
#                print (resultJason)
                try:
                    js = json.loads(resultJason)
#                    print ('dst')
                    dst = str(js['trans_result'][0]['dst'])
#                    outStr = dst
#                    print (dst)
                    if dst[0]:
                        outDst=dst.strip()+'\n'
                        fileOut.write(outDst)
                except Exception as e:
                    fileOut.write('\n')
                    continue
                else:
                    fileOut.write('\n')
if os.path.exists('temp.txt'):
    os.remove("temp.txt")
