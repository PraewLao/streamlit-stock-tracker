import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Tracker", layout="centered")
st.title("📈 Real-Time Stock Tracker")

ticker = st.text_input("Enter stock ticker (e.g. AAPL, TSLA):", value="AAPL")

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        price = info.get("regularMarketPrice", "N/A")
        pe_ratio = info.get("trailingPE", "N/A")
        pb_ratio = info.get("priceToBook", "N/A")

        st.subheader(f"📊 {ticker.upper()} Summary")
        st.metric("Current Price", f"${price}")
        st.write(f"**P/E Ratio:** {pe_ratio}")
        st.write(f"**P/B Ratio:** {pb_ratio}")

    except Exception as e:
        st.error(f"Error retrieving data: {e}")
