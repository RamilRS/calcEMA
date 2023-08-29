# calcEMA
project include following functions:

LoadPrices - function loads tick data from *.csv file using pandas, input parameters are filename and timeframe for creating candles, functions returns candles data (OHLC) in the given timeframe

calculate_ema - function calculates exponential moving average, input parameters are array with prices and the period of calculation

project requires the following packages to be installed:

pandas, mplfinance

run main.py

Screenshot. timeframe=1D, EMA(14)
![Screenshot. timeframe=1D, EMA(14) ](https://github.com/RamilRS/calcEMA/raw/master/plot1.jpg)

Screenshot. timeframe=1h, EMA(100)
![Screenshot. timeframe=1h, EMA(100) ](https://github.com/RamilRS/calcEMA/raw/master/plot1.jpg)
