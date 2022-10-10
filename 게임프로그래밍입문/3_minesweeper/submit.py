import tkinter as tk
import numpy as np
from tkinter import messagebox as msg
import tkinter.font

TILE_SIZE = 24


class Game:
    def __init__(self, w, h, mine, frame):
        
        
        self.board = tk.Frame(frame)
        self.board.pack()
        self.tileLeft = w*h - mine     # 게임 승리를 위해 눌어야 하는 지뢰의 수
        self.mine = mine                # 지뢰의 수를 저장
        self.flag = 0                   # 사용된 깃발의 수를 저장
        self.disabled = False
        
        self.width = w
        self.height = h
        
        
        # 보드를 만드는데 전부 0로로 생성된 보드를 만든다
        self.dataBoard = np.zeros(self.width*self.height, dtype='i')
        self.dataBoard[:mine] = 9 # 지뢰는 9로 인덱싱함
        np.random.shuffle(self.dataBoard) #데이터 보드를 섞는다
        self.dataBoard = self.dataBoard.reshape(self.width, self.height) # 지뢰를 무작위로 배치
        
        for  x in range(self.width):
            for y in range(self.height):
                self.dataBoard[x][y] = self.boardCheck(x,y)
        
        # 타일별 프레임, 라벨, 버튼, 변수 초기화
        self.tileFrame = [[0] * self.height for _ in range(self.width)]
        self.tileBack = [[0] * self.height for _ in range(self.width)]
        self.tileBtn = [[0] * self.height for _ in range(self.width)]
        self.tileBtnImg = [[0] * self.height for _ in range(self.width)]
    
    def boardCheck(self, x, y):
        # 지뢰이라면 9를 그대로 반환함.
        if (self.board[x][y] == 9):
            return 9
        
        result = 0
        # x와 y좌표를 기준으로 for 문을 돌림
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                # 자신의 주변의 좌표가 유효한지 확인
                if (0 <= x + i < self.width) and (0 <= y + j < self.height):
                    # 지뢰가 맞는지 확인
                    if (self.dataBoard[x + i][y + j] == 9):
                        result += 1
        return result
    
    def boardActivated(self):
        for x in range(self.width):
            for y in range(self.height):                                  # padx and pady = 여백 크기 0 / relief 테두리 스타일
                self.tileFrame[x][y] = tk.Frame(self.board, width=TILE_SIZE, height=TILE_SIZE, padx=0, pady=0, relief='raised', bd = 1)
                self.tileFrame[x][y].pack_propagate(False)
                self.tileFrame[x][y].grid()
                
                backText = self.dataBoard[x][y]
                if backText == 0:
                    self.tileBack[x][y] = tk.Label(self.tileFrame[x][y], text = '')
                elif backText == 9:
                    self.tileBack[x][y] = tk.Label(self.tileFrame[x][y], text = '')
                else:
                    self.tileBack[x][y] = tk.Label(self.tileFrame[x][y], text='')
                
                self.tileBtn[x][y] = tk.Button(self.tileFrame[x][y], command=(lambda))