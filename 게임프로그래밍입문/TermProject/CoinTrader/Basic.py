from datetime import datetime
from os import access
from matplotlib import ticker
import pyupbit
# import schedule
import datetime
import time
import pandas as pd
import numpy as np
from pyupbit.exchange_api import Upbit

# 구매할 코인의 정보를 찾는 작업을 하나로 묶는다.
########################################################################################################################################
the_box = []
the_num = False


def find_ticker():
    # 원화로 거래가 가능한 ticker들의 정보를 가져온 뒤에 the_all_ticker에 ticker의 내용을 저장한다.
    the_all_ticker = []
    tickers = pyupbit.get_tickers(fiat="KRW")
    for item in tickers:
        the_all_ticker.append(item)

    # 모든 티커를 엑셀 파일로 저장한다. 저장하는 내용은 4일 동안의 티커의 ohlcv의 값이다.
    for ticker_name in the_all_ticker:
        # dt에 "BTC"에 관련한 코인 정보 ohlcv에 관한 정보를 저장한다.
        dt = pyupbit.get_ohlcv(ticker=ticker_name, interval="day",
                               count=4)  # 1분 봉으로 값을 정렬해서 전해줌
        # df를 데이타 프라임 속성을 부여하여, to_excel 함수를 가질 수 있게 한다.
        dt_da = pd.DataFrame(dt)
        # dt_da의 값을 엑셀로 정리하여 sample.xlsx라는 파일의 이름으로 저장하여 기록한다.
        dt_da.to_excel(
            excel_writer='파이썬\\StockAndCoin_GameDevelop\\실전\\Project\\Xlsx_File\\{0}.xlsx'.format(ticker_name))

    # 1. (1번 전략(나만의 전략): 자본금의 50% 분배 예정) 3일 연속 하락 시 오는 약간의 상승을 노리는 전략
    # 모든 티커의 ohlcv의 값을 가져온 뒤에 이들로부터 1일동안의 변동률을 확인한다.

    def first_strategy():
        for ticker_name in the_all_ticker:
            file_root = "파이썬\\StockAndCoin_GameDevelop\\실전\\Project\\Xlsx_File\\{0}.xlsx".format(
                ticker_name)
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
                        the_box.append(ticker_name)
            return the_box

        # 2. (2번 전략(기존의 나와있는 전략): RSi 지표를 통한 매수 매도  https://rebro.kr/139
        def second_strategy():
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

            while True:
                data = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute5")
                now_rsi = rsi(data, 14).iloc[-1]
                time.sleep(1)


# 파이썬 시간 정해서 함수 실행
#  11:00에 find_ticker 함수를 실행한다.
# schedule.every().day.at("11:00").do(find_ticker)
# while True:
#     schedule.run_pending()
#     time.sleep(60)
########################################################################################################################################
# 박스 안에 들어가 있는 수의 우선순위를 정하기 위해서 진행하는 작업
for the_coin in the_box:
    file_root = "파이썬\\StockAndCoin_GameDevelop\\실전\\Project\\Xlsx_File\\{0}.xlsx".format(
        the_coin)
    check_box = {}
    readed_excel = pd.read_excel(file_root)
    data_np = pd.DataFrame.to_numpy(readed_excel)
    data_rate = (data_np[3][1]-data_np[2][1])/data_np[2][1]
    check_box[the_coin].append(data_rate)

find_ticker()

###########################################################################################################################################
check_box = []

for the_coin in the_box:
    file_root = "파이썬\\StockAndCoin_GameDevelop\\실전\\Project\\Xlsx_File\\{0}.xlsx".format(the_coin)
    readed_excel = pd.read_excel(file_root)
    data_np = pd.DataFrame.to_numpy(readed_excel)
    data_rate = (data_np[3][1]-data_np[2][1])/data_np[2][1]
    check_box[the_coin] = data_rate

for key_value in check_box:
    print(check_box)

# 매수를 진행할 코인의 정보를 정한 후 매수 프로그램을 진행함.
# 매수를 진행한 코인을 시가에 사서 5%가 오른다면, 이를 매도하는 방식으로 진행함.

# # upbit 시장 접근 허용 객체 형성
# key_path = "C:\\Users\\jsilv\\Desktop\\coding project\\파이썬\\StockAndCoin_GameDevelop\\실전\\Api_Key.txt"

# f = open(key_path, 'r', encoding='utf-8')
# line = f.readlines()
# access_key = line[0].strip()
# secert_key = line[1].strip()
# f.close()

# upbit = pyupbit.Upbit(access_key, secert_key)
# # the_box안에 들어가는 ticker의 수가 여러 개일 수도 있으므로 ticker의 구매의 우선 수위를 정해야한다.

# for coin_name in the_box:
#     upbit.buy_market_order(coin_name, 100)