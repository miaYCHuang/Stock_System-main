# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:28:11 2021

@author: yu
"""

from flask import Flask,redirect,render_template,request,url_for
from flask import request
import requests
from pprint import pprint
import json
from flask_restful import Resource

token = {
        'apim_header_token': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzMjMyNjU3LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.ouHStICt7NYOEzpWn-Jz7t3rsm0tGMM6Rxrh3lXT0Wo",
        'apim_query_token': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzMjMyNjU3LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.ouHStICt7NYOEzpWn-Jz7t3rsm0tGMM6Rxrh3lXT0Wo", 
        'realtime_api_token':"4af7c90c0eac7cd5ee3d289f00045bbb"
    }
header = {
          'Authorization': token['apim_header_token'],
          'User-Agent': 'Mozilla/5.0'
        }
class News(Resource):
    def news(id):
        print(id)
        # if request.form['submit_button'] == 'news':
        #     #Newsfile ='news'+request.values['send']+'.json'
        #     aaa = request.values['send']
            
        # url3= "https://api.fintechspace.com.tw/social/keywordSearch/news?keyword="+str(id)+"&type=title"
        url3 = "https://api.fintechspace.com.tw/social/keywordSearch/news?keyword=%22{}%22&type=title".format(id)
        print(url3)

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

        
        return (newsTime,newsUrl,newsTitle)
    # else:
    #     print("NO")