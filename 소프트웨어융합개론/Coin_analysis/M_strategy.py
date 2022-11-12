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

    # 1. (1번 전략(나만의 전략): 자본금의 50% 분배 예정) 3일 연속 하락 시 오는 약간의 상승을 노리는 전략
    # 모든 티커의 ohlcv의 값을 가져온 뒤에 이들로부터 1일동안의 변동률을 확인한다.
    if count == 1:
        for ticker_name in the_all_ticker:
            file_root = "C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\coin_ohlcv\\{0}.xlsx".format(ticker_name)
            check_box = []
            readed_excel = pd.read_excel(file_root)
            data_np = pd.DataFrame.to_numpy(readed_excel)

            len_np = len(data_np)
            
            for i in range(len_np - 1):
                day_rate = (data_np[i + 1][1] - data_np[i][1]) / data_np[i][1]
                check_box.append(day_rate)
            
            for i in range(len_np - 3):
                if (-0.25 <= check_box[i] < -0.1):
                    if (check_box[i + 1] < -0.03):
                        if (-0.05 < check_box[i + 2] < -0.01):
                            first_strategy["{0}:  {1}".format(ticker_name, data_np[i + 2][0])] = check_box[i + 3]

def action(number):
    if number == 1:
        find_ticker(1)
        df = pd.DataFrame(data=first_strategy, index=[1])
        df = (df.T)
        df.to_excel("C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\M_strategy\\file.xlsx")

def main():
    action(1)
    # action(2)
    
main()