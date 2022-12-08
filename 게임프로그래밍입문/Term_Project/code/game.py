import pygame
from pygame import mixer
import random
import os
import csv
import button

mixer.init()
pygame.init()

#초기 화면 설정
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('I\'m slimer')

# 게임 프레임 정의
clock = pygame.time.Clock()
FPS = 60

# 게임 변수 설정
GRAVITY = 0.6
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
MAX_LEVEL = 3
TILE_SIZE = SCREEN_HEIGHT//ROWS
TILE_TYPE = 21

MAGIC_TYPE = 1


screen_scroll = 0
bg_scroll = 0
level = 0
start_game = False
start_intro = False



#음악 및 소리 로드
# pygame.mixer.music.load("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\music\\music2.mp3")
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1, 0.0, 5000)
jump_fx = pygame.mixer.Sound("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\music\\jump.wav")
jump_fx.set_volume(0.5)
shoot_fx = pygame.mixer.Sound("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\music\\shot.wav")
shoot_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\music\\grenade.wav")
magic_fx.set_volume(0.5)


# 이미지 로드
# 버튼 이미지
start_img  = pygame.image.load("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\button\\start_btn.png")
exit_img  = pygame.image.load("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\button\\exit_btn.png")
restart_img  = pygame.image.load("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\button\\restart_btn.png")

# 리스트로 타일 저장
img_list = []
for x in range(TILE_TYPE):
    img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\level\\img\\tile\\{0}.png'.format(x))
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)


# 슬라임 총알
bullet_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\attack_bullet.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (bullet_img.get_width() * 0.03, bullet_img.get_height() * 0.03))
skeleton_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\attack_skeleton.png').convert_alpha()
skeleton_img = pygame.transform.scale(skeleton_img, (skeleton_img.get_width() * 0.09, skeleton_img.get_height() * 0.09))

# 마법 이미지
magic_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Magic_slime.png').convert_alpha()
magic_img = pygame.transform.scale(magic_img, (magic_img.get_width() * 0.4, magic_img.get_height() * 0.4))

# 주울 수 있는 아이템
health_box_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\icon\\heal.png').convert_alpha()
health_box_img = pygame.transform.scale(health_box_img, (health_box_img.get_width() * 3, health_box_img.get_height() * 3))
ammo_box_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\icon\\ammo.png').convert_alpha()
ammo_box_img = pygame.transform.scale(ammo_box_img, (ammo_box_img.get_width() * 3, ammo_box_img.get_height() * 3))
power_box_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\icon\\power.png').convert_alpha()
power_box_img = pygame.transform.scale(power_box_img, (power_box_img.get_width() * 3, power_box_img.get_height() * 3))

# 마법 슬라임 생성
slime_ice_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\icon\\skill_water.png').convert_alpha()
slime_ice_img = pygame.transform.scale(slime_ice_img, (slime_ice_img.get_width() * 0.9, slime_ice_img.get_height() * 0.9))
slime_posion_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\icon\\skill_posion.png').convert_alpha()
slime_posion_img = pygame.transform.scale(slime_posion_img, (slime_posion_img.get_width() * 0.9, slime_posion_img.get_height() * 0.9))
slime_fire_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\icon\\skill_fire.png').convert_alpha()
slime_fire_img = pygame.transform.scale(slime_fire_img, (slime_fire_img.get_width() * 0.9, slime_fire_img.get_height() * 0.9))

item_boxes = {
    'Health': health_box_img,
    'Ammo': ammo_box_img,
    'Power': power_box_img,
    'ice' : slime_ice_img,
    'fire' : slime_fire_img,
    'posion' : slime_posion_img
}

# 캐릭터 액션 정의
moving_left = False
moving_right = False
shoot = False
magic = False
spin = False
magic_thrown = False

pine1_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\level\\img\\Background\\pine1.png').convert_alpha()
pine2_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\level\\img\\Background\\pine2.png').convert_alpha()
mountain_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\level\\img\\Background\\mountain.png').convert_alpha()


