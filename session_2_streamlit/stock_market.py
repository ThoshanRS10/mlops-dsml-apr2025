import streamlit as st
import pandas as pd
import numpy as np 

import yfinance as yf

st.title('A Sample Stock Market App')

# st.header('Stock Market Data')
# st.subheader('Stock Price Data')
# st.write('This is a simple stock market app that fetches and displays stock price data.')

# #examples of widgets
# if st.checkbox('Show Widgets'):
#     st.write('Checkboxes are useful for binary options.')
#     st.radio('Select an option:', ('Option 1', 'Option 2', 'Option 3'))         
#     st.write('Radio buttons are useful for single selection.')
#     st.selectbox('Select a stock:', ('AAPL', 'GOOGL', 'MSFT'))
#     st.write('Select boxes are useful for single selection with a dropdown.')
#     st.multiselect('Select multiple stocks:', ('AAPL', 'GOOGL', 'MSFT'))
#     st.write('Multi-select boxes are useful for multiple selection.')
#     st.slider('Select a range of values:', 0, 100, (25, 75))
#     st.write('Sliders are useful for selecting a range of values.')
#     st.number_input('Enter a number:', min_value=0, max_value=100, value=50)
#     st.write('Number inputs are useful for entering numeric values.')
#     st.text_input('Enter some text:')
#     st.write('Text inputs are useful for entering text.')
#     st.text_area('Enter a longer text:')
#     st.write('Text areas are useful for entering longer text.')
#     st.date_input('Select a date:')
#     st.write('Date inputs are useful for selecting dates.')
#     st.time_input('Select a time:')
#     st.write('Time inputs are useful for selecting times.')


start_date = st.date_input("Start date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2023-01-01"))

#symbol="AAPL" #perform analysis on this stock

ticker_symbol = st.text_input("Enter a stock symbol:", "AAPL") #create a text input for the stock symbol
symbol = ticker_symbol.upper() #convert the stock symbol to uppercase

ticker_data = yf.Ticker(symbol) #create a Ticker object for the stock symbol
ticker_df = ticker_data.history(period = '1d', start=start_date, end=end_date) #get historical data for the stock symbol from start_date to end_date

st.dataframe(ticker_df) #display the dataframe in the Streamlit app

#let's create a chart of the stock price data
st.write("## Closing Price Chart")
st.line_chart(ticker_df['Close']) #create a line chart of the closing price data, inside line_chart pass the series of closing prices from the dataframe

col1, col2 = st.columns(2) #create two columns for the app layout, specify the number of columns as 2	

with col1:	 #create a context manager for the first column
    st.write("## Closing Price Chart")
    st.line_chart(ticker_df['Close']) #create a line chart of the closing price data, inside line_chart pass the series of closing prices from the dataframe            

with col2:	 #create a context manager for the second column
    st.write("## Volume Chart")
    st.line_chart(ticker_df['Volume']) #create a line chart of the volume data, inside line_chart pass the series of volume from the dataframe