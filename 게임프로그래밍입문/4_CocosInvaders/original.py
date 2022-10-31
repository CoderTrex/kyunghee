from asyncio import base_tasks
from logging import setLogRecordFactory
from operator import truediv
import random
from collections import defaultdict
import re
from time import sleep
from pyglet.image import load, ImageGrid, Animation
from pyglet.window import key
import cocos.layer
import cocos.sprite
import cocos.collision_model as cm
import cocos.euclid as eu

# 전역 번수로 설정한다. 이는 발사된 총알을 전부다 담는다.
basket_bullet = []

class Actor(cocos.sprite.Sprite):
    def __init__(self, image, x, y):
        super(Actor, self).__init__(image)
        self.position = eu.Vector2(x, y)
        self.cshape = cm.AARectShape(self.position,
                                     self.width * 0.5,
                                     self.height * 0.5)
        self.basket_bullet = []
        
    def move(self, offset):
        self.position += offset
        self.cshape.center += offset

    def update(self, elapsed):
        pass

    def collide(self, other):
        pass
    

class PlayerCannon(Actor, cocos.layer.Layer):
    #static no!
    KEYS_PRESSED = defaultdict(int)

    def __init__(self, x, y):
        super(PlayerCannon, self).__init__('img/cannon.png', x, y)
        self.speed_x = eu.Vector2(200, 0)
        self.speed_y = eu.Vector2(0, 200)

    def update(self, elapsed):
        pressed = PlayerCannon.KEYS_PRESSED
        space_pressed = pressed[key.SPACE] == 1
        if space_pressed and self.Check_position():
            # 추가되는 playershoot를 리스트에 추가해준다.
            basket_bullet.append(PlayerShoot(self.x, self.y + 50))
            self.parent.add(PlayerShoot(self.x, self.y + 50))
        
        #상하 처리
        movement_y = pressed[key.UP] - pressed[key.DOWN]
        h = self.height * 0.5
        if (movement_y != 0 and h <= self.y <= self.parent.height - h):
            self.move(self.speed_y * movement_y * elapsed)
        else:
            if h >= self.y:
                if (movement_y < 0):
                    pass
                else:
                    self.move(self.speed_y * movement_y * elapsed)
            elif self.y >= self.parent.height - h:
                if (movement_y > 0):
                    pass
                else:
                    self.move(self.speed_y * movement_y * elapsed)

        # 좌우 처리
        movement_x = pressed[key.RIGHT] - pressed[key.LEFT]
        w = self.width * 0.5 
        # 움직임이 0이 아니고, 좌우 거리에 어느 정도 거리
        # (왼쪽 끝부터 자신의 x축 거리의 반절거리, 끝보다 자신의 반절보다 약간 짧은 거리)를 두고 범위를 정한다.
        if movement_x != 0 and w <= self.x <= self.parent.width - w:
            self.move(self.speed_x * movement_x * elapsed)
        else:
            # 만약 더 작은 범위에 있다면 
            if w >= self.x:
                # 왼쪽으로 가는 커맨드는 무시한다.
                if (movement_x < 0):
                    pass
                # 그 외의 x축으로의 이동은 실행한다.
                else:
                    self.move(self.speed_x * movement_x * elapsed)
            # 더 큰 범위를 가는 커맨드를 무시한다.
            elif self.x >= self.parent.width - w:
                # 오른쪽으로 가는 커맨드는 무시한다.
                if (movement_x > 0):
                    pass
                # 그 외의 x축으로의 이동은 실행한다.
                else:
                    self.move(self.speed_x * movement_x * elapsed)

    def Check_position(self):
        if (PlayerShoot.INSTANCE is not None):
            # 만약에 playershoot의 위치가 현재 플레이어의 위치보다 높아지면 출력이 됨 -> 자연스러운 연발로 나가는 것이 구현이 됨
            if (PlayerShoot.INSTANCE.position[1] >= self.position[1] + 200):
                return True
            else:
                return False
        else:
            return True

    def collide(self, other):
        other.kill()
        self.kill()