# 배경 형성
BG = (200, 101, 120)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# 폰트 정의
font = pygame.font.SysFont('Futura', 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# 배경 처리
def draw_bg():
    screen.fill(BG)
    width = mountain_img.get_width()
    for x in range(5):
        screen.blit(mountain_img, ((x * width - bg_scroll) * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * width - bg_scroll) * 0.5 - bg_scroll, SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * width - bg_scroll) * 0.5 - bg_scroll, SCREEN_HEIGHT - pine2_img.get_height()))
    
def reset_level():
    enemy_group.empty()
    bullet_group.empty()
    magic_group.empty()
    explosion_group.empty()
    Item_box_group.empty()
    freeze_group.empty()
    poison_group.empty()
    lava_group.empty()
    star_group.empty()

    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1]  * COLS
        data.append(r)
    
    return data


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, magic):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.magic = magic
        self.magic_type = 1

        
        # 마법 상태
        self.freeze = False
        self.burn = False
        self.posion = False
        
        if (char_type == 'lich'):
            self.health = 300 # 몬스터에 맞춰서 health 구현하기
        if (char_type == "goblin"):
            self.health = 75
        if (char_type == 'player'):
            self.health = 150

        self.max_health = self.health
        self.shoot_cooldown = 0
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        
        self.spin_time = 0
        self.spin = False
        self.in_spin = False
        
        
        self.flip = False
        
        # 애니메이션 인덱스
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
        # ai 변수
        self.move_counter = 0
                                    # 넓이와 높이
        self.vision = pygame.Rect(0, 0, 150, 100)
        self.idling = False
        self.idling_counter = 0
        
        animation_types =['Idle', 'Walk', 'Jump', 'Death', 'Spin']
        for animation in animation_types:
            # 임시 이미지 파일 리스트
            temp_list = []
            # 파일안에 있는 사진 수 세기    
            num_of_frames = len(os.listdir("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\{0}\\{1}"\
                                .format(self.char_type, animation)))
            for i in range (1, num_of_frames + 1):
                # 이미지 가져오기
                img = pygame.image.load("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\{0}\\{1}\\{1}{2}.png"\
                                        .format(self.char_type, animation, i)).convert_alpha()
                # 이미지의 크기 다시 제정의하기
                img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
                # 이미지 리스트에 넣어 두기
                temp_list.append(img)
            self.animation_list.append(temp_list)
        
        # 이미지 변수는 2차원 배열이고 액션 인덱스에 따라서 프레임도 변화함
        self.image = self.animation_list[self.action][self.frame_index]
        #이미지 모양 지정
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        # 애니메이션 업데이트
        self.update_animation()
        self.check_alive()
        # 쿨다운 업데이트
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # 움직임 변수들을 초기화
        screen_scroll = 0
        dx = 0
        dy = 0

        # 왼쪽과 오른쪽으로 움직임을 할당해줌
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -15
            self.jump = False
            self.in_air = True
        
        # 중력 적용
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y 
        dy += self.vel_y
        
        if self.spin == True and self.in_spin == False:
            self.spin_time = -200
            self.spin = False
            self.in_spin = True
        
        if (self.spin_time < 0):
            self.spin_time += 1
        else:
            self.in_spin = False
        
        # 바닥과 충돌 처리
        for tile in world.obstacle_list:
            # x축과의 충돌 처리
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'lich' or self.char_type == 'goblin':
                    self.direction *= -1
                    self.move_counter = 0
            # y축과의 충돌 처리
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # 땅에 맏닿아 있는지 확인
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # 땅 위에 있는 지 확인
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        if pygame.sprite.spritecollide(self, lava_group, False):
            self.health = 0
        level_complete = False
        if pygame.sprite.spritecollide(self, star_group, False):
            level_complete = True
            
        # 맵아래로 빠졌는지 확인
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        if self.char_type == 'player':
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0
            
        # 할당 받은 사각형의 위치를 정해줌
        self.rect.x += dx
        self.rect.y += dy

        # 플레이어의 위치에 기반해 스크롤을 업데이트
        if self.char_type == 'player':
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH \
                and bg_scroll < (world.level_length * TILE_SIZE) - SCREEN_WIDTH) \
                or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
                self.rect.x -= dx
                screen_scroll = -dx 
                
        return screen_scroll, level_complete
        
    # 플레이어의 총알 발사
    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 30
            if self.char_type == 'lich':
                bullet = Bullet(self.rect.centerx + self.direction *(self.rect.size[0] * 1), self.rect.centery, self.direction, self.char_type)
            else:
                bullet = Bullet(self.rect.centerx + self.direction *(self.rect.size[0] * 0.7), self.rect.centery, self.direction, self.char_type)
            bullet_group.add(bullet)
            # 총알 감소
            self.ammo -= 1
            shoot_fx.play()
    
    def ai(self):
        i = 0
        if self.alive and player.alive:
            if self.freeze == True:
                self.update_action(0)
                self.idling = True
            elif (self.idling == False and random.randint(1, 200) == 3):
                self.update_action(0) # 멈춰있는 자세 유지
                self.idling = True
                self.idling_counter = 100
            # ai 근처에 플레이어가 있는 지 확인
            elif self.vision.colliderect(player.rect):
                i += 1
                # 움직이지 않고 플레이어를 바라본다.
                if i % 10 == 9:
                    self.update_action()
                    self.shoot()
                else:
                    self.update_action(0)
                    self.shoot() # 여기서 변주를 주자

            
            else:
                if self.idling == False:
                    if  self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    # 달리기 상태를 유지함
                    self.update_action(1)
                    self.move_counter += 1
                    # ai가 움직이면서 시야가 달라지는 것을 구현
                    self.vision.center = (self.rect.centerx + 150 * self.direction, self.rect.centery)
                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False
        # 스크롤
        self.rect.x += screen_scroll



    def update_animation(self):
        # 애니메이션 업데이트
        ANIMATION_COOLDOWN = 100
        # 현재 프레임에 따라 화면을 업데이트 함
        self.image = self.animation_list[self.action][self.frame_index]
        # 마지막 업데이트 시간 이후로 충분한 시간이 지났는 지 확인
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # 만약 애니메이션이 인덱스를 초과하면 처음으로 돌아감
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # 액션이 일전에 햇던 액션과 같은 지 확인함
        if new_action != self.action:
            self.action = new_action
            # 에니메이션의 세팅을 바꿈
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.rect.x
            self.speed = 0
            self.alive = False
            self.update_action(3)
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        # pygame.draw.rect(screen, RED, self.rect, 1)


