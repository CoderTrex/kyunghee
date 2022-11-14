import pybithumb
import pyupbit
import numpy as np

all_ticker_name = []
ticker_all_name = pyupbit.get_tickers(fiat="KRW")
for item in ticker_all_name:
    all_ticker_name.append(item)

for ticker_name  in all_ticker_name:
    df = pyupbit.get_ohlcv(ticker=str(ticker_name), interval="day", count=500)
    df['ascent rate'] = ((df['close'] - df['open']) / df['close']) * 100
    df['range(=(high - low) * 0.5)'] = (df['high'] - df['low']) * 0.5
    df['target(=open + range)'] = df['open'] + df['range(=(high - low) * 0.5)'].shift(1)
    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target(=open + range)'], df['close'] / df['target(=open + range)'] - fee, 1)
    df['hpr'] = df['ror'].cumprod()
    df['mdd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\all_info\\all_info_{0}.xlsx".format(str(ticker_name)))