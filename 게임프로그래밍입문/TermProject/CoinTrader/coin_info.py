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



class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        w, h = cocos.director.director.get_window_size()
        self.score_text = cocos.text.Label('', font_size=18, color=(50, 50, 255, 255))
        self.score_text.position = (20, h - 40)
        self.add(self.score_text)

    def update_score(self, person, computer):
        self.score_text.element.text = 'You: %s, Computer: %s' % (person, computer)

    def show_game_over(self, winner):
        w, h = cocos.director.director.get_window_size()
        game_over = cocos.text.Label(winner, font_size=50,
                                    anchor_x='center',
                                    anchor_y='center',
                                    color=(50, 50, 255, 255))
        game_over.position = w * 0.5, h * 0.5
        self.add(game_over)

class GameStart(cocos.layer.Layer):
    def __init__(self):
        super(GameStart, self).__init__()
        self.schedule(self.now_money)
        
    # 현재가 가져와서 출력
    def now_money():
        ticker_name = ["KRW-BTC", "kRW-XRP", "kRW-DOGE", "kRW-WEMIX", "kRW-ETH"]
        for i in ticker_name:
            currnet_price = pyupbit.get_current_price(i)

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
        scene.add(GameStart(), z=1)
        scene.add(color_layer, z=0)
        cocos.director.director.push(scene)

    def set_difficulty(self, index):
        self.selDifficulty = index
        
if __name__ == '__main__':
    cocos.director.director.init(caption = 'coin king', width = 75*8, height = 75*8)
    scene = cocos.scene.Scene()
    scene.add(MainMenu())
    cocos.director.director.run(scene)