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


def M_strategy(count):
    # 원화로 거래가 가능한 ticker들의 정보를 가져온 뒤에 the_all_ticker에 ticker의 내용을 저장한다.
    the_all_ticker = []
    tickers = pyupbit.get_tickers(fiat="KRW")
    for item in tickers:
        the_all_ticker.append(item)

    # 1. (1번 전략(나만의 전략): 자본금의 50% 분배 예정) 3일 연속 하락 시 오는 약간의 상승을 노리는 전략
    # 모든 티커의 ohlcv의 값을 가져온 뒤에 이들로부터 1일동안의 변동률을 확인한다.
    if count == 1:
        for ticker_name in the_all_ticker:
            file_root = "C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\all_info\\all_info_{0}.xlsx".format(ticker_name)
            readed_excel = pd.read_excel(file_root)
            data_np = pd.DataFrame.to_numpy(readed_excel)

            len_np = len(data_np)

            for i in range(len_np - 3):
                if -25 <= data_np[i][7] <= -10:
                    if  data_np[i + 1][7] <= -5:
                        if -3 <= data_np[i + 2][7] <= -1:
                            first_strategy["{0}:  {1}".format(ticker_name, data_np[i + 3][0])] = data_np[i + 3][7]
    # 2. 2번 전략  
    
def action():
    M_strategy(1)
    df = pd.DataFrame(data=first_strategy, index=[1])
    df = (df.T)
    df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\M_strategy\\M_Strategy.xlsx")

action()