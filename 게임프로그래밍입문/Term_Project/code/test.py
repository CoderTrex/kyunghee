import pygame
import os

pygame.init()

#초기 화면 설정
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Legend of past')

# 게임 프레임 정의
clock = pygame.time.Clock()
FPS = 60

# 게임 변수 설정
GRAVITY = 0.98

# 이미지 로드
# bullet_slime
bullet_img = pygame.image.load('C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\effect\\attack_bullet.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (bullet_img.get_width() * 0.03, bullet_img.get_height() * 0.03))

# 캐릭터 액션 정의
moving_left = False
moving_right = False
shoot = False

# 배경 형성
BG = (144, 201, 120)
RED = (255, 0, 0)

# 배경 처리
def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))



class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.health = 100 # 몬스터에 맞춰서 health 구현하기
        self.max_health = self.health
        self.shoot_cooldown = 0
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        
        # 애니메이션 인덱스
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
        animation_types =['Idle', 'Walk', 'Jump', 'Death']
        for animation in animation_types:
            # 임시 이미지 파일 리스트
            temp_list = []
            # 파일안에 있는 사진 수 세기    
            num_of_frames = len(os.listdir("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\{0}\\{1}"\
                                .format(self.char_type, animation)))
            for i in range (1, num_of_frames + 1):
                # 이미지 가져오기
                img = pygame.image.load("C:\\Coding\\kyunghee\\게임프로그래밍입문\\Term_Project\\asset\\{0}\\{1}\\{1}0{2}.png"\
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
    
    def update(self):
        # 애니메이션 업데이트
        self.update_animation()
        self.check_alive()
        # 쿨다운 업데이트
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1



    def move(self, moving_left, moving_right):
        # 움직임 변수들을 초기화
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
            self.vel_y = -20
            self.jump = False
            self.in_air = True

        # 중력 적용
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y 
        dy += self.vel_y

        # 바닥과 충돌 처리
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        # 할당 받은 사각형의 위치를 정해줌
        self.rect.x += dx
        self.rect.y += dy


    # 플레이어의 총알 발사
    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 30
            bullet = Bullet(self.rect.centerx + self.direction *(self.rect.size[0] *0.6), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            # 총알 감소
            self.ammo -= 1

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
            self.speed = 0
            self.alive = False
            self.update_action(3)
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        
    def update(self):
        # 총알 움직이기
        self.rect.x += (self.direction * self.speed)
        # 총알이 화면 밖으로 나갔는가 확인하기
        if  self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        #check collision with characters
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()
        if pygame.sprite.spritecollide(enemy, bullet_group, False):
            if enemy.alive:
                enemy.health -= 25
                self.kill()



#create sprite groups
bullet_group = pygame.sprite.Group()



player = Soldier('player', 200, 200, 3, 5, 20)
enemy = Soldier('player', 400, 200, 3, 5, 20)



run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.update()
    player.draw()

    enemy.update()
    enemy.draw()

    #update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)


    #update player actions
    if player.alive:
        #shoot bullets
        if shoot:
            player.shoot()
        if player.in_air:
            player.update_action(2)#2: jump
        elif moving_left or moving_right:
            player.update_action(1)#1: run
        else:
            player.update_action(0)#0: idle
        player.move(moving_left, moving_right)


    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False


        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False




    pygame.display.update()

pygame.quit()