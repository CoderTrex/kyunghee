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


# 초기 자본금 / 평가 금액 / 가지고 있는 코인의 이름과 금액
have_Money = 500000000
have_coin = {1:0, 2:0, 3:0, 4:0, 5:0} # 코인 넘버 : 코인 개수
Valuation_coin = 0


# 구매 가능한 코인의 목록
ticker_name = ["KRW-BTC", "kRW-XRP", "kRW-DOGE", "kRW-WEMIX", "kRW-ETH"]

def current_coin_prince():
    for i  in ticker_name:
        print("{} : {}".format(i, pyupbit.get_current_price(i)))

while(True):
    # 현재 보유하고 있는 코인의 양을 출력함   
    # 가지고 있는 코인의 이름과 개수를 출력함
    for name, count in have_coin:    
        coin_current_price = pyupbit.get_current_price(ticker_name[name])
        # 코인 평가 금액 +=  
        Valuation_coin += coin_current_price * count 
        print("coin:{0}\nprice:{1}".format(ticker_name[name], Valuation_coin))
        
    print("Valuation amount : {}".format(Valuation_coin + have_Money))
    print("hand money       : {}".format(have_Money))
    print ("\n\n")
    print("Enter the number to be done\n")
    print("1. buy\t2. sell\t3. infomation\t 4. Balance Check")
    behavior = int(input())

    # 구매 작업
    if (behavior == 1):
        while (True):
            # 구매할 코인의 이름을 불러옴
            buy_ticker_num = int(input("write number what you want buy\n \
1. KRW-BTC, 2. kRW-XRP, 3. kRW-DOGE, 4. kRW-WEMIX, 5. kRW-ETH, 6. quit\n"))
            # 잘못된 입력
            if not (buy_ticker_num < 6 and buy_ticker_num > 0):
                break
            
            # 구매 코인에 대한 
            purchase_amount = int(input("write amount purchase coin\n"))
            if (purchase_amount > have_Money):
                print("You entered an amount greater than your holding amount")
                break
            else:
                purchase_coin_price = pyupbit.get_current_price(ticker_name[buy_ticker_num])
                number_coin = purchase_coin_price / purchase_amount
                have_coin.append((buy_ticker_num, number_coin))
                have_Money -= purchase_amount
                break
            
    
    # 현재가 가져와서 출력
    # def now_money():
    #     for i in ticker_name:
    #         currnet_price = pyupbit.get_current_price(i)