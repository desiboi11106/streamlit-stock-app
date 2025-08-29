import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="Finance Dashboard", page_icon="💰", layout="wide")

# --- Sidebar ---
st.sidebar.title("⚙️ Controls")
chart_type = st.sidebar.selectbox("Chart Type", ["Line", "Bar", "Area"])
num_points = st.sidebar.slider("Number of Data Points", 10, 200, 50)

# --- Fake Finance Data ---
dates = pd.date_range("2023-01-01", periods=num_points)
prices = np.cumsum(np.random.randn(num_points)) + 100
df = pd.DataFrame({"Date": dates, "Price": prices}).set_index("Date")

# --- Title ---
st.title("💹 Finance Dashboard")
st.write("Demo app with Streamlit to show graphs and tables.")

# --- Graph Section ---
st.subheader("📊 Stock Prices")
if chart_type == "Line":
    st.line_chart(df)
elif chart_type == "Bar":
    st.bar_chart(df)
else:
    st.area_chart(df)

# --- Matplotlib Custom Plot ---
st.subheader("Matplotlib Plot")
fig, ax = plt.subplots()
ax.plot(df.index, df["Price"], color="royalblue", linewidth=2)
ax.set_title("Stock Price Trend", fontsize=16, color="darkred")
st.pyplot(fig)

# --- Data Table ---
st.subheader("📑 Raw Data")
st.dataframe(df.reset_index())
