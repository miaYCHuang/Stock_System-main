import csv
from flask_restful import Resource
import pandas as pd

# 開啟 CSV 檔案
class class_search(Resource):
    def get(id , mode):        
        with open('resources\Mode{}.csv'.format(mode), newline='',encoding="utf-8") as csvfile:
        # 讀取 CSV 檔案內容
            rows = csv.reader(csvfile)

            stock_list=[]
            stock_df = pd.DataFrame(stock_list, columns = ['Number' , 'Name'])


    #         Listed=["水泥","食品","塑膠","紡織","電機","電器電纜","化學","生技醫療",
    # "玻璃","造紙","鋼鐵","橡膠","汽車","半導體","電腦週邊","光電","通信網路",
    # "電子零組件","電子通路","資訊服務","其它電子","營建","航運","觀光","金融",
    # "貿易百貨","油電燃氣","存託憑證","ETF","受益證券","ETN","其他","市認購",
    # "市認售","指數類","市牛證","市熊證"]

            
            # 以迴圈輸出每一列
            for row in rows:
                if(row[5]==id):

                    stock_df=stock_df.append({'Number' : row[0] , 'Name' : row[1]},ignore_index=True)

            csvfile.close()


        return stock_df

    def get_Mode(id):        
        with open('resources\Mode4.csv', newline='',encoding="utf-8") as csvfile:
        # 讀取 CSV 檔案內容
            rows = csv.reader(csvfile)

            stock_list=[]
            stock_df = pd.DataFrame(stock_list, columns = ['Number' , 'Name'])

            

            # 以迴圈輸出每一列
            for row in rows:
                if(row[5]==id):

                    stock_df=stock_df.append({'Number' : row[0] , 'Name' : row[1]},ignore_index=True)

            csvfile.close()

        return stock_df
    