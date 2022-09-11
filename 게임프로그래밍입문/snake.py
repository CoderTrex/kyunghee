# -*- coding: utf8 -*-
from __future__ import print_function
import random
import os
import re
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
    
    def __init__(self, w, h, length, delay):
        self.W = w
        self.H = h
        self.initLen = length
        self.snake = Snake(length)
        self.delay = delay  
        self.board = [[[0]*2 for x in range(self.W)] for y in range(self.H)]
        #self.board[a][b][c]

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
   
    # def Makefood():
    #     x = random.randint(0, self.W-1)
    #     y = random.randint(0, self.H-1)

    #     while self.board[y][x][SnakeGame.element["SPRITE"]] != SnakeGame.sprite["EMPTY"]:
    #         x = random.randint(0, self.W-1)
    #         y = random.randint(0, self.H-1)

    #     self.board[y][x][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["FOOD"]
    #     pass
 
    def GameLoop(self):
        self.DrawScene()

        ret = SnakeGame.direction["RIGHT"]
        current = SnakeGame.direction["RIGHT"]
        
        while True:
            start = time.time()
            
            while (time.time() - start) <= self.delay/1000:
                if msvcrt.kbhit():
                    current = SnakeGame.GetDirection()

                if ((ret == current) or (ret == (current * -1))):
                    current = ret
                # up = 1 down = 1 right = 2 left = -2
                
                food = 0
                #헤드 변환 지정
                if (current == 1):
                    self.snake.head[0] += 1
                    #새로 바뀐 헤드 위치에 대해서 보드값 변환
                    self.board[self.snake.head[1]][self.snake.head[0]][SnakeGame.element["DIRECTION"]] = SnakeGame.direction["UP"]
                    self.board[self.snake.head[1]][self.snake.head[0]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["HEAD"]
                    
                    if (self.board[self.snake.head[1]][self.snake.head[0]][SnakeGame.element["SPRITE"]] == SnakeGame.sprite["FOOD"]):
                        self.snake.length += 1
                        food = 1

                
                
                #지나간 꼬리의 테이블 정보를 바꾼다.
                self.board[self.snake.tail[1]][self.snake.tail[0]][SnakeGame.element["SPRITE"]] = SnakeGame.sprite["EMPTY"]
                
                #꼬리가 움직여야 하는 위치를 변환해준다.
                if (food == 0):
                    direction = self.board[self.snake.tail[1]][self.snake.tail[0]][SnakeGame.element["DIRECTION"]]
                    if (direction == 1) :
                        self.snake.tail[0] += 1 
                    elif (direction == -1) :
                        self.snake.tail[0] -= 1
                    elif (direction == 2) :
                        self.snake.tail[1] += 1
                    elif (direction == -2) :
                        self.snake.tail[1] -= 1
            ret = current
            self.DrawScene()
            print("Score: {}".format(self.snake.length - self.initLen))

if __name__ == '__main__' :
    game = SnakeGame(60, 24, 4, 300)
    game.GameLoop()