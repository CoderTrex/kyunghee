from cocos.director import director

import pyglet.font
import pyglet.resource

from mainmenu import new_menu
if __name__ == '__main__':
    pyglet.resource.path.append('assets')
    pyglet.resource.reindex()
    
    pyglet.font.add_file('게임프로그래밍입문\\5_towerDefends\실습코드\\towerdefense\\assets\\Oswald-Regular.ttf')

    director.init(caption='Tower Defense')
    director.run(new_menu())
