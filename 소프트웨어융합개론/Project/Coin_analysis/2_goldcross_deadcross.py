import pyupbit
import talib as ta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ticker = "KRW-BTC"

df = pyupbit.get_ohlcv(ticker, interval="minute60", count=144)

# MA : move average로 평균 이동에 대한 정보이다.
df['MA'] = ta.SMA(df['close'], 20) # 20시간 이평선이다. -> 중기 이평선
df['5MA']  = ta.SMA(df['close'], 5) # 5시간 이평선이다.  -> 단기 이평선

df[['close', 'MA', '5MA']].plot(figsize=(12, 6))
plt.title("BTC-6 day", {"fontsize" : 20})
plt.show()