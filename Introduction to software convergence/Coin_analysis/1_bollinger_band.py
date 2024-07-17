import pyupbit
import matplotlib.pyplot as plt

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute15", count=200)
w_size = 20
pd = 2

df["Moving Average"] = df["close"].rolling(window=w_size,min_periods=1).mean()
df["Standard Deviation"]  = df["close"].rolling(window=w_size, min_periods=1).std()
df["Upper BollingerBand"] = df["Moving Average"] + (df["Standard Deviation"] * pd)
df["Lower BollingerBand"] = df["Moving Average"] - (df["Standard Deviation"] * pd)
df = df.dropna()


plt.style.use('fivethirtyeight')
plt.figure(figsize=(20, 13))
plt.plot(df['close'], lw =1.2)
plt.plot(df['Moving Average'], label='Moving Average', lw=1.2)
plt.plot(df['Upper BollingerBand'], label='Upper Bollinger Band', lw=1.2)
plt.plot(df['Lower BollingerBand'], label='Lower Bollinger Band', lw=1.2)
plt.legend(loc = 'upper left')

i = 0
j = 0
t = len(df)
x1 = 0
x2 = 0
y1 = 0
k = 0
target = 0

for i in range(t-1,x1,-1):
    if (df['Lower BollingerBand'][i] < df['close'][i]) and \
        (df['Lower BollingerBand'][i - 1] > df['close'][i - 1]):
        k = i
        for j in range(k, t - 1):
            if (df['Moving Average'][j - 1] > df['close'][j - 1]) and \
                (df['Moving Average'][j] < df['close'][j]):
                x2 = j
                y2 = df['close'][j]
                if x2 != 0:
                    target = ((y2 - y1)/(x2 - x1))*(199 - x1) + y1
                break
            
plt.show()