class World():
    def __init__(self):
        self.obstacle_list = []
    
    def process_data(self, data):
        self.level_length = len(data[0])
        
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9  and tile <= 10:
                        lava = Lava(img, x*TILE_SIZE, y*TILE_SIZE)
                        lava_group.add(lava)
                    elif tile == 11: # 힐팩 생성
                        Item_box = ItemBox('Health', x*TILE_SIZE, y*TILE_SIZE)
                        Item_box_group.add(Item_box)
                    elif tile == 12: # 마법 팩 형성
                        Item_box = ItemBox('Power', x*TILE_SIZE, y*TILE_SIZE)
                        Item_box_group.add(Item_box)
                    elif tile == 13: # 총알 팩 형성
                        Item_box = ItemBox('Ammo', x*TILE_SIZE, y*TILE_SIZE)
                        Item_box_group.add(Item_box)
                    elif tile == 14:
                        player = Soldier('player', x * TILE_SIZE, y * TILE_SIZE, 2, 5, 20, 5)
                        health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile == 15:
                        enemy = Soldier('lich', x * TILE_SIZE, y * TILE_SIZE, 2, 2, 20, 0)
                        enemy_group.add(enemy)
                    elif tile == 16:
                        enemy2 = Soldier('goblin', x * TILE_SIZE, y * TILE_SIZE, 0.5, 2, 20, 0)
                        enemy_group.add(enemy2)
                    elif tile == 17:
                        Item_box = ItemBox('ice', x * TILE_SIZE, y * TILE_SIZE)
                        Item_box_group.add(Item_box)
                    elif tile == 18:
                        Item_box = ItemBox('fire', x * TILE_SIZE, y * TILE_SIZE)
                        Item_box_group.add(Item_box)
                    elif tile == 19:
                        Item_box = ItemBox('posion', x * TILE_SIZE, y * TILE_SIZE)
                        Item_box_group.add(Item_box)
                    elif tile == 20:
                        star = Star(img, x*TILE_SIZE, y*TILE_SIZE)
                        star_group.add(star)
        return player, health_bar

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])

