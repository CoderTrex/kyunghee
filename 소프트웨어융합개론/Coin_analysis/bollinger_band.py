import pyupbit
import matplotlib.pyplot as plt

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute15", count=200)
w_size = 20
pd = 2

df["Moving Average"] = df["close"].rolling(window=w_size,min_periods=1).mean()
df["Standard Deviation"]  = df["close"].rolling(window=w_size, min_periods=1).std()
df["Upper BollingerBand"] = df["Moving Average"] + (df["Standard Deviation"] * pd)
df["lower BollingerBand"] = df["Moving Average"] - (df["Standard Deviation"] * pd)
df = df.dropna()

