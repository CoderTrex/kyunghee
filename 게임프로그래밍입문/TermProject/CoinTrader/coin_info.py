# cocos 툴
import cocos
from cocos.menu import *
import cocos.euclid as eu


from datetime import datetime
from os import access
from matplotlib import ticker

# pyupbit 툴
import pyupbit
from pyupbit.exchange_api import Upbit



# 찾게 되는 코인의 리스트
ticker_name = ["KRW-BTC", "kRW-XRP", "kRW-DOGE", "kRW-WEMIX", "kRW-ETH"]
# 기본 금 (5억)
basic_money = 500000000


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Game')
        self.font_title['font_name'] = 'Times New Roman'
        self.font_title['font_size'] = 60
        self.font_title['bold'] = True
        self.font_item['font_name'] = 'Times New Roman'
        self.font_item_selected['font_name'] = 'Times New Roman'

        self.selDifficulty = 0
        self.difficulty = ['Easy', 'Normal', 'Hard']

        items = list()
        items.append(MenuItem('New Game', self.start_game))
        items.append(MultipleMenuItem('Difficuly: ', self.set_difficulty, self.difficulty, 0))
        items.append(MenuItem('Quit', exit))
        self.create_menu(items, shake(), shake_back())

    def start_game(self):
        scene = cocos.scene.Scene()
        color_layer = cocos.layer.ColorLayer(0, 100, 0, 255)
        hud_layer = HUD()
        scene.add(hud_layer, z=2)
        scene.add(GameLayer(self.selDifficulty, hud_layer), z=1)
        scene.add(color_layer, z=0)
        cocos.director.director.push(scene)

    def set_difficulty(self, index):
        self.selDifficulty = index
# 현재가 가져와서 출력
for i in ticker_name:
    currnet_price = pyupbit.get_current_price(i)
    print("{} : {}".format(i, currnet_price))
    
    
if __name__ == '__main__':
    cocos.director.director.init(caption = 'Coin King', width = 75*100, height = 75 * 100)
    scene = cocos.scene.Scene()
    scene.add(MainMenu())
    cocos.director.director.run(scene)