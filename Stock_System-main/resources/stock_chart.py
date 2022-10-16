from requests import request
from flask_restful import Resource
import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO



class Stock_chart(Resource):
    def get(id):
        # open_stock = 0
        # high_stock = 0
        # close_stock =0
        # low_stock = 1000
        # open_stock = 0
        # stocl_ohcl=[open_stock,high_stock,close_stock,low_stock]
        # count=0
        try:
            stock_file = 'resources\intraday_chart_'+id+'.json'
            with open(stock_file, 'r') as obj:
                data = json.load(obj)

            obj.close()

            # for time in data["data"]["chart"]:
            #     if(count==0):
            #         stocl_ohcl[open_stock] =  data["data"]["chart"][time]["open"]
                

            return  data
        except:
            return "#"

    def get_name(id):
        stock_file1 = 'resources\intraday_meta_'+id+'.json'
        with open(stock_file1, 'r',encoding="utf-8") as obj1:
            data1 = json.load(obj1)

        stock_name =data1["data"]["meta"]["nameZhTw"]
        obj1.close()

        return  stock_name

    def create_figure(id):
            stock_file =  'resources\intraday_chart_'+id+'.json'
            with open(stock_file, 'r') as obj:
                data = json.load(obj)

            obj.close()

            xpt=[]
            ypt=[]
            count=0
            for time in data["data"]["chart"]: 
                count+=1
                xpt.append((count/60)+9) #筆數/60為換算成小時，+9為開盤時間
                ypt.append(data["data"]["chart"][time]["open"])
            
            open1 = data["data"]["chart"]["2021-06-07T01:01:00.000Z"]["open"]

            plt.figure(figsize=(4.5,4.5))
            plt.axis([9 , 13.5, open1*0.85, open1*1.15])
            plt.plot(xpt,ypt) #畫線
            plt.title("Today", fontsize=24) #圖表標題
            plt.xlabel("Time", fontsize=10) #x軸標題
            plt.ylabel("Price", fontsize=10) #y軸標題
            
            # plt.show() #顯示繪製的圖形

            # figure 保存为二进制文件

            buffer = BytesIO()
            plt.savefig(buffer)
            plot_data = buffer.getvalue()
            # 将matplotlib图片转换为HTML
            imb = base64.b64encode(plot_data)  # 对plot_data进行编码
            ims = imb.decode()
            imd = "data:image/png;base64," + ims

            return imd



