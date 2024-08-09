import main
import tkinter as tk
root=tk.Tk()
root.geometry("500x800")
stock_var=tk.StringVar()
exchange_var = tk.StringVar()

def submit():
    name=stock_var.get()
    exchange = exchange_var.get()
    
    main.stock_info(name, exchange)
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
print(main.news_org("aapl")[0].link)


root.mainloop()
