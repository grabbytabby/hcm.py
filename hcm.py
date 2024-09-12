import streamlit as st
import pandas as pd
import numpy as np
from tqdm import tqdm

# Dummy data to simulate prices and trade volume
def simulate_trade_data():
    time_points = pd.date_range(start="2024-09-01", periods=100, freq="T")
    price = np.cumsum(np.random.randn(len(time_points)) * 0.5 + 100)
    volume = np.random.randint(1, 1000, size=len(time_points))
    return pd.DataFrame({"time": time_points, "price": price, "volume": volume})

# Simulated Data
trade_data = simulate_trade_data()

# Streamlit App Layout
st.title("HarmonyChain and McM Live Exchange")
st.sidebar.header("Device Configuration")

# Device Options
device = st.sidebar.selectbox("Select Device for Execution", ["auto", "cuda", "cpu", "openvino", "tpu", "xpu"])

st.sidebar.header("Trading Configuration")
max_trades = st.sidebar.slider("Max Number of Trades", min_value=1, max_value=100, value=10)
block_size = st.sidebar.slider("Block Size", min_value=1, max_value=32, value=16)

st.write(f"Device selected: {device}")
st.write(f"Max trades allowed: {max_trades}")
st.write(f"Block size: {block_size}")

if st.button("Start Trading Simulation"):
    st.write("Simulating trades...")

    for _ in tqdm(range(max_trades)):
        st.write(f"Trade executed at price: {trade_data['price'].iloc[np.random.randint(len(trade_data))]}")

    st.write("Trading simulation complete!")

# Display trade data
st.write("## Trade Data")
st.line_chart(trade_data[['price']])
st.bar_chart(trade_data[['volume']])
