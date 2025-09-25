import yfinance as yf
from bs4 import BeautifulSoup
import pandas as pd
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "iframe"
import warnings
import kaleido
warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,subplot_titles=("Historical Share Price", "Historical Revenue"),vertical_spacing=0.3)

    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date),y=stock_data_specific.Close.astype(float),name="Share Price"),row=1, col=1)

    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date),y=revenue_data_specific.Revenue.astype(float),name="Revenue"),row=2, col=1)

    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)

    fig.update_layout(showlegend=False,height=900,title=stock,xaxis_rangeslider_visible=True)

    fig.show()
    fig.write_html("gme_graph.html")


def tesla_analyze():
    tesla = yf.Ticker("TSLA")
    tesla_data = tesla.history("max")
    tesla_data.reset_index(inplace=True)
    print(tesla_data.head())
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data,"html.parser")
    tables = pd.read_html(html_data,flavor="bs4")
    tesla_revenue = pd.DataFrame(columns=["Date","Revenue"])

    for row in soup.find("tbody").find_all("tr"):
        cel = row.find_all("td")
        date = cel[0].text
        revenue = cel[1].text
        tesla_revenue = pd.concat([tesla_revenue,pd.DataFrame({"Date":[date],"Revenue":[revenue]})])
        
    tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r'[,|$]',"",regex=True)
    tesla_revenue.dropna(inplace= True)
    tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
    print(tesla_revenue.tail())
    make_graph(tesla_data,tesla_revenue,"TSLA")

def gme_analyze():
    gme = yf.Ticker("GME")
    gme_data = gme.history("max")
    gme_data.reset_index(inplace=True)
    print(gme_data.head())

    url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
    html_data_2 = requests.get(url2).text
    soup = BeautifulSoup(html_data_2,"html.parser")
    gme_revenue = pd.DataFrame(columns=["Date","Revenue"])
    for row in soup.find("tbody").find_all("tr"):
        cel = row.find_all("td")
        date = cel[0].text
        revenue = cel[1].text
        gme_revenue = pd.concat([gme_revenue,pd.DataFrame({"Date":[date],"Revenue":[revenue]})])

    gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r"[,$]","",regex=True)
    gme_revenue = gme_revenue[gme_revenue["Revenue"]!= ""]
    gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors="coerce")
    print(gme_revenue.tail())
    make_graph(gme_data,gme_revenue,"GME")

while(True):
    print("Choose Stock to analyze : \n [1] Tesla\n [2] GME")
    user = input()
    if user == "1":
        tesla_analyze()
        break
    elif user == "2":
        gme_analyze()
        break
    else:
        print("Please enter correct number\n")
