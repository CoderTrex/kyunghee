# cocos 툴
import cocos
from cocos.menu import *
import cocos.euclid as eu

# pyupbit 툴
import pyupbit
from pyupbit.exchange_api import Upbit

# 기타 작업을 위한 툴
import time
from datetime import datetime
from os import access
from matplotlib import ticker


# 초기 자본금 / 평가 금액 / 가지고 있는 코인의 이름과 금액
have_Money = 500000000
have_coin = {'1':0, '2':0, '3':0, '4':0, '5':0} # 코인 넘버 : 코인 개수

# 코인 인덱스 : [코인의 개수, 코인의 구매 단가]
have_coin_info = {'1':[0,0], '2':[0,0], '3':[0,0], '4':[0,0], '5':[0,0]} 


# 구매 가능한 코인의 목록
ticker_name = ["Blank", "KRW-BTC", "kRW-XRP", "kRW-DOGE", "kRW-WEMIX", "kRW-ETH"]
Valuation_coin = 0



def coin_list():
    for name, count in have_coin.items(): 
        Val = 0
        coin_current_price = pyupbit.get_current_price(ticker_name[int(name)])
        Val += coin_current_price * count
        print("{0}: price:{1}, count:{2}, total:{3}".format(ticker_name[int(name)],coin_current_price,count,Val))
    print()

def check_coin_price():
    Val = 0
    for name, count in have_coin.items(): 
        coin_current_price = pyupbit.get_current_price(ticker_name[int(name)])
        Val += coin_current_price * count
    return Val

def call_buy(buy_amount, coin_index):
    global have_Money
    purchase_coin_price = pyupbit.get_current_price(ticker_name[coin_index])
    add_coin = buy_amount / purchase_coin_price
    exist_coin = have_coin.get(str(coin_index))
    have_coin.update({str(coin_index): add_coin + exist_coin})
    have_Money -= (buy_amount)
    
def call_sell(sell_amount, coin_index, coin_in_bank):
    global have_Money
    sell_coin_price = pyupbit.get_current_price(ticker_name[coin_index])
    have_coin.update({str(coin_index) : coin_in_bank - sell_amount})
    have_Money += sell_amount * sell_coin_price


def main():
    while(True):
        global have_Money
        # 현재 보유하고 있는 코인의 양을 출력함   
        # 가지고 있는 코인의 이름과 개수를 출력함
        Valuation_coin = float(check_coin_price())
        print("Valuation amount : {}".format(Valuation_coin + have_Money))
        print("hand money       : {}".format(have_Money))
        print ("\n\n")
        print("Enter the number to be done\n")
        print("1. buy  2. sell  3. investment analysis  4. Balance Check  5. Clear Page")
        behavior = int(input())

# --------------------------------------------------------------------------------------------------------------------------------------------- #
        # 구매 작업
        if (behavior == 1):
            while (True):
                # 구매할 코인의 이름을 불러옴
                buy_ticker_num = int(input("write number what you want buy\n1. KRW-BTC, 2. kRW-XRP, 3. kRW-DOGE, 4. kRW-WEMIX, 5. kRW-ETH, 6. quit\n"))
                # 잘못된 입력
                if not (buy_ticker_num < 6 and buy_ticker_num > 0):
                    break
                buy_method = float(input("input num method of buying your coin\n1. Directly input, 2. 10%, 3. 25%, 4. 50%, 5.100%\n"))
                
                if (buy_method == 1):
                    # 구매 코인에 대한 
                    purchase_amount = int(input("write amount purchase coin\n"))
                    if (purchase_amount > have_Money):
                        print("You entered an amount greater than your holding amount")
                        break
                    else:
                        purchase_coin_price = pyupbit.get_current_price(ticker_name[buy_ticker_num])
                        # 구매코인의 개수 = 구매하려는 금액 / 구매 코인의 가격
                        add_coin = purchase_amount / purchase_coin_price
                        exist_coin = have_coin.get(str(buy_ticker_num))
                        have_coin.update({str(buy_ticker_num): add_coin + exist_coin})
                        have_Money -= (purchase_amount)
                        break
                elif (buy_method == 2):
                    purchase_amount = have_Money/10
                    call_buy(purchase_amount, buy_ticker_num)
                    break
                elif (buy_method == 3):
                    purchase_amount = have_Money/2.5
                    call_buy(purchase_amount, buy_ticker_num)
                    break
                elif (buy_method == 4):
                    purchase_amount = have_Money/2
                    call_buy(purchase_amount, buy_ticker_num)
                    break
                elif (buy_method == 5):
                    purchase_amount = have_Money/1.0
                    call_buy(purchase_amount, buy_ticker_num)
                    break
                else:
                    break

# --------------------------------------------------------------------------------------------------------------------------------------------- #
        # 판매
        if (behavior == 2):
            while (True):
                coin_list()
                sell_ticker_num = int(input("write number what you want sell\n1. KRW-BTC, 2. kRW-XRP, 3. kRW-DOGE, 4. kRW-WEMIX, 5. kRW-ETH, 6. quit\n"))
                if not (sell_ticker_num < 6 and sell_ticker_num > 0):
                    break
                
                coin_amount = have_coin.get(str(sell_ticker_num))
                print("you have a coin : {0}".format(coin_amount))
                # 구매 코인에 대한 
                sell_method = float(input("input num method of selling your coin\n1. Directly input, 2. 10%, 3. 25%, 4. 50%, 5.100%\n"))
                
                if (sell_method == 1):
                    sell_amount = int(input("write amount purchase coin\n"))
                    if (sell_amount > coin_amount):
                        print("You entered an amount greater than your holding amount")
                        break
                    else:
                        sell_coin_price = pyupbit.get_current_price(ticker_name[sell_ticker_num])
                        have_coin.update({str(sell_ticker_num) : coin_amount - sell_amount})
                        have_Money += sell_amount * sell_coin_price
                        break
                elif (sell_method == 2):
                    call_sell(coin_amount/10.0, sell_ticker_num, coin_amount)
                    break
                elif (sell_method == 3):
                    call_sell(coin_amount/4.0, sell_ticker_num, coin_amount)
                    break
                elif (sell_method == 4):
                    call_sell(coin_amount/2.0, sell_ticker_num, coin_amount)
                    break
                elif (sell_method == 5):
                    call_sell(coin_amount/1.0, sell_ticker_num, coin_amount)
                    break
                else:
                    break

# --------------------------------------------------------------------------------------------------------------------------------------------- #
        if (behavior == 3):
            pass

        if (behavior == 4):
            coin_list()

        if (behavior == 5):
            for i in range(50):
                print()

main()