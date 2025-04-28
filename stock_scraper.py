import yfinance as yf
import pandas as pd

# 20 stock symbols
stock_symbols = [
    "AAPL", "GOOG", "MSFT", "TSLA", "AMZN",
    "META", "NFLX", "NVDA", "AMD", "INTC",
    "UBER", "BABA", "ORCL", "CSCO", "PYPL",
    "ADBE", "CRM", "PEP", "KO", "WMT"
]

# Empty list to store data
stock_data = []

for symbol in stock_symbols:
    try:
        stock = yf.Ticker(symbol)
        stock_price = stock.history(period="1d")["Close"].iloc[0]
        price_with_dollar = f"${round(stock_price, 2)}"
        stock_data.append({"Symbol": symbol, "Price": price_with_dollar})
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# DataFrame me convert
df = pd.DataFrame(stock_data)

# Excel file me save
df.to_excel("stock_prices.xlsx", index=False)

print(" Stock prices with $ sign saved successfully in 'stock_prices.xlsx'!")
