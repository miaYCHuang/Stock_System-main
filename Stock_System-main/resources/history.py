from flask import Flask,request
import requests
from flask_restful import Resource

from datetime import datetime

import base64
from requests import request

import json


import urllib.request as req


class history(Resource):
    def stock1(id):
      
        token = {
            'apim_header_token': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzMjMyNjU3LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.ouHStICt7NYOEzpWn-Jz7t3rsm0tGMM6Rxrh3lXT0Wo",
            'apim_query_token': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzMjMyNjU3LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.ouHStICt7NYOEzpWn-Jz7t3rsm0tGMM6Rxrh3lXT0Wo", 
            'realtime_api_token':"4af7c90c0eac7cd5ee3d289f00045bbb"
        }
        #aaa="1101"
        url3= "https://api.fintechspace.com.tw/history/api/v2/data/contents/FCNT000002?symbol_id="+id
        
        
        header = {
                'Authorization': token['apim_header_token'],
                'User-Agent': 'Mozilla/5.0'
            }
        
        response = requests.get(url3, headers=header)    
        data = json.loads(response.text)
            
        #print(data)
        
        # with open("1101B.json","r",encoding="utf-8") as f:
        #data = json.load(f)  
        len(data['data']['content']['rawContent']['day'])         
        l=""  #要傳給js的值
        #天
        for i in data['data']['content']['rawContent']['day']:
            d=i['date'].split("T")
            l+=str(i['close'])+","
            l+=str(i['low'])+","
            l+=str(i['high'])+","
            l+=str(i['open'])+","
            l+=d[0]+","
            l+=str(i['volume'])+"#"
        l=l[:-1]
        l+="@"     
        for i in data['data']['content']['rawContent']['week']:
            d=i['date'].split("T")
            l+=str(i['close'])+","
            l+=str(i['low'])+","
            l+=str(i['high'])+","
            l+=str(i['open'])+","
            l+=d[0]+","
            l+=str(i['volume'])+"#"
        l=l[:-1]
        l+="@"
        
        for i in data['data']['content']['rawContent']['month']:
            d=i['date'].split("T")
            l+=str(i['close'])+","
            l+=str(i['low'])+","
            l+=str(i['high'])+","
            l+=str(i['open'])+","
            l+=d[0]+","
            l+=str(i['volume'])+"#"
        l=l[:-1]
        #print(l)

        # return render_template('index1.html',l=l)  
        return l