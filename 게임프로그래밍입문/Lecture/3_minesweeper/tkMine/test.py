import tkinter as tk
import numpy as np

class GameBoard:        # 게임 보드 클래스 생성
    def __init__(self, w, h, mine, frame):      # 게임판의 가로, 세로, 지뢰의 수, 게임판이 표시될 프레임
        self.board = tk.Frame(frame)        # 게임보드의 타일들을 포함할 프레임 'board' 생성
        self.board.pack()
        self.tileLeft = w * h - mine        # 게임에 승리하기 위해 클릭해야 하는 타일의 수를 저장
        self.mine = mine                    # 지뢰의 수를 저장
        self.flag = 0                       # 사용된 깃발의 수를 저장
        self.disabled = False               # 게임 승리, 패배, 일시정지 시에 True

        self.width = w
        self.height = h                     # 게임 판의 가로, 세로 타일 수

        self.dataBoard = np.zeros(self.width * self.height, dtype='i')
        self.dataBoard[:mine] = 9
        np.random.shuffle(self.dataBoard)
        self.dataBoard = self.dataBoard.reshape(self.width, self.height)        # 2d-array(w x h)에 지뢰를 9개 무작위 배치

        for x in range(self.width):
            for y in range(self.height):
                self.dataBoard[x][y] = self.boardCheck(x, y)        # dataBoard 9가 아닌(지뢰가 없는) 타일에 인접 지뢰 수 저장

        self.frame_tile = [[0] * self.height for _ in range(self.width)]
        self.frame_number = [[0] * self.height for _ in range(self.width)]
        self.frame_btn = [[0] * self.height for _ in range(self.width)]
        self.frame_img = [[0] * self.height for _ in range(self.width)]  # 타일별 프레임, 라벨, 버튼, 변수 초기화

    def boardCheck(self, x, y):     # dataBoard[x][y] 칸의 지뢰여부 또는 인접지뢰 수를 출력
        if self.dataBoard[x][y] == 9:
            return 9        # dataBoard[x][y] == 9 이면 그대로 반환

        result = 0
        # x와 y 좌표를 기준으로 for문을 돌림
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                # 자신의 주변의 좌표가 유효한지 확인
                if (0 <= x + i < self.width) and (0 <= y + j < self.height):
                    # 지뢰가 맞는지 확인
                    if (self.dataBoard[x + i][y + j] == 9):
                        result += 1
        return result       # dataBoard[x][y] != 9 이면 인접 지뢰 수 반환

    def boardActivate(self):        # __init__에서 구성된 보드를 부모 프레임에 표시
        for x in range(self.width):
            for y in range(self.height):        # 보드의 모든 타일에 대하여
                self.frame_tile[x][y] = tk.Frame(self.board, width=25, height=25, padx=0, pady=0, relief='sunken', bd=1)
                self.frame_tile[x][y].pack_propagate(False)
                self.frame_tile[x][y].grid(column=x, row=y)      # 타일의 사이즈를 가진 작은 프레임 생성

                number_back = self.dataBoard[x][y]
                # 뒤에 적혀 있는 수가 0이라면 아무것도 보이게 설정되지 않는다.
                if number_back == 0:
                    self.frame_number[x][y] = tk.Label(self.frame_tile[x][y], text='')
                # 만약 9라면 이는 지뢰이므로 red로 표시한다.
                elif number_back == 9:
                    self.frame_number[x][y] = tk.Label(self.frame_tile[x][y], text='', fg='red')#image=self.imgMine
                # 나머지 경우는 숫자를 표시한다.
                else:
                    self.frame_number[x][y] = tk.Label(self.frame_tile[x][y], text=number_back)     # 타일의 데이터에 따라 빈칸, 이미지, 숫자 라벨 구성 (패킹하지 않음)

                self.frame_btn[x][y] = tk.Button(self.frame_tile[x][y], command=(lambda x_=x, y_=y: self.boardClick(x_, y_)), bd=1)
                self.frame_btn[x][y].bind('<Button-3>', (lambda event, x_=x, y_=y: self.boardRightClick(x_, y_)))
                self.frame_btn[x][y].pack(fill=tk.BOTH, expand=tk.YES)                        # 각 타일에 버튼 생성, command 지정 및 우클릭 이벤트 바인드

    def boardClick(self, x, y):     # x, y 좌표의 타일이 클릭되었을 때 호출
        if not self.disabled:       # 보드가 활성화 되어있으면,
            self.frame_btn[x][y].pack_forget()
            self.frame_number[x][y].pack(fill=tk.BOTH, expand=tk.YES)       # 버튼을 언패킹. 지뢰 그림, 인접 지뢰 숫자 등을 포함한 라벨 패킹

            if self.dataBoard[x][y] == 9:
                self.frame_number[x][y].configure(background='RED', relief='flat')
                self.lose()     # 지뢰를 클릭했다면, 클릭한 칸의 배경을 붉게하고, 게임 종료
            else:
                self.tileLeft -= 1      # 지뢰가 아니라면 클리어까지 남은 타일 수를 1 감소
                if self.tileLeft == 0:
                    self.win()          # 클리어 까지 남은 타일의 수가 0이 되면 게임에서 승리

                if self.dataBoard[x][y] == 0:       # 인접 지뢰 숫자가 0인 타일에서 주변 타일로 재귀호출
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + i < self.width and 0 <= y + j < self.height \
                                and self.frame_btn[x + i][y + j].winfo_ismapped():
                                self.boardClick(x + i, y + j)

            if self.frame_img[x][y] == 1:      # 깃발이 사용된 칸을 클릭한 것이면, 우클릭 이벤트를 발생 (사용된 깃발 수 관리를 위해)
                self.boardRightClick(x, y)

    def boardRightClick(self, x, y):        # x, y 좌표의 타일이 우클릭되었을 때 호출
        if not self.disabled:               # 보드가 활성화 되어있으면,
            self.frame_img[x][y] = (self.frame_img[x][y] + 1) % 2
            if self.frame_img[x][y] == 0:
                self.frame_btn[x][y].configure(image='', text='')
            elif self.frame_img[x][y] == 1:
                self.frame_btn[x][y].configure(bg = 'green')
                self.flag += 1

    def win(self):
        self.disabled = True        # 승리시 승리 메시지 출력, 게임판 비활성화

    def lose(self):                                                                         # 패배시
        self.disabled = True        # 패배시 패배 메시지 출력, 게임판 비활성화

    def unpackBoard(self):
        self.board.pack_forget()        # 화면에서 게임판 지우기


