# cocos 툴
import cocos
from cocos.menu import *
import cocos.euclid as eu


class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        w, h = cocos.director.director.get_window_size()
        
        self.market_value = cocos.text.Label('', font_size=18, color=(50,50,255,255))
        self.holding_money = cocos.text.Label('', font_size=18, color=(50,50,255,255))
        
        self.market_value.position = (20, h-40)
        self.holding_money.position = (20, h-40)
        
        self.add(self.market_value)
        self.add(self.holding_money)
    
    def update_capital(self, stock_value, hand_money):
        self.market_value.element.text = "Market Value : %s" % (stock_value)
        self.holding_money.element.text = "Market Value : %s" % (hand_money)


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Game')
        self.font_title['font_name'] = 'Times New Roman'
        self.font_title['font_size'] = 60
        self.font_title['bold'] = True
        self.font_item['font_name'] = 'Times New Roman'
        self.font_item_selected['font_name'] = 'Times New Roman'

        self.selDifficulty = 0

        items = list()
        items.append(MenuItem('New Game', self.start_game))
        items.append(MenuItem('Load Game', self.Load_game))
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

    def Load_game(self):
        pass

    def set_difficulty(self, index):
        self.selDifficulty = index
    
if __name__ == '__main__':
    cocos.director.director.init(caption = 'Coin King', width = 75*12, height = 75 * 12)
    scene = cocos.scene.Scene()
    scene.add(MainMenu())
    cocos.director.director.run(scene)