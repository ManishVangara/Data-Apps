import yfinance as yf
import streamlit as st
import pandas as pd

st.title('Simple Stock Price App')




google = st.button('GOOGLE')
apple = st.button("APPLE")
tesla= st.button("TESLA")
meta = st.button("META")
netflix= st.button("NETFLIX")

stocks={'apple':'AAPL', 'google': 'GOOGL', 'tesla':'TSLA', 'meta' : 'META', 'netflix' : 'NFLX'}

#Defining Ticker symbol for Google stock


if google==True:
    tickerSymbol=stocks['google']
elif apple==True:
    tickerSymbol=stocks['apple']
elif tesla==True:
    tickerSymbol=stocks['tesla']
elif meta==True:
    tickerSymbol=stocks['meta']
elif netflix == True:
    tickerSymbol=stocks['netflix']

st.text('Shown are the stock closing price and volume')

try:
    # Getting the data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # Getting the historical prices for this ticker (Google)
    tickerDf = tickerData.history(period='1d', start='2010-5-31')

    # Open High Low Close Volume Dividends Stock Splits

    st.write('### Close')

    st.line_chart(tickerDf.Close)

    st.write("""
    ### Volume 
    """)
    st.line_chart(tickerDf.Volume)
except:
    st.write("""
    ### Select a Stock
    """)
try:
    if tickerSymbol != '':
        st.write('Recent 10 days of the stock performance')
    st.dataframe(tickerDf.tail(10))
except:
    print('')




