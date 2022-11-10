from os import access
import readline
from matplotlib import ticker
import pyupbit
import pandas as pd

tickers = pyupbit.get_tickers(fiat="KRW")
# 코인 500일치의 정보 가져오기


def The_find_ticker():
    for ticker_name in tickers:
        ticker_ohlcv = pyupbit.get_ohlcv(
            ticker=ticker_name, interval="day", count=500)
        ticker_dt = pd.DataFrame(ticker_ohlcv)
        ticker_dt.to_excel(
            excel_writer='C:\\Users\\정은성\\Desktop\\coding project\\Python\\StockAndCoin_GameDevelop\\Coin_실전\\Project\\Xlsx_File\\{0}.xlsx'.format(ticker_name))


# 내가 고안한 전략
#: 급락한 코인이 3일 연속으로 하락장이면 시초가보다 5% 넘게 한 번은 상승한다는 것을 노린 전략
def First_strategy():
    for ticker_name in tickers:
        file_root = 'C:\\Users\\정은성\\Desktop\\coding project\\Python\\StockAndCoin_GameDevelop\\Coin_실전\\Project\\Xlsx_File\\{0}.xlsx'.format(
            ticker_name)
        file_excel = pd.read_excel(file_root)
        data_np = pd.DataFrame.to_numpy(file_excel)

        percent_box = []
        for i in range(3):
            data_rate = (data_np[i+496][1]-data_np[i+495][1])/data_np[i+495][1]
            percent_box.append(data_rate)

        target_ticker = []
        if (percent_box[0] <= -0.20):
            if (percent_box[1] <= -0.05):
                if (-0.05 <= percent_box <= 0):
                    target_ticker.append(ticker_name)

        if len(target_ticker) > 0:
            return target_ticker
        else:
            return 0


# 변동성 돌파 전략
def Second_strategy():
    for ticker_name in tickers:
        file_root = 'C:\\Users\\정은성\\Desktop\\coding project\\Python\\StockAndCoin_GameDevelop\\Coin_실전\\Project\\Xlsx_File\\{0}.xlsx'.format(
            ticker_name)
        file_excel = pd.read_excel(file_root)
        data_np = pd.DataFrame.to_numpy(file_excel)

        # 변동성 매매 돌파 전략은 가격의 RSI의 비율이 25%이하인 코인으로 진행한다.
        



        # [가로][세로]
        the_pin_point = (data_np[498][2] - data_np[498][3])*(0.1)
        # 주식의 시초가를 가져오고 12시에 the_pin_point를 더한 값을 넘으면 이를 매수하고 5% 이상 상승시 매도한다.
        while(1):
            pyupbit.get_current_price()

    target_ticker = 0
    return target_ticker


# Second_strategy()

# def Third_strategy():
#     target_ticker = 0
#     return target_ticker


# def The_access_Upbit():
#     Key_file = "C:\\Users\\jsilv\\Desktop\\coding project\\Python\\StockAndCoin_GameDevelop\\Coin_실전\\Project\\Api_Key(Hotspot).txt"
#     file_open = open(Key_file, 'r', encoding="utf-8")
#     line = file_open.readlines()
#     access_key = line[0].strip()
#     secert_key = line[1].strip()
#     file_open.close()

#     upbit = pyupbit.Upbit(access_key, secert_key)
#     return upbit

#  연결 확인 코드
# upbit = The_access_Upbit()
# balance_my = upbit.get_balance("KRW")
# print(balance_my)


# # 구매 매크로
# def The_Buy():
#     upbit = The_access_Upbit()
#     My_balance = upbit.get_balance("KRW")

#     # 1번째 전략을 통해 가져온 ticker의 이름
#     First_ticker = "이것은 처음 전략을 통해 가져온 ticker의 이름입니다."
#     Second_ticker = "이것은 두번째 전략을 통해 가져온 ticker의 이름입니다."
#     Third_ticker = "이것은 세번째 전략을 통해 가져온 ticker의 이름입니다."

#     first_buy = upbit.buy_market_order("First_ticker", My_balance*0.5)
#     first_buy.get()

#     second_buy = upbit.buy_market_order("second_ticker", My_balance*0.3)
#     Third_buy = upbit.buy_market_order("third_ticker", My_balance*0.2)

#     return first_buy, second_buy, Third_buy


# def The_5percent_rule():
#     upbit = The_access_Upbit()
#     one, two, three = The_Buy()
#     if


# def The_sell():
#     upbit = The_access_Upbit()
#     one, two, three = The_Buy()
#     First_sell = upbit.sell_market_order