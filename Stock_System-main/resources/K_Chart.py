import plotly
import plotly.graph_objs as go
from flask_restful import Resource
import json , csv
import pandas as pd
from datetime import datetime, timedelta, timezone
import urllib.request as req

class K_Chart(Resource):
    def get(id):
        try:
            stock_file = "https://api.fintechspace.com.tw/realtime/v0/intraday/meta?symbolId="+id+"&apiToken=4af7c90c0eac7cd5ee3d289f00045bbb&oddLot=false&jwt=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzOTEwMTQ5LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.JlZH2GwwXzS8QyALnq7iBc6ocm_fCIKPUGmTnHVa9qQ"
            with open(stock_file, 'r') as obj:
                data = json.load(obj)

            obj.close()
            return  data
        except:
            return "#"

    def create_image(id):
        #stock_file =  'resources\intraday_chart_'+id+'.json'
        stock_file =  "https://api.fintechspace.com.tw/realtime/v0/intraday/chart?symbolId="+id+"&apiToken=4af7c90c0eac7cd5ee3d289f00045bbb&oddLot=false&jwt=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzOTEwMTQ5LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.JlZH2GwwXzS8QyALnq7iBc6ocm_fCIKPUGmTnHVa9qQ"
        

        with req.urlopen(stock_file) as stock_file:

            stock_data=json.load(stock_file)

        stock_df = pd.DataFrame(columns = ['Date' , 'Open', 'High' , 'Low' , 'Close'])

        for time in stock_data["data"]["chart"]: 
            dt = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f%z')
            utc_dt = dt.replace(tzinfo=timezone.utc) 
            tw_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  
            
            new_stock = pd.DataFrame.from_dict( {"Date": [tw_dt],
                                    "Open":[stock_data["data"]["chart"][time]["open"]],
                                    "High":[stock_data["data"]["chart"][time]["high"]],
                                    "Low":[stock_data["data"]["chart"][time]["low"]],
                                    "Close":[stock_data["data"]["chart"][time]["close"]]}) 

            stock_df = stock_df.append(new_stock,ignore_index=True)
        



        fig = go.Figure(data=[go.Candlestick(x=stock_df['Date'],
                        open=stock_df['Open'],
                        high=stock_df['High'],
                        low=stock_df['Low'],
                        close=stock_df['Close'],
                        increasing_line_color= 'red', decreasing_line_color= 'forestgreen')])

        # fig.show()
        graphJSON = json.dumps(fig, cls= plotly.utils.PlotlyJSONEncoder)

        return graphJSON

    def get_name(id):
        try:

            stock_file1 = "https://api.fintechspace.com.tw/realtime/v0/intraday/meta?symbolId="+id+"&apiToken=4af7c90c0eac7cd5ee3d289f00045bbb&oddLot=false&jwt=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIyMDI0IiwiaWF0IjoxNjIzOTEwMTQ5LCJpc3MiOiIydUtBOE8xYU1iUUs2ZFpCT0M0UGpWRnJlOW9NWjM3byJ9.JlZH2GwwXzS8QyALnq7iBc6ocm_fCIKPUGmTnHVa9qQ"
            with req.urlopen(stock_file1) as stock_file1:
                stock_data=json.load(stock_file1)

            stock_name =stock_data["data"]["meta"]["nameZhTw"]
            #obj1.close()

            return  stock_name
        except:
            return("#")