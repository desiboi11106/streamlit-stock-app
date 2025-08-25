import yfinance as yf
import matplotlib.pyplot as plt

# Ask user for a stock ticker
ticker = input("Enter a stock ticker symbol (e.g., AAPL, TSLA, MSFT): ")

# Download data (last 1 year)
data = yf.download(ticker, period="1y")

# Plot 1: Stock closing price
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label="Closing Price")
plt.title(f"{ticker} Stock Price (1 Year)")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.show()

# Plot 2: Daily Volatility (percent change)
data['Daily Return'] = data['Close'].pct_change()
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Daily Return'], label="Daily Return (Volatility)")
plt.title(f"{ticker} Daily Volatility (1 Year)")
plt.xlabel("Date")
plt.ylabel("Daily % Change")
plt.legend()
plt.show()

# Plot 3: Moving averages (50-day vs 200-day)
data['50 MA'] = data['Close'].rolling(window=50).mean()
data['200 MA'] = data['Close'].rolling(window=200).mean()

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label="Closing Price")
plt.plot(data.index, data['50 MA'], label="50-Day MA", color="orange")
plt.plot(data.index, data['200 MA'], label="200-Day MA", color="red")
plt.title(f"{ticker} 50-Day vs 200-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.show()