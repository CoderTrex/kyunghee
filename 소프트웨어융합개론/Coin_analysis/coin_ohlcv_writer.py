from os import access
import readline
from matplotlib import ticker
import pyupbit
import pandas as pd

def get_coin_info():
    the_all_ticker = []
    tickers = pyupbit.get_tickers(fiat="KRW")
    for item in tickers:
        the_all_ticker.append(item)

    # 모든 티커를 엑셀 파일로 저장한다. 저장하는 내용은 4일 동안의 티커의 ohlcv의 값이다.
    for ticker_name in the_all_ticker:
        # dt에 "BTC"에 관련한 코인 정보 ohlcv에 관한 정보를 저장한다.
        dt = pyupbit.get_ohlcv(ticker=ticker_name, interval="day",
                            count=500)  # 1분 봉으로 값을 정렬해서 전해줌
        # df를 데이타 프라임 속성을 부여하여, to_excel 함수를 가질 수 있게 한다.
        dt_da = pd.DataFrame(dt)
        # dt_da의 값을 엑셀로 정리하여 sample.xlsx라는 파일의 이름으로 저장하여 기록한다.
        dt_da.to_excel(
            excel_writer='C:\\Coding\\kyunghee\\소프트웨어융합개론\\File\\coin_ohlcv\\{0}.xlsx'.format(ticker_name))
        
get_coin_info()