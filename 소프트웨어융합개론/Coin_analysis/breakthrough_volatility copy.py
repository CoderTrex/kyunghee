import pybithumb
import numpy as np

ticker_all_name = pybithumb.get_tickers("kRW")

for ticker_name  in ticker_all_name:
    df = pybithumb.get_ohlcv(str(ticker_name))
    df['range'] = (df['high'] - df['low']) * 0.5
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],df['close'] / df['target'] - fee, 1)

    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    print("MDD:", df['dd'].max())
    df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\Breakthrough\\breakthrough_{0}.xlsx".format(str(ticker_name)))