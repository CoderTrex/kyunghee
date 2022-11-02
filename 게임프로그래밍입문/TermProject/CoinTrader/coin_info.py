# cocos 툴
import cocos
from cocos.menu import *
import cocos.euclid as eu

# pyupbit 툴
import pyupbit
from pyupbit.exchange_api import Upbit

# 기타 작업을 위한 툴
import schedule
import time
from datetime import datetime
from os import access
from matplotlib import ticker







# 찾게 되는 코인의 리스트
# 기본 금 (5억)
basic_money = 500000000

def print_check():
    print("hello")

# 현재가 가져와서 출력
def now_money():
    ticker_name = ["KRW-BTC", "kRW-XRP", "kRW-DOGE", "kRW-WEMIX", "kRW-ETH"]
    for i in ticker_name:
        currnet_price = pyupbit.get_current_price(i)

# schedule.every(3).seconds.do(print_check)
schedule.every(1).seconds.do(now_money)
# now_money()
# print_check()

while (True):
    schedule.run_pending()