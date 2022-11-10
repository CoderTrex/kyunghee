from os import access
import pyupbit
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

    # 1. (1번 전략(나만의 전략): 자본금의 50% 분배 예정) 3일 연속 하락 시 오는 약간의 상승을 노리는 전략
    # 모든 티커의 ohlcv의 값을 가져온 뒤에 이들로부터 1일동안의 변동률을 확인한다.
    if count == 1:
        for ticker_name in the_all_ticker:
            file_root = "C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\coin_ohlcv\\{0}.xlsx".format(ticker_name)
            check_box = []
            readed_excel = pd.read_excel(file_root)
            data_np = pd.DataFrame.to_numpy(readed_excel)

            # 데이터의 시초가를 읽어 상승률을 계산한다.
            for k in range(3):
                data_rate = (data_np[k+1][1]-data_np[k][1])/data_np[k][1]
                check_box.append(data_rate)

            # 상승률을 아래의 조건에 집어넣어 원하는 코인의 이름을 불어들인다.
            # 확인하는 3일전 종가는 25퍼에서 10이상으로 떨어져아한다.
            if (-0.25 <= check_box[0] < -0.1):
                # 만약 떨어졌다면 둘째날도 3퍼센트 이상 떨어져야 한다.
                if (check_box[1] < -0.03):
                    # 마지막날도 떨어져야하지만, 너무 많이 떨어지면 안된다. 기준치인 5퍼에서 1퍼센트가 떨어진 코인을 찾는다.
                    if (-0.05 < check_box[2] < -0.01):
                        first_strategy[ticker_name] = check_box

    elif count == 2:
        # 2. (2번 전략(기존의 나와있는 전략): RSi 지표를 통한 매수 매도  https://rebro.kr/139
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
        df = pd.DataFrame(data=first_strategy, index=[0])
        df = (df.T)
        df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\M_strategy\\file.xlsx")
    if number == 2:
        find_ticker(2)
        df = pd.DataFrame(data=second_strategy, index=[0])
        df = (df.T)
        df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\RSI\\RSI.xlsx")


def main():
    action(2)