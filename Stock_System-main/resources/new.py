# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:28:11 2021

@author: yu
"""

from flask import Flask,redirect,render_template,request,url_for
from flask import request
from flask_bootstrap import Bootstrap
import requests
from pprint import pprint
import json
import urllib.request as req
#url3= "https://api.fintechspace.com.tw/social/keywordSearch/news?keyword="+id+"&type=all"

app = Flask(__name__)
bootstrat = Bootstrap(app)
fbfile ='fb1101.json'
newsfile ='news1101.json'
token = {
        'apim_header_token': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzMjMyNjU3LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.ouHStICt7NYOEzpWn-Jz7t3rsm0tGMM6Rxrh3lXT0Wo",
        'apim_query_token': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzMjMyNjU3LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.ouHStICt7NYOEzpWn-Jz7t3rsm0tGMM6Rxrh3lXT0Wo", 
        'realtime_api_token':"4af7c90c0eac7cd5ee3d289f00045bbb"
    }
header = {
          'Authorization': token['apim_header_token'],
          'User-Agent': 'Mozilla/5.0'
        }

@app.route('/')#首頁讀檔固定
def index():
     with open(fbfile,'r',encoding="utf-8") as obj:
          fb = json.load(obj)

          FBtitle=[]
          FBurl=[]
          FBtime=[]
          cnt=0
          for res in fb['result']:
               t=res['page_id_name'] #'166883573428837 Piko Live 皮克直播'
               tit=t[t.find(' ')+1:] #找到第一個空白然後取後面
               FBtitle.append(tit)
               FBurl.append(res['url'])
               FBtime.append(res['time'])
               cnt=cnt+1
               if cnt==5 : #取前五筆
                    break
          #pprint(title)
          #pprint(url)
          #pprint(time)

     with open(newsfile,'r',encoding="utf-8") as obj:
               news = json.load(obj)

               newsTitle=[]
               newsUrl=[]
               newsTime=[]
         
               for res in news['result']:
                    
                    newsTitle.append(res['title'])
                    newsUrl.append(res['url'])
                    newsTime.append(res['time'])
                 
               #pprint(newsTitle)
               #pprint(newsUrl)
               #pprint(newsTime)
     return render_template('news_index.html',time=FBtime ,url=FBurl,title=FBtitle,nTitle=newsTitle,nUrl=newsUrl,nTime=newsTime) 

        
@app.route('/total',methods=['POST','GET'])#根據輸入變換json檔 可輸1101、1604
def total():
     if request.method =='POST':
          if request.form['submit_button'] == 'news':
               #Newsfile ='news'+request.values['send']+'.json'
               aaa = request.values['send']
               
               url3= "https://api.fintechspace.com.tw/social/keywordSearch/news?keyword=2330&type=title"
               response = requests.get(url3, headers=header)    
               
               #with open(url3,'r',encoding="utf-8") as res3:
               #with req.urlopen(url3) as res:

               news = json.loads(response.text)
               
               #news = json.load(obj)
               newsTitle=[]
               newsUrl=[]
               newsTime=[]
               for res in news['result']:
                    newsTitle.append(res['title'])
                    newsUrl.append(res['url'])
                    newsTime.append(res['time'])
      
              
               return render_template('news_result.html',time=newsTime ,url=newsUrl,title=newsTitle)
          else:
               print("NO")
        
          
     
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=5001)