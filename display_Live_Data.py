import chartFunctions
import plotly.graph_objects as go
import yfinance as yf
import streamlit as st
import numpy as np
import pandas
import math

#---------------------------------------------------
import os

import yfinance as yf
import streamlit as st
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure
#---------------------------------------------------


def containerDisplay():
    df = pandas.read_csv("StockAnalysisApp/all_data[DJI30].txt")

    st.markdown("# Live Data")
    st.markdown("## ATR")

    
    imc= int(df.iloc[-1:,6])
    st.markdown("The average true range is the following:")
    fig=chartFunctions.atr_chart(imc)
    st.write(fig)

    file1 = open('StockAnalysisApp/fractalbreakAllBuy[DJI30].txt', 'r')
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
    file4 = open("StockAnalysisApp/OneHourFractalDifference[DJI30].txt", "r")
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
    #
    fileSignal = open("StockAnalysisApp/recordBreakTypeInfo[DJI30].txt", "r")
    LineSignal = fileSignal.readlines()

    signalValues = []
    signalType = []
    signalTime = []
    signalTarget = []

    # Strips the newline character
    for line in LineSignal:
        vlaue = (line.split(','))
        signalType.append(vlaue[0])
        signalTime.append(vlaue[1])
        signalTarget.append(vlaue[2])

    signalData = {
        "Type": signalType,
        "Time": signalTime,
        "Target": signalTarget
    }

    dfSignals = pandas.DataFrame(signalData, columns = ['Type','Time', 'Target'])


    #---------------------------------------------
    st.write("""
    # Quantitative Analysis of DJI
    Shown are the values **MACD, EMAs** and ***ATR*** of DJI!
    """)
    st.write("""
    With particular focus on fractal geometry patterns in finanical time series data
    https://www.researchgate.net/publication/281964401_Fractal_Dimensional_Analysis_in_Financial_Time_Series
    http://www.jonathankinlay.com/Articles/Long%20Memory%20and%20Regime%20Shifts%20in%20Asset%20Volatility.pdf
    """)

    st.write(df.describe())
    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    #define the ticker symbol
    tickerSymbol = 'DJI'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = df.iloc[-400:,7]

   


    d = {
        "4hr":df.iloc[-700:,1],
        "1hr": df.iloc[-700:,2],
        "5min": df.iloc[-700:,3]
    }

    dfChart = pandas.DataFrame(d, columns = ['4hr','1hr', '5min'])
    chart_data = dfChart 
    st.write("""
    ## Live: Bid Price Relative To 5M,1H,4H Fractal movements
    Values below 0% are Bearish, Values above 100% are Bullish!
    """)

    st.line_chart(chart_data)
    #-------------------------------------------------
    d_macd = {
        "1hr": df.iloc[-1000:,8],
        "5min": df.iloc[-1000:,9],
        "ATR": df.iloc[-1000:,6]
    }

    dfChart_macd = pandas.DataFrame(d_macd, columns = ['1hr', '5min', 'ATR'])

    st.write("""
    ## Live: MACD 5M, 1H & ATR
    """)

    st.area_chart(dfChart_macd)

    #------------------------------------------------------
    st.write("""
    ## Live: Most Recent Signals
    """)
    st.write(dfSignals.tail())
    #-------------------------------------------------
    d_ema = {
        "1hr": df.iloc[-1000:,4],
        "5min": df.iloc[-1000:,5]}

    dfChart_ema = pandas.DataFrame(d_ema, columns = ['1hr', '5min'])

    st.write("""
    ## Live: EMA % 5M, 1H
    """)

    st.line_chart(dfChart_ema)

    #------------------------------------------------------


    st.write("""
    ## 1 Hour Fractal range
    """)
    st.line_chart(v4[-400:])

    st.write("""
    ## Bullish Fractal Breakout range 1 Hour
    """)
    st.line_chart(v[-100:])


    st.write("""
    ## Bid Price
    """)
    st.line_chart(df.iloc[-50:,7])

    #---------------------------------------------
    #read hurst data
    hurst_data_file = open('StockAnalysisApp/5_HurstData_for_[DJI30].txt', 'r')
    Line_hurst_data_file = hurst_data_file.readlines()

    hurstArray = []

    # Strips the newline character
    for line in Line_hurst_data_file:
        hurst = (float(line.strip()))
        hurstArray.append(hurst )
    st.write("""
    ## Hurst value EUR/USD
    """)

    hurst_data = {
        "5min": hurstArray
    }

    dfChart_hurst_data = pandas.DataFrame(hurst_data, columns = ['5min'])


    st.write(dfChart_hurst_data.describe())
    #---------------------------------------------
    #---------------------------------------------
    #read hurst data
    tfm_data_file = open('StockAnalysisApp/5_DCs_Record_[DJI30].txt', 'r')
    Line_tfm_data_file = tfm_data_file.readlines()

    tfmArray = []

    # Strips the newline character
    for line in Line_tfm_data_file:
        if not line.strip():
            cp = 1
        else:
            tfm = (float(line.strip()))
            tfmArray.append(tfm)
    tfm_data = {
        "Fractal ranges": tfmArray
    }

    dfChart_tfm = pandas.DataFrame(tfm_data, columns = ['Fractal ranges'])

    st.write("""
    ## fractal ranges data dji
    """)
    st.write(dfChart_tfm.describe())

    st.write("""
    ## total fractal movement dji
    """)
    st.line_chart(tfmArray)

    st.write(dfChart_tfm.describe())
    st.write(dfChart_tfm.quantile(0.656))