class Lava(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x  + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
    def update(self):
        self.rect.x += screen_scroll

class Star(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x  + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
    def update(self):
        self.rect.x += screen_scroll

class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
    
    def update(self):
        self.rect.x += screen_scroll
        # 플레이어가 물약을 주웠는지 확인함
        if pygame.sprite.collide_rect(self, player):
            # 어떤 박스와 충돌했는 지 확인함
            if self.item_type == 'Health':
                player.health += 25
                if player.health > player.max_health:
                    # 최대 체력보다 많이 회복되면 체력은 최대체력 자체가 됨
                    player.health = player.max_health
            elif self.item_type == 'Ammo':
                player.ammo += 15
            elif self.item_type == 'Power':
                player.magic += 5
            elif self.item_type == "ice":
                player.magic_type = 1
                player.magic += 5
            elif self.item_type == "fire":
                player.magic_type = 2
                player.magic += 5
            elif self.item_type == "posion":
                player.magic_type = 3
                player.magic += 5
            # 아이템 삭제 
            self.kill()
            

class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
    
    def draw(self, health):
        self.health = health
        
        # calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, char_type):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.bullet_type = 0
        if char_type == "player":
            self.image = bullet_img
            self.bullet_type = 0
        elif char_type == "lich" or char_type == "goblin":
            self.image = skeleton_img
            self.bullet_type = 1
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        
    def update(self):
        # 총알 움직이기
        self.rect.x += (self.direction * self.speed) + screen_scroll
        # 총알이 화면 밖으로 나갔는가 확인하기
        if  self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        
        # 레벨과 충돌 처리
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()
        
        # 캐릭터와 총알 충돌 체크
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                if player.in_spin:
                    pass
                else:
                    player.health -= 5
                self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive and self.bullet_type == 0:
                    enemy.health -= 25
                    self.kill()

class Spin(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, direction):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 13):
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\player\\spin\\Spin{0}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        
    def update(self):
        for enemy in enemy_group:
            if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 1.5 and \
                abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 1.5:
                enemy.health -= 3
        if self.counter <= len(self.images):
            self.counter += 1
            self.image = self.images[self.counter]
        else:
            self.counter = 0
            self.image = self.images[self.counter]

        
class Magic(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, player):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -8
        self.speed = 15
        self.image = magic_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # 레벨과 충돌 처리
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * self.speed
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom
        
        # 마법의 위치 업데이트
        self.rect.x += dx + screen_scroll
        self.rect.y += dy
        
        # 시간 카운트 다운
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            magic_fx.play()
            if player.magic_type== 1:
                explosion = Explosion_Ice(self.rect.x, self.rect.y + 100, 3.0)
            elif player.magic_type == 2:
                explosion = Explosion_Fire(self.rect.x, self.rect.y + 100, 3.0)
            elif player.magic_type == 3:
                explosion = Explosion_Posion(self.rect.x, self.rect.y + 70, 1.0)

            explosion_group.add(explosion)
            # 근처의 누구에게나 데미지 입히기 
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and \
                abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
            for enemy in enemy_group:
                    # 얼음 마법 진행
                    if player.magic_type == 1:
                        if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2.5 and abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2.5:
                            freeze = Freeze(enemy.rect.centerx, enemy.rect.centery, 1, enemy)
                            freeze_group.add(freeze)
                            enemy.health -= 30  
                    # 화염 마법 진행
                    elif player.magic_type == 2:
                        if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 1.5 and abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 1.5:
                            fire = Fire(enemy.rect.centerx, enemy.rect.centery, 0.5, enemy)
                            fire_group.add(fire)
                            enemy.health -= 75
                    # 독 마법 진행
                    elif player.magic_type == 3:
                        if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 3 and abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 3:
                            poison = Poison(enemy.rect.centerx, enemy.rect.centery, 0.5, enemy)
                            poison_group.add(poison)
                            enemy.health -= 20

class Freeze(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, freeze_enemy):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.freeze_enemy = freeze_enemy
        for num in range(1, 8):
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Freeze\\{0}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        
    def update(self):
        self.rect.x += screen_scroll
        Explosion_SPEED = 200
        if self.counter <= Explosion_SPEED:
            self.freeze_enemy.freeze = True
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
                self.counter += 1
            else:
                self.image = self.images[self.frame_index]
        else:
            self.freeze_enemy.freeze = False
            self.kill()

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, fired_enemy):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.fired_enemy = fired_enemy
        for num in range(1, 8):
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Explosion_Fire\\frame{:04d}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        
    def update(self):
        self.rect.x += screen_scroll
        Explosion_SPEED = 200
        if self.counter <= Explosion_SPEED:
            self.fired_enemy.freeze = True
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
                self.counter += 1
            else:
                self.image = self.images[self.frame_index]
        else:
            self.fired_enemy.freeze = False
            self.kill()