class GameLayer(cocos.layer.Layer):
    # KEYS_PRESSED = defaultdict(int)
    is_event_handler = True

    def on_key_press(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 1

    def on_key_release(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 0
    
    def __init__(self, hud):
        super(GameLayer, self).__init__()
        w, h = cocos.director.director.get_window_size()
        self.hud = hud
        self.width = w
        self.height = h
        self.lives = 3
        self.score = 0
        self.update_score()
        self.create_player()
        self.create_alien_group(100, 300)
        cell = 1.25 * 50
        self.collman = cm.CollisionManagerGrid(0, w, 0, h, cell, cell)
        self.schedule(self.update)

    def create_player(self):
        self.player = PlayerCannon(self.width * 0.5, 50)
        self.add(self.player)
        self.hud.update_lives(self.lives)

    def update_score(self, score=0):
        self.score += score
        self.hud.update_score(self.score)

    def create_alien_group(self, x, y):
        self.alien_group = AlienGroup(x, y)
        for alien in self.alien_group:
            self.add(alien)

    def update(self, dt):
        self.collman.clear()
        for _, node in self.children:
            self.collman.add(node)
            if not self.collman.knows(node):
                self.remove(node)
        
        # basket_bullet 이라는 배열에 총알을 담아 두고 for 문을 돌면서 self.collide()에 넣어서 진행한다.
        # 현재 충돌이 되지 않는 것은 업데이트를 진행해도 처음 발사된 sprite만 충돌 처리를 했기 때문이기에 이런 방식으로 전체를 순환해준다.
        for i in basket_bullet:
            self.collide(i.INSTANCE)

        if self.collide(self.player):
            self.respawn_player()

        for column in self.alien_group.columns:
            shoot = column.shoot()
            if shoot is not None:
                self.add(shoot)

        for _, node in self.children:
            node.update(dt)
    
        self.alien_group.update(dt)
        if random.random() < 0.01:
            self.add(MysteryShip(50, self.height - 50))
        
        
    def collide(self, node):
        if node is not None:
            for other in self.collman.iter_colliding(node):
                node.collide(other)
                return True
        return False
    
    def respawn_player(self):
        self.lives -= 1
        if self.lives < 0:
            self.unschedule(self.update)
            self.hud.show_game_over()
        else:
            self.create_player()

class Alien(Actor):
    def load_animation(imgage):
        seq = ImageGrid(load(imgage), 2, 1)
        return Animation.from_image_sequence(seq, 0.5)
    
    TYPES = {
        '1': (load_animation('C:\\Coding\\github\\kyunghee\\게임프로그래밍입문\\4_CocosInvaders\\img\\alien1.png'), 40),
        '2': (load_animation('C:\\Coding\\github\\kyunghee\\게임프로그래밍입문\\4_CocosInvaders\\img\\alien2.png'), 20),
        '3': (load_animation('C:\\Coding\\github\\kyunghee\\게임프로그래밍입문\\4_CocosInvaders\\img\\alien3.png'), 10)
    }

    def from_type(x, y, alien_type, column):
        animation, score = Alien.TYPES[alien_type]
        return Alien(animation, x, y, score, column)
    
    def __init__(self, img, x, y, score, column=None):
        super(Alien, self).__init__(img, x, y)
        self.score = score
        self.column = column

    def on_exit(self):
        super(Alien, self).on_exit()
        if self.column:
            self.column.remove(self)

class AlienColumn(object):
    def __init__(self, x, y):
        alien_types = enumerate(['3', '3', '2', '2', '1'])
        self.aliens = [Alien.from_type(x, y+i*60, alien, self) 
                        for i, alien in alien_types]

    def should_turn(self, d):
        if len(self.aliens) == 0:
            return False
        alien = self.aliens[0]
        x, width = alien.x, alien.parent.width
        return x >= width - 50 and d == 1 or x <= 50 and d == -1
    
    def remove(self, alien):
        self.aliens.remove(alien)

    def shoot(self):
        if random.random() < 0.001 and len(self.aliens) > 0:
            pos = self.aliens[0].position
            return Shoot(pos[0], pos[1] - 50)
        return None

class AlienGroup(object):
    def __init__(self, x, y):
        self.columns = [AlienColumn(x + i * 60, y)
                        for i in range(10)]
        self.speed = eu.Vector2(10, 0)
        self.direction = 1
        self.elapsed = 0.0
        self.period = 1.0

    def update(self, elapsed):
        self.elapsed += elapsed
        while self.elapsed >= self.period:
            self.elapsed -= self.period
            offset = self.direction * self.speed
            if self.side_reached():
                self.direction *= -1  
                offset = eu.Vector2(0, -10)
            for alien in self:
                alien.move(offset)  

    def side_reached(self):
        return any(map(lambda c: c.should_turn(self.direction), 
                        self.columns))

    def __iter__(self):
        for column in self.columns:
            for alien in column.aliens:
                yield alien

class Shoot(Actor):
    def __init__(self, x, y, img='img/shoot.png'):
        super(Shoot, self).__init__(img, x, y)
        i = random.randrange(-200, 200)
        self.speed = eu.Vector2(i, -400)
    def update(self, elapsed):
        self.move(self.speed * elapsed)

class PlayerShoot(Shoot):
    INSTANCE =  None

    def __init__(self, x, y):
        super(PlayerShoot, self).__init__(x, y, 'img/laser.png')
        self.speed *= -1
        PlayerShoot.INSTANCE = self

    def collide(self, other):
        if isinstance(other, Alien):
            self.parent.update_score(other.score)
            other.kill()
            self.kill()

    def on_exit(self):
        super(PlayerShoot, self).on_exit()
        del basket_bullet[0]
        PlayerShoot.INSTANCE = None

class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        w, h = cocos.director.director.get_window_size()
        self.score_text = cocos.text.Label('', font_size=18)
        self.score_text.position = (20, h - 40)
        self.lives_text = cocos.text.Label('', font_size=18)
        self.lives_text.position = (w - 100, h - 40)
        self.add(self.score_text)
        self.add(self.lives_text)

    def update_score(self, score):
        self.score_text.element.text = 'Score: %s' % score

    def update_lives(self, lives):
        self.lives_text.element.text = 'Lives: %s' % lives

    def show_game_over(self):
        w, h = cocos.director.director.get_window_size()
        game_over = cocos.text.Label('Game Over', font_size=50, anchor_x='center', anchor_y='center')
        game_over.position = w * 0.5, h * 0.5
        self.add(game_over)
    
    def pause(self):
        w, h = cocos.director.director.get_window_size()
        pause = cocos.text.Label('pause', font_size=50, anchor_x='center', anchor_y='center')
        pause.position = w * 0.5, h * 0.5
        self.add(pause)

class MysteryShip(Alien):
    SCORES = [10, 50, 100, 200]

    def __init__(self, x, y):
        score = random.choice(MysteryShip.SCORES)
        super(MysteryShip, self).__init__('img/alien4.png', x, y, 
                                            score)
        self.speed_1 = eu.Vector2(900, 0)
        self.speed_2 = eu.Vector2(0, -900)
        self.speed_3 = eu.Vector2(-900, 0)
        self.speed_4 = eu.Vector2(0, 900)
        
        
    def update(self, elapsed):
        print(self.x)
        if(self.x < self.parent.width - 50 and self.y==600):
            self.move(self.speed_1 * elapsed)
        elif (self.x > self.parent.width - 50 and self.y>130):
            self.move(self.speed_2 * elapsed)
        elif (self.x > 50 and self.y <= 130):
            self.move(self.speed_3 * elapsed)
        else:
            self.move(self.speed_4 * elapsed)
        
        
if __name__ == '__main__':
    cocos.director.director.init(caption='Cocos Invaders', 
                                    width=800, height=650)
    main_scene = cocos.scene.Scene()
    hud_layer = HUD()
    main_scene.add(hud_layer, z=1)
    game_layer = GameLayer(hud_layer)
    main_scene.add(game_layer, z=0)
    cocos.director.director.run(main_scene)
