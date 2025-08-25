import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Learning App", layout="wide")

# --- Title ---
st.title("📈 Stock Learning App")
st.write("Learn investing by exploring stocks with moving averages and volatility graphs.")

# --- Sidebar for user input ---
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL, TSLA, MSFT):", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# --- Download stock data ---
try:
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        st.warning("No data found for this ticker. Try another one.")
    else:
        st.subheader(f"Stock Data for {ticker}")
        st.write(data.tail())

        # --- Plot price chart with 50-day & 200-day moving averages ---
        data['50_MA'] = data['Close'].rolling(window=50).mean()
        data['200_MA'] = data['Close'].rolling(window=200).mean()

        st.subheader("Price Chart with Moving Averages")
        fig, ax = plt.subplots(figsize=(12,6))
        ax.plot(data.index, data['Close'], label='Close Price', color='blue')
        ax.plot(data.index, data['50_MA'], label='50-Day MA', color='orange')
        ax.plot(data.index, data['200_MA'], label='200-Day MA', color='red')
        ax.set_title(f"{ticker} Price with Moving Averages")
        ax.legend()
        st.pyplot(fig)

        # --- Volatility (daily % change) ---
        st.subheader("Volatility (Daily Returns)")
        data['Daily Return'] = data['Close'].pct_change()
        fig2, ax2 = plt.subplots(figsize=(12,6))
        ax2.plot(data.index, data['Daily Return'], label='Daily Return', color='purple')
        ax2.axhline(0, color='black', linewidth=1)
        ax2.set_title(f"{ticker} Daily Volatility")
        ax2.legend()
        st.pyplot(fig2)

except Exception as e:
    st.error(f"Error fetching data: {e}")
