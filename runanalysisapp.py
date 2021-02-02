import yfinance as yf
import streamlit as st
import numpy as np
#---------------------------------------------------
import os

import yfinance as yf
import streamlit as st
import numpy as np
#---------------------------------------------------
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


file1 = open('fractalbreakAllBuy[DJI30].txt', 'r')
Lines = file1.readlines()

count = 0
v = []
count = []
counter = 0

# Strips the newline character
for line in Lines:
    vlaue = (line.strip())
    vlaue = vlaue[20:len(vlaue)]

    #print(vlaue)
    v.append(float(vlaue.strip()))
    counter = counter + 1
    #print(counter)
    count.append(counter)



#---------------------------------------------
file4 = open("OneHourFractalRelativeToBid[DJI30].txt", "r")
Line4 = file4.readlines()

count4 = 0
v4 = []
count4 = []
counter4 = 0
# Strips the newline character
for line in Line4:
    vlaue = (float(line.strip()))
    v4.append(vlaue)
#---------------------------------------------


#---------------------------------------------
st.write("""
# Quantitative Analysis of DJI
# Price App
Shown are the stock **closing price** and ***volume*** of DJI!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'DJI'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-1-31', end='2021-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Live: Bid Relative To 1H Fractal movements as percentage
""")
st.write("""
 Current Value: 
""", round(v[-1]),"""%""")
st.line_chart(v[-100:])

st.write("""
## Bullish Fractal Breakout range 1 Hour
""")
st.line_chart(v4)


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

#file updated
#file updated
#file updated
#file updated
#file updated
#file updated
