from os import access
import pyupbit
import pybithumb
import time
# import schedule
import pandas as pd
import numpy as np
import openpyxl

# 구매할 코인의 정보를 찾는 작업을 하나로 묶는다.
########################################################################################################################################
first_strategy = {}
second_strategy = {}
the_num = False


def find_ticker(count):
    # 원화로 거래가 가능한 ticker들의 정보를 가져온 뒤에 the_all_ticker에 ticker의 내용을 저장한다.
    the_all_ticker = []
    tickers = pyupbit.get_tickers(fiat="KRW")
    for item in tickers:
        the_all_ticker.append(item)
        
    if count == 1:
        # 1. (1번 전략(기존의 나와있는 전략): RSi 지표를 통한 매수 매도  https://rebro.kr/139
        def rsi(ohlc: pd.DataFrame, period: int = 14):
            delta = ohlc['close'].diff()
            ups, downs = delta.copy(), delta.copy()
            ups[ups < 0] = 0
            downs[downs > 0] = 0

            au = ups.ewm(com=period-1, min_periods=period).mean()
            ad = downs.abs().ewm(com=period - 1, min_periods=period).mean()
            rs = au/ad
            the_result = pd.Series(100 - (100/(1+rs)), name="RSI")
            return the_result
        
        for ticker_name in the_all_ticker:
            data = pyupbit.get_ohlcv(ticker="{0}".format(ticker_name), interval="minute5")
            now_rsi = rsi(data, 14).iloc[-1]
            second_strategy[ticker_name] = now_rsi
            time.sleep(1)

def action(number):
    if number == 1:
        find_ticker(1)
        df = pd.DataFrame(data=second_strategy, index=[0])
        df = (df.T)
        df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\RSI\\RSI.xlsx")

def main():
    action(1)
    # action(2)
    
main()