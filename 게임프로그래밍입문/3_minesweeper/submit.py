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
    
    # __init__에서 구성된 보드를 부모 프레임에 표시를 진행함
    def boardActivated(self):
        # 가로와 세로만큼 for문을 돌린다.
        for x in range(self.width):
            for y in range(self.height):                                  # padx and pady = 여백 크기 0 / relief 테두리 스타일
                self.tileFrame[x][y] = tk.Frame(self.board, width=TILE_SIZE, height=TILE_SIZE, padx=0, pady=0, relief='raised', bd = 1)
                self.tileFrame[x][y].pack_propagate(False)
                self.tileFrame[x][y].grid(column=x, row=y) # 타일의 사이즈를 가진 작은 프레임을 형성
                
                backText = self.dataBoard[x][y]
                # 아무 것도 아닌 공간의 색은 없다.
                if backText == 0:
                    self.tileBack[x][y] = tk.Label(self.tileFrame[x][y], text = '')
                # 지뢰의 원래 색을 red이다.
                elif backText == 9:
                    self.tileBack[x][y] = tk.Label(self.tileFrame[x][y], text = '', fg='red')
                # 이외 숫자를 가진 타일은 그대로의 모습을 가져간다.
                else:
                    self.tileBack[x][y] = tk.Label(self.tileFrame[x][y], text=backText) # 타일 데이터에 따라 빈칸, 이미지, 숫자 라벨 구성
                
                self.tileBtn[x][y] = tk.Button(self.tileFrame[x][y], command=(lambda x_=x, y_=y: self.boardClick(x_, y_)), bd=1)
                self.tileBtn[x][y].bind('<Button-3>', (lambda event, x_=x,y_=y: self.boarRightClick(x_, y_)))
                self.tileBtn[x][y].pack(fill=tk.BOTH, expand=tk.YES)
    
    # x, y 좌표의 타일이 클릭되었을 때 호출
    def boardClick(self, x, y):
        if not self.disabled: #보드가 활성화된 경우
            self.tileBtn[x][y].pack_forget()
            self.tileBack[x][y].pack(fill=tk.BOTH, expand=tk.YES) # 버튼을 언패킹, 지뢰 그림, 인접 지뢰 숫자등을 포함한 레벨 패킹
            
            if self.dataBoard[x][y] == 9:
                self.tileBack[x][y].configure(background='RED', relief='flat')
                self.lose()
            else:
                self.tileLeft -= 1
                if self.tileLeft == 0:
                    self.win()
                
                if self.dataBoard[x][y] == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if (0 <= x + i < self.width and 0 <= y + j < self.height and self.tileBtn[x + i][y + j].winfo_ismapped()):
                                self.boardClick(x + i, y + j)
                            
            if self.tileBtnImg[x][y] == 1:
                self.boardClick(x, y)


    def boardRightClick(self, x, y):
        if not self.disabled:
            self.tileBtnImg[x][y]



game = None

mainWindow = tk.Tk()
scrW = mainWindow.winfo_screenwidth()
scrH = mainWindow.winfo_screenheight()
mainWindow.geometry('%dx%d+%d+%d' % (10 * TILE_SIZE, 10 * TILE_SIZE + 64, (scrW - 10 * TILE_SIZE)/2, (scrH - 10 * TILE_SIZE - 64)/2))
mainWindow.resizable(False, False)
mainWindow.title('지뢰 찾기')
mainWindow.lift()       # mainWindow tk 윈도우를 생성, 초기설정



defaultFont = tk.font.Font(family='맑은 고딕', size=10, weight='bold')
mainWindow.option_add("*Font", defaultFont)             # mainWindow 기본 폰트 지정

level = tk.IntVar()
menubar = tk.Menu(mainWindow)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="9*9", command=(lambda: gameStart(mainFrame, 0)))
filemenu.add_separator()
filemenu.add_command(label="16*16", command=(lambda: gameStart(mainFrame, 1)))
filemenu.add_separator()
filemenu.add_command(label="30*16", command=(lambda: gameStart(mainFrame, 2)))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=(lambda: exit()))
menubar.add_cascade(label="File", menu=filemenu)
mainWindow.config(menu=menubar)

""" mainWindow 의 GUI 구성 """
imgFlagCnt = tk.PhotoImage(file='C:\\Coding\\github\\kyunghee\\게임프로그래밍입문\\3_minesweeper\\tkMine\\img\\flag.png')

mainFrame = tk.Frame(mainWindow, width=10 * TILE_SIZE, height=10 * TILE_SIZE, padx=11, pady=11, relief='sunken', bd=1)
mainFrame.pack_propagate(False)     # 게임이 들어갈 mainFrame 생성


uiPlace(9, 9)       # mainWindow 위젯 배치 함수

mainWindow.mainloop()