class Poison(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, addicted_enemy):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.addicted_enemy = addicted_enemy
        for num in range(1, 10):                                                                            
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Explosion_Posion\\Explosion_gas{0}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        
    def update(self):
        Explosion_SPEED = 10
        self.counter += 1
        if self.counter >= Explosion_SPEED:
            self.addicted_enemy.health -= 2
            self.counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]


class Explosion_Ice(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 73):
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Explosion_Ice\\frame{:04d}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - 100)
        self.counter = 0

    def update(self):
        self.rect.x += screen_scroll
        Explosion_SPEED = 4
        # 폭발 이미지 업데이트
        self.counter += 1
        if self.counter >= Explosion_SPEED:
            self.counter = 0
            self.frame_index += 1
            # 애니메이션이 완성되면 삭제한다.
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]

class Explosion_Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 64):
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Explosion_Fire\\frame{:04d}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - 100)
        self.counter = 0

    def update(self):
        self.rect.x += screen_scroll
        Explosion_SPEED = 4
        # 폭발 이미지 업데이트
        self.counter += 1
        if self.counter >= Explosion_SPEED:
            self.counter = 0
            self.frame_index += 1
            # 애니메이션이 완성되면 삭제한다.
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]

class Explosion_Posion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 10):
            img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\Explosion_Posion\\Explosion_gas{0}.png'.format(num)).convert_alpha()
            img = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - 100)
        self.counter = 0

    def update(self):
        self.rect.x += screen_scroll
        Explosion_SPEED = 4
        # 폭발 이미지 업데이트
        self.counter += 1
        if self.counter >= Explosion_SPEED:
            self.counter = 0
            self.frame_index += 1
            # 애니메이션이 완성되면 삭제한다.
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]

