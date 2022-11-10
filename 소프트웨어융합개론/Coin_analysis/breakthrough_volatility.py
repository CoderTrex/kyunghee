import pyupbit
import numpy as np
import pandas as pd
from os import access
import readline


breakthrough_df  = pd.DataFrame({'coin':[],'i':[],'ror':[]})
all_ticker = []
tickers = pyupbit.get_tickers(fiat='KRW')
for item in tickers:
    all_ticker.append(item)



for ticker_name in all_ticker:
    for i in range(0, 9, 1):
        i = i / 10.0
        df = pyupbit.get_ohlcv(ticker=ticker_name, interval="day",count=5)  # 1분 봉으로 값을 정렬해서 전해줌
        df['range'] = (df['high'] - df['low']) * i
        df['target'] = df['open'] + df['range'].shift(1)


        fee = 0.0032
        df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

        ror = df['ror'].cumprod()[-2]
        print("{2}/{0}:  {1}".format(i, ror,ticker_name))
        # d = [{'coin':ticker_name, 'i': i, 'ror': ror}]
        
        # breakthrough_df  = breakthrough_df.append(d, ignore_index = True, sort=False)


# for i in range(0, 9, 1):
#     i = i / 10.0
#     df = pyupbit.get_ohlcv(ticker="KRW-XRP", interval="day",count=10)  # 1분 봉으로 값을 정렬해서 전해줌
#     df['range'] = (df['high'] - df['low']) * i
#     df['target'] = df['open'] + df['range'].shift(1)


#     fee = 0.0032
#     df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

#     ror = df['ror'].cumprod()[-2]
#     print("{2}/{0}:  {1}".format(i, ror, "KRW-XRP"))

# breakthrough_df.to_excel("hello.xlsx")