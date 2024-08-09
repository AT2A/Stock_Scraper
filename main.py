import yfinance as yf
from bs4 import BeautifulSoup
import requests
#use google to get basic stock info
#use stockAnaylsis to get forecast info

    #anaylist ratings
#use reddit too

#Stock Analysis Website ----------------------------------------------------------------------------------------------
#Class of the info of each stock analyst

class analyst:
  
  def _init_(self):
    self.name = ''
    self.firm = ''
    self.rating = ''
    self.action = ''
    self.priceTarget = ''
    self.upside = ''
    self.date = ''
def stockAnalysis(ticker):  
  stockAnalysisHTML = requests.get(f'https://stockanalysis.com/stocks/{ticker}/ratings/').text
  anaylsisSoup = BeautifulSoup(stockAnalysisHTML, 'html.parser')
  table = anaylsisSoup.find('tbody' , class_ = "svelte-1c46ly0")
  allAnalyst = table.find_all('tr')
  #List that stores each of the analyst objects and the loop, that loops through the websites table and extracts the data
  analystList = []
  
  for index,x in enumerate(allAnalyst):
    analystList.append(analyst())
    analystList[index].name = x.find('div', class_ = 'analyst-name svelte-1c46ly0').text
    analystList[index].firm = x.find('td', class_ = 'desktop-only max-w-[120px] text-smaller svelte-1c46ly0').text
    analystList[index].rating = x.find('td', class_ = 'desktop-only text-sm svelte-1c46ly0').span.text
    analystList[index].action = x.find('td', class_ = 'desktop-only text-smaller svelte-1c46ly0').text
    analystList[index].priceTarget = x.find('td', class_ = 'desktop-only min-w-[80px] text-smaller svelte-1c46ly0').text
    analystList[index].upside = x.find('td', class_ = 'desktop-only text-right text-smaller svelte-1c46ly0').text
    analystList[index].date = x.find('td', class_ = 'whitespace-nowrap align-middle text-smaller font-semibold svelte-1c46ly0').text

  return analystList
#------------------------------------------------------------------------------------------------------------------------------------------


#Stock info from google finance
def stock_info(ticker, exchange):
  htlm_texts = requests.get(f'https://www.google.com/finance/quote/{ticker}:{exchange}').text
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
  return stock_info

#News on stock through yfinance

class news:
  def __init__ (self):
    self.title = ''
    self.publisher = ''
    self.relatedTickers = ''
    self.link = ''
    
def news_org(ticker):
    
    tick = yf.Ticker(ticker)
    info = tick.news
    newsList = []
   
    for index,article in enumerate(info):
      
      newsList.append(news())
      newsList[index].title = article.get("title")
      newsList[index].publisher = article.get("punlisher")
      newsList[index].relatedTickers = article.get("relatedTickers")
      newsList[index].link = article.get("link") 
    return newsList


