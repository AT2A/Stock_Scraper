# Stock News Scraper

## Description
The scraper scrapes Google Finance, stockanalysis.com, and Yahoo Finance to retrieve the day stock information,
it's all displayed in a text file and Gemini ai is used to summarize all the information which is also included in the text file

A simple GUI uses tKinter that takes the stock ticker and stock exchange of the stock
That information is used to get the link to the webpage on Google Finance and Stock Analysis to scrape the financial and analyst data, it is also used to get multiple news articles from the yFinance API the content of each of the articles is also scrapped
The information is put into a text file and is sent to the Gemini API and is summarized and the summary is displayed in the text file.