def gameLevel():
    if game is not None:
        game.disabled = True

def gameLevelCancel():
    if game is not None:
        game.disabled = False

def gameStart(frame, level):
    global game     # 전역변수 game 사용

    if game is not None:
        game.unpackBoard()      # 실행 중이던 게임이 있으면 화면에서 지움

    if level == 0:
        w = 9
        h = 9
        mine = 10
    elif level == 1:
        w = 16
        h = 16
        mine = 40
    else:
        w = 30
        h = 16
        mine = 99
    game = GameBoard(w, h, mine, frame)     # 사용자가 선택한 레벨에 따라 게임보드 생성
    game.boardActivate()                    # 활성화

    mainWindow.geometry('%dx%d+%d+%d' % ((w + 1) * 25, (h + 1) * 25 + 64, (scrW - (w + 1) * 25) / 2, (scrH - (h + 1) * 25 - 64) / 2))
    mainFrame.configure(width=(w + 1) * 25, height=(h + 1) * 25)      # 화면의 사이즈와 위치 조정
    uiPlace(w, h)
    game.disabled = False       # ui 재설정 및 게임 활성화

def uiPlace(w, h):
    mainFrame.place(y=32)

game = None

mainWindow = tk.Tk()
scrW = mainWindow.winfo_screenwidth()
scrH = mainWindow.winfo_screenheight()
mainWindow.resizable(False, False)
mainWindow.title('지뢰 찾기')
mainWindow.lift()       # mainWindow tk 윈도우를 생성, 초기설정

# 메뉴바 선택
level = tk.IntVar()
menubar = tk.Menu(mainWindow)
filemenu = tk.Menu(menubar, tearoff=0)
# 9*9 게임을 시작
filemenu.add_command(label="9*9", command=(lambda: gameStart(mainFrame, 0)))
filemenu.add_separator()
# 16*16 게임을 시작
filemenu.add_command(label="16*16", command=(lambda: gameStart(mainFrame, 1)))
filemenu.add_separator()
# 30*16 게임을 시작
filemenu.add_command(label="30*16", command=(lambda: gameStart(mainFrame, 2)))
filemenu.add_separator()
# 게임을 종료
filemenu.add_command(label="Exit", command=(lambda: exit()))
menubar.add_cascade(label="File", menu=filemenu)
mainWindow.config(menu=menubar)

mainFrame = tk.Frame(mainWindow, width=10 * 25, height=10 * 25, padx=11, pady=11, relief='sunken', bd=1)
mainFrame.pack_propagate(False)     
uiPlace(9, 9)       

mainWindow.mainloop()