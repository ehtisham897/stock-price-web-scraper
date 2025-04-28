# stock-price-web-scraper
This project fetches stock prices and saves them in an Excel file.
This Python project uses web scraping techniques to fetch real-time stock price data from a financial website and save the collected data into an Excel file. The tool is designed to make it easier for users to track stock prices over time and save the data in a structured manner for analysis and record-keeping.

Key Features:
Real-Time Data Collection: The project scrapes live stock prices from popular financial websites like Yahoo Finance or others.

Excel File Storage: The scraped data is saved in an Excel file (stock_prices.xlsx) where each stock's price is stored in a clean, easy-to-read format.

Automation: This script can be run periodically to fetch updated stock prices automatically.

Data Columns: The Excel file will contain the stock symbol, name, and price of the stock, which can be further analyzed.

Technologies Used:
Python: The main programming language used for scraping and handling data.

BeautifulSoup: Used to scrape data from web pages.

Requests: A library used to fetch the page content.

Pandas: Used for managing data and saving it into Excel format.

Project Flow:
Scrape Stock Data: The project first scrapes stock data from a specified source.

Clean the Data: The raw data is cleaned to remove unnecessary information and formatted for easy storage.

Save Data to Excel: After collecting and cleaning the data, the script saves it into an Excel file named stock_prices.xlsx.