class ScreenFade():
    def __init__(self, direction, color, speed):
        self.direction = direction
        self.color = color
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed

        if self.direction == 1:
            pygame.draw.rect(screen, self.color, (0 - self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.color, (SCREEN_WIDTH // 2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_WIDTH))
            pygame.draw.rect(screen, self.color, (0, 0 - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.color, (0, SCREEN_HEIGHT // 2 + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.direction == 2:
            pygame.draw.rect(screen, self.color, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
        if  self.fade_counter >= SCREEN_WIDTH:
            fade_complete = True
        return fade_complete


intro_fade = ScreenFade(1, BLACK, 4)
death_fade = ScreenFade(2, GREEN, 4)

#버튼 생성
start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1.1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 - 20, exit_img, 1.1)
restart_button = button.Button(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, restart_img, 3)

# 스프라이트 그룹을 생성
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
magic_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
Item_box_group = pygame.sprite.Group()
magic_slime_group = pygame.sprite.Group()


freeze_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
poison_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
star_group = pygame.sprite.Group()

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1]  * COLS
    world_data.append(r)

# load in level data and create world
with open('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\code\\level{}_data.csv'.format(0), newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

world = World()
player, health_bar = world.process_data(world_data)

# 비어있는 파일 리스트를 출력한다.
run = True
while run:
    clock.tick(FPS)
    if (start_game == False):
        screen.fill(BG)
        if start_button.draw(screen):
            start_game = True
            start_intro = True
        if exit_button.draw(screen):
            run = False
        
    else:
        # 배경 출력
        draw_bg()
        # 맵 출력
        world.draw()
        # HP 출력
        health_bar.draw(player.health)
        # 총알 수 출력
        draw_text('AMMO:'.format(player.ammo), font, WHITE, 10, 35)
        for x in range(player.ammo):
            screen.blit(bullet_img, (90 + (x * 10), 40))
        # 마법 수 출력
        draw_text('MAGIC:'.format(player.magic), font, WHITE, 10, 65)
        for x in range(player.magic):
            
            screen.blit(magic_img, (90 + (x * 10), 65))

        # 플레이어 생성
        player.draw()
        player.update()
        player.move(moving_left, moving_right)

        # 적 형성
        for enemy in enemy_group:
            enemy.ai()
            enemy.draw()
            enemy.update()

        # 총알 및 마법 업데이트 및 생성
        bullet_group.update()
        magic_group.update()
        explosion_group.update()
        freeze_group.update()
        fire_group.update()
        poison_group.update()
        
        Item_box_group.update()
        lava_group.update()
        star_group.update()    
        
        bullet_group.draw(screen)
        magic_group.draw(screen)
        explosion_group.draw(screen)
        freeze_group.draw(screen)
        fire_group.draw(screen)
        poison_group.draw(screen)
        Item_box_group.draw(screen)
        lava_group.draw(screen)
        star_group.draw(screen)
        
        if start_intro == True:
            if intro_fade.fade():
                start_intro = False
                intro_fade.fade_counter = 0
        # 플레이어의 액션 상태 업데이트
        if player.alive:
            # 총알 액션 (플레이어의 중심 x, 플레이어 중심 y, 플레이어방향(같은방향))
            if shoot:
                player.shoot()
            # 수류탄 투척 액션
            elif magic and magic_thrown == False and player.magic > 0:
                magic = Magic(player.rect.centerx + (1 * player.rect.size[0]) * player.direction, player.rect.top, player.direction, player)
                magic_group.add(magic)
                # 수류탄 수 줄어들기
                player.magic -= 1
                magic_thrown = True
            # elif spin:
            #     spin = Spin(player.rect.center, player.direction, 1, player.direction)
            if player.in_air:
                player.update_action(2)#2: jump
            elif moving_left or moving_right:
                player.update_action(1)#1: run
            elif player.spin:
                player.update_action(4)
            else:
                player.update_action(0)#0: idle
                
            screen_scroll, level_complete = player.move(moving_left, moving_right)
            bg_scroll -= screen_scroll
            #check if player has completed the level
            if level_complete:
                start_intro = True
                level += 1
                bg_scroll = 0
                world_data = reset_level()
                if level <= MAX_LEVEL:
                    with open('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\code\\level{}_data.csv'.format(0), newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                        world = World() 
                        player, health_bar = world.process_data(world_data)
        else:
            screen_scroll = 0
            if death_fade.fade():
                if restart_button.draw(screen):
                    death_fade.fade_counter = 0
                    start_intro = True
                    bg_scroll = 0
                    world_data = reset_level()
                    with open('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\code\\level{}_data.csv'.format(0), newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)
                    
                
    for event in pygame.event.get():
        # when quit game
        if event.type == pygame.QUIT:
            run = False
    
        # 키보드 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP and player.alive:
                player.jump = True
                jump_fx.play()
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_a:
                magic = True
            if event.key == pygame.K_s and player.alive:
                player.spin = True
            if event.key == pygame.K_ESCAPE:
                run = False
        
        # 키보드 입력 해제
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_s:
                spin == False
            if event.key == pygame.K_a:
                magic = False
                magic_thrown = False
    pygame.display.update()

pygame.quit()