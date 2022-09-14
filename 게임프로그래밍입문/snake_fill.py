# -*- coding: utf8 -*-
from __future__ import print_function
from email import header
import random
import os
import re
from tabnanny import check
import time
import msvcrt

class Snake:
    def __init__(self, n):
        self.length = n
        self.head = []
        self.tail = []

class SnakeGame:
    direction = {"LEFT":-2, "DOWN":-1, "NON_DIR":0, "UP":1, "RIGHT":2}
    sprite = {"EMPTY":0, "BODY":1, "HEAD":2, "FOOD":3}
    element = {"SPRITE":0, "DIRECTION":1}
    
    def __init__(self, w, h, length, delay, level):
        self.W = w
        self.H = h
        self.initLen = length
        self.snake = Snake(length)
        self.delay = delay  
        self.board = [[[0]*2 for x in range(self.W)] for y in range(self.H)]
        self.level = level
        #self.board[a][b][c]

        #세로 / 가로 
        self.snake.head = [self.H//2, self.snake.length-1]
        self.snake.tail = [self.H//2, 0]

        for i in range(0, self.snake.length):
            self.board[self.H//2][i][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
            self.board[self.H//2][i][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["RIGHT"]

        self.board[self.H//2][self.snake.length-1][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
        self.board[self.H//2][self.snake.length-1][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["RIGHT"]

        x = random.randint(0, self.W-1)
        y = random.randint(0, self.H-1)

        while self.board[y][x][SnakeGame.element["SPRITE"]] != SnakeGame.sprite["EMPTY"]:
            x = random.randint(0, self.W-1)
            y = random.randint(0, self.H-1)

        self.board[y][x][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["FOOD"]



    def DrawScene(self):
        os.system('cls||clear')
        
        for x in range(0, self.W+2):
            print("=", end="")
        print("")
        
        for y in range(0, self.H):
            print("|", end="")
            for x in range(0, self.W):
                if self.board[y][x][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["BODY"]:
                    print("+", end="")
                elif  self.board[y][x][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["HEAD"]:
                    print("@", end="")
                elif  self.board[y][x][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("|")

        for x in range(0, self.W+2):
            print("=", end="")
        print("")
                

    @staticmethod
    def GetDirection():
        rtn = SnakeGame.direction["NON_DIR"]
        msvcrt.getch()
        ch = msvcrt.getch().decode()
        
        if ch == chr(72):
            print("UP")
            rtn = SnakeGame.direction["UP"]
        elif ch == chr(75):
            print("LEFT")
            rtn = SnakeGame.direction["LEFT"]
        elif ch == chr(77):
            print("RIGHT")
            rtn = SnakeGame.direction["RIGHT"]
        elif ch == chr(80):
            print("DOWN")
            rtn = SnakeGame.direction["DOWN"]
        return rtn

    def did_eat(self):
        x = random.randint(0, self.W-1)
        y = random.randint(0, self.H-1)

        while (self.board[y][x][SnakeGame.element["SPRITE"]] != SnakeGame.sprite["EMPTY"]):
            x = random.randint(0, self.W-1)
            y = random.randint(0, self.H-1)

        self.board[y][x][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["FOOD"]
    
    def didnt_eat(self):
        self.board[self.snake.tail[0]][self.snake.tail[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["EMPTY"]
        
        direction = self.board[self.snake.tail[0]][self.snake.tail[1]][SnakeGame.element["DIRECTION"]]
        self.board[self.snake.tail[0]][self.snake.tail[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["NON_DIR"]
        if (direction == 1) :
            self.snake.tail[0] -= 1
        elif (direction == -1) :
            self.snake.tail[0] += 1
        elif (direction == 2) :
            self.snake.tail[1] += 1
        elif (direction == -2) :
            self.snake.tail[1] -= 1
        
    
    def check_crash(self):
        if (self.snake.head[0] < 0 or self.snake.head[0] >= self.H or self.snake.head[1] < 0 or self.snake.head[1] >= self.W):
            print("Game Over")
            exit()
        if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["BODY"]):
            print("Game Over")
            exit()
    
    def GameLoop(self):
        self.DrawScene()

        ret = SnakeGame.direction["RIGHT"]
        current = SnakeGame.direction["RIGHT"]
        
        while True:
            start = time.time()
            
            while ((time.time() - start) <= self.delay/10000):
                if msvcrt.kbhit():
                    current = SnakeGame.GetDirection()

                if ((ret == current) or (ret == (current * -1))):
                    current = ret
                
                self.check_crash()
                #헤드 변환 지정
                if (current == 1):
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["UP"]
                    self.snake.head[0] -= 1
                    self.check_crash()
                    # 음식을 먹었는지 여부 확인 
                    # 1. 음식을 먹었으면 길이가 길어짐 
                    # 2. 음식을 먹지 않으면 전 단계의 꼬리의 물체는 빈 공간으로 채워야한다.
                    if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]):
                        self.snake.length += 1
                        self.did_eat()
                    else:
                        self.didnt_eat()

                    #새로 바뀐 헤드 위치에 대해서 보드값 변환
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["UP"]
                    

                elif (current == -1):
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["DOWN"]
                    self.snake.head[0] += 1
                    self.check_crash()
                    
                    if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]):
                        self.snake.length += 1
                        self.did_eat()
                    else:
                        self.didnt_eat()
                    
                    #새로 바뀐 헤드 위치에 대해서 보드값 변환
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["DOWN"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
                
                
                elif (current == 2):
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["RIGHT"]
                    self.snake.head[1] += 1
                    self.check_crash()
                    
                    if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]):
                        self.snake.length += 1
                        self.did_eat()
                    else:
                        self.didnt_eat()
                    
                    #새로 바뀐 헤드 위치에 대해서 보드값 변환
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["RIGHT"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
                    
                
                elif (current == -2):
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["BODY"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["LEFT"]
                    self.snake.head[1] -= 1
                    self.check_crash()
                    
                    if (self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]):
                        self.snake.length += 1
                        self.did_eat()
                    else:
                        self.didnt_eat()
                    
                    #새로 바뀐 헤드 위치에 대해서 보드값 변환
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["LEFT"]
                    self.board[self.snake.head[0]][self.snake.head[1]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
                if (level == 1):
                    time.sleep(0.2)
                elif (level == 2):
                    time.sleep(0.08)
                elif (level == 3):
                    time.sleep(0.02)
            ret = current
            self.DrawScene()
            print("Score: {}".format(self.snake.length - self.initLen))

if __name__ == '__main__' :
    
    print("select speed level")
    level = int(input("1. easy    2. medium   3. hard\n"))
    
    game = SnakeGame(60, 24, 4, 300, level)
    game.GameLoop()