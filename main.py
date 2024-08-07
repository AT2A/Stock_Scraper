import yfinance as yf
from bs4 import BeautifulSoup
import requests
htlm_texts = requests.get('https://www.google.com/finance/quote/NVDA:NASDAQ').text
soup = BeautifulSoup(htlm_texts, 'html.parser')
infoList = soup.find_all('div', class_ = 'P6K39c')

stockInfo = {
  "prevClose":infoList[0].text,
  "dayRange":infoList[1].text,
  "yearRange":infoList[2].text,
  "marketCap":infoList[3].text,
  "avgVolume":infoList[4].text,
  "PE":infoList[5].text,
  "divYield":infoList[6].text,
  "exchange":infoList[7].text
  }

print(stockInfo.get("marketCap"))

#use google to get basic stock info
#use stockAnaylsis to get forecast info
#use reddit too
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
