import talib as ta
import pyupbit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = "KRW-ETH"
df = pyupbit.get_ohlcv(ticker, interval = 'minute60', count=144)
df['MA'] = ta.SMA(df['close', 20])
df[['close','MA']].plot(figsize=(12,6))
plt.title("ETH - 6 Days", {"fontsize" : 20})
plt.show()