import yfinance as yf
from bs4 import BeautifulSoup
import requests
htlm_texts = requests.get('https://www.google.com/finance/quote/AAPL:NASDAQ').text
soup = BeautifulSoup(htlm_texts, 'html.parser')
News = soup.find('div', class_ = 'P6K39c')
print(News.text)
def news_org(ticker):
    
    tick = yf.Ticker(ticker)
    info = tick.news
    with open(f'{ticker}.txt',  'w') as f:
        for i in info:
 
       
          f.write(f"Title: {i.get("title")}\n")
          f.write(f"Publisher: {i.get("publisher")}\n")
          f.write(f"Related Tickers: {i.get("relatedTickers")}\n")
          f.write(f"Link: {i.get("link")}\n")
          f.write("\n")
