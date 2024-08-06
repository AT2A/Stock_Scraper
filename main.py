from flask import Flask,request, render_template
import yfinance as yf
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
  
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


ticker = my_form_post()
tick = yf.Ticker(ticker)


info = tick.news
with open(f'{ticker}.txt',  'w') as f:
    for i in info:
 
       
       f.write(f"Title: {i.get("title")}\n")
       f.write(f"Publisher: {i.get("publisher")}\n")
       f.write(f"Related Tickers: {i.get("relatedTickers")}\n")
       f.write(f"Link: {i.get("link")}\n")
       f.write("\n")
  