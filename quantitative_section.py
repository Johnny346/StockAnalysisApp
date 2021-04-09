#---------------------------------------------------
import chartFunctions
import plotly.graph_objects as go
import os
import pandas

import yfinance as yf
import streamlit as st
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure
#---------------------------------------------------
#@st.cache  # This function will be cached
def getMTwoData():

    #------ get M2 data from file and chache it ---------------
    fileSignal = open("StockAnalysisApp/FED_M2SL.txt", "r")
    LineSignal = fileSignal.readlines()

    signalValues = []
    signalDates = []
    countValues = 1
    countArray = []
    # Strips the newline character
    for line in LineSignal:
        vlaue = (line.split('	'))
        signalDates.append(vlaue[0])
        signalValues.append(vlaue[1])
        countValues = countValues + 1
        countArray.append(countValues)

    mTwo_data = {
        "MTwo": signalValues,
        "counter": countValues 
    }

    return mTwo_data


#@st.cache  # This function will be cached
def getDJIOpenCloseData():

    #------ get M2 data from file and chache it ---------------
    fileSignal = open("StockAnalysisApp/49153_HighLow_[DJI30].txt", "r")
    LineSignal = fileSignal.readlines()

    signalValues = []
    signalDates = []
    countValues = 1
    countArray = []
    # Strips the newline character
    for line in LineSignal:
        vlaue = (line.split(','))
        signalDates.append(vlaue[0])
        signalValues.append(vlaue[1])
        countValues = countValues + 1
        countArray.append(countValues)

    mTwo_data = {
        "MTwo": signalValues,
        "counter": countValues 
    }

    return mTwo_data


def containerDisplay():
    st.write("""""")
    st.write("""# Corralation Study: """,""" Dow Jones Index""")
    st.write("""## To evaluate if there is a corralation between the M2 money supply and Dow Jones Index price, between the years 2013 and 2021""")

    #------ get M2 data from file and chache it ---------------
    
    mTwoDF = pandas.DataFrame(getMTwoData(), columns = ['MTwo','counter'])
    st.write("""M2 Money Monthly Supply from 2013 - 2021""")
    st.line_chart(mTwoDF)

    djiOpenCloseDF = pandas.DataFrame(getDJIOpenCloseData(), columns = ['MTwo','counter'])
    st.write(""" DJI Open Monthly Price from 2013 - 2021""")
    st.line_chart(djiOpenCloseDF )
    djiList = getDJIOpenCloseData().values()

    djiArrayHold = []
    mTwoArrayHold = [] 
   
    

    for i in djiOpenCloseDF['MTwo'].to_numpy():
        djiArrayHold.append(int(float(i)))
    for i in mTwoDF['MTwo'].to_numpy():
        mTwoArrayHold.append(int(float(i)))

    matrix = np.corrcoef(mTwoArrayHold,djiArrayHold)
    st.write(""" # Matrix coefficient result """)

    st.write(int(float(matrix[0][1]*100)),"""%""")
    #---------------------------------------------------
