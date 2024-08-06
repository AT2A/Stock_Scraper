import main
# Program to make a simple 
# login screen 


import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
stock_var=tk.StringVar()



def submit():
    name=stock_var.get()
    main.news_org(name)
    stock_var.set("")
    
stock_label = tk.Label(root, text = 'Stock Ticker', font=('calibre',10, 'bold'))
stock_entry = tk.Entry(root,textvariable = stock_var, font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)
stock_label.grid(row=0,column=0)
stock_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)


root.mainloop()
