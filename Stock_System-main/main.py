from typing import List
from flask import Flask ,render_template ,url_for,redirect
from flask_restful import Api
from flask import request
from numpy import equal
from resources.stock_chart import Stock_chart
from resources.stock_chart_copy import Stock_chart_copy
from resources.classes import class_search
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from resources.K_Chart import K_Chart
from resources.history import history
from resources.new2 import News

#from resources.account import Accounts, Account
app= Flask(__name__) # 初始化Flask物件，並貼上app這個標籤。接著我們就可以很方便的使用這個物件裡面的各種功能
api=Api(app)



@app.route("/classes", methods=['GET'])
def classes():
    input_class = request.args.get('')
    input_mode = request.args.get('mode')
    stock_class = class_search.get(input_class,input_mode)
    
    return render_template('class_search.html',**locals() ,stock_classes=stock_class ,input_classes=input_class)
 


@app.route("/stock", methods=['GET']) #轉公司代碼當日行情
def stock():
    input = request.args.get('input')
    # stock_chart_information = Stock_chart.get(input)
    name= K_Chart.get_name(input)
    if(name != ("#")):
        

        # fig = Stock_chart.create_figure(input)
        fig2 =K_Chart.create_image(input)
        #l = history.stock1(input)
        return render_template('stock_chart.html',**locals()  , stock_name = name  , img2 = fig2)
    else:
        return redirect(url_for('index'))

@app.route("/stock/day", methods=['GET']) #轉公司代碼當日行情
def stock_day():
    input = request.args.get('input')
    # stock_chart_information = Stock_chart.get(input)
    name= K_Chart.get_name(input)
    if(name != ("#")):
        
        # fig = Stock_chart.create_figure(input)
        fig2 =K_Chart.create_image(input)
        l = history.stock1(input)
        return render_template('stock_chart_day.html',**locals()  , stock_name = name  , img2 = fig2 , lq=l)
    else:
        return redirect(url_for('index'))

@app.route("/news", methods=['GET']) #轉公司代碼當日行情
def stock_new():
    input = request.args.get('input')
    # stock_chart_information = Stock_chart.get(input)
    name= K_Chart.get_name(input)
    if(name != ("#")):
        newsTime,newsUrl,newsTitle = News.news(input)
        # print(newsTitle)
        print("***************************")
        # fig = Stock_chart.create_figure(input)
        #fig2 =K_Chart.create_image(input)
        #l = history.stock1(input)
        return render_template('news_result.html',**locals()  , stock_name = name,time=newsTime,url=newsUrl,title=newsTitle)
    else:
        return redirect(url_for('index'))


@app.route('/') # 創造出主網域下的"/"這個網址，並定義了請求(request)該網址時可用的手段。
def index(): #定義一個函數，只要使用者請求相應的網址，就執行該函數。

 
    #上市公司
    Listed=["水泥工業","食品工業","塑膠工業","紡織纖維","電機機械","電器電纜","化學工業","生技醫療業",
        "玻璃陶瓷","造紙工業","鋼鐵工業","橡膠工業","汽車工業","半導體業","電腦及週邊設備業","光電業","通信網路業",
        "電子零組件業","電子通路業","資訊服務業","其他電子業","建材營造業","航運業","觀光事業","金融保險業",
        "貿易百貨業","油電燃氣業","存託憑證","ETF","受益證券","ETN","其他","市認購",
        "市認售","指數類","市牛證","市熊證"]

    

    #上櫃公司
    # OTC=["櫃食品","櫃塑膠","櫃紡織","櫃電機","櫃電器","櫃化工","櫃生技","櫃玻璃","櫃鋼鐵",
    # "櫃橡膠","櫃半導","櫃電腦","櫃光電","櫃通信","櫃電零","櫃通路","櫃資服",
    # "櫃他電","櫃營建","櫃航運","櫃觀光","櫃金融","櫃貿易","櫃油電","櫃文創",
    # "櫃農科","櫃電商","櫃其他","櫃管理","櫃公司","櫃ETF","櫃ETN","櫃認購",
    # "櫃認售","櫃指數類","櫃牛證","櫃熊證","櫃憑證"]

    OTC2=["化學工業","文化創意業","半導體業","生技醫療業","光電業","其他業","其他電子業",
    "油電燃氣業","金融保險業","建材營造業","食品工業","紡織纖維","航運業","通信網路業","貿易百貨業","塑膠工業",
    "資訊服務業","農業科技業","電子商務","電子通路業","電子零組件業","電腦及週邊設備業","電器電纜","電機機械","橡膠工業","鋼鐵工業","觀光事業"]

    Emerging=["化學工業","文化創意業","半導體業","生技醫療業","光電業","其他業","其他電子業",
    "油電燃氣業","股票金融保險業","建材營造業","食品工業","紡織纖維","航運業通信網路業","貿易百貨業","塑膠工業",
    "資訊服務業","農業科技業","電子商務","電子通路業","電子零組件業","電腦及週邊設備業","電機機械","鋼鐵工業","觀光事業"]
    
    return render_template("index.html", Listed=Listed ,OTC=OTC2, Emerging=Emerging)



@app.route("/from_start")
def from_start():
    return render_template("from_start.html")



if __name__ == '__main__':
    app.debug = True
    
    app.run(host='127.0.0.1',port=5000) 


 