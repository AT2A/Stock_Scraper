import main
import tkinter as tk
root=tk.Tk()
root.geometry("500x800")
stock_var=tk.StringVar()
exchange_var = tk.StringVar()

def toText(name, exchange):
    print("works")
    info = main.stock_info(name, exchange)
    analystList = main.stockAnalysis(name)
    newsList = main.news_org(name)
    with open(f'{name}.txt', 'w', encoding="utf-8") as f:
        f.write(f"""Stock Name: {name}\n
Previous Close: {info.get("prevClose")}                
Day Range: {info.get("prevClose")}
Year Range: {info.get("yearRange")}            
Market Cap: {info.get("marketCap")}  
Average Volume: {info.get("avgVolume")}   
P/E Ratio: {info.get("PE")}  
Dividend Yield: {info.get("divYield")}  
Exchange: {info.get("exchange")}                 

Analyst Ratings\n""")
        for index,x in enumerate(analystList):
            f.write(f"""{x.date}   {x.name}  {x.firm}  {x.rating}   {x.action}   {x.priceTarget}  \n\n""")
        
        f.write("News\n")      
        for x in newsList:
            f.write(f"""Title: {x.title}
Publisher: {x.publisher}
Related Tickers: {x.relatedTickers}
Link: {x.link}\n\n""")


def submit():
    name=stock_var.get()
    exchange = exchange_var.get()
    toText(name, exchange)
    stock_var.set("")
    exchange_var.set("")
    
stock_label = tk.Label(root, text = 'Stock Ticker', font=('calibre',10, 'bold'))
stock_entry = tk.Entry(root,textvariable = stock_var, font=('calibre',10,'normal'))

exchange_label = tk.Label(root, text = 'Exchange', font=('calibre',10, 'bold'))
exchange_entry = tk.Entry(root,textvariable = exchange_var, font=('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = submit)

stock_label.grid(row=0,column=0)
stock_entry.grid(row=0,column=1)
exchange_label.grid(row=1,column=0)
exchange_entry.grid(row=1,column=1)

sub_btn.grid(row=2,column=1)
hello = "hello"



root.mainloop()
