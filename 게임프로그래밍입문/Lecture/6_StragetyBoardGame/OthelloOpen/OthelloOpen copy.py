import cocos
from cocos.menu import *
import numpy as np
import cocos.euclid as eu

class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        w, h = cocos.director.director.get_window_size()
        self.score_text = cocos.text.Label('', font_size=18, color=(50, 50, 255, 255))
        self.score_text.position = (20, h - 40)
        self.add(self.score_text)

    def update_score(self, person, computer):
        self.score_text.element.text = 'You: %s, Computer: %s' % (person, computer)

    def show_game_over(self, winner):
        w, h = cocos.director.director.get_window_size()
        game_over = cocos.text.Label(winner, font_size=50,
                                    anchor_x='center',
                                    anchor_y='center',
                                    color=(50, 50, 255, 255))
        game_over.position = w * 0.5, h * 0.5
        self.add(game_over)

class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    PERSON = -1
    COMPUTER = 1
    
    def __init__(self, difficulty, hud_layer):
        super(GameLayer, self).__init__()
        self.difficulty = difficulty

        self.levelDepth = self.difficulty*2+2
        self.hud = hud_layer
        self.square = 75
        self.row = 8
        self.column = 8
        self.height = self.row*self.square
        self.width = self.column*self.square
        self.table = np.arange(self.row*self.column).reshape(self.row, self.column)
        if difficulty == 1:
            self.weight = np.array(     [   [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1], 
                                            [  1,    1,    1,    1,    1,    1,    1,    1]])
        elif difficulty == 2:
            self.weight = np.array(     [   [ 50,  -10,   15,   15,   15,   15,  -10,   50],
                                            [-10,  -20,  -10,  -10,  -10,  -10,  -20,  -10],
                                            [ 15,  -10,    1,    1,    1,    1,  -10,   15], 
                                            [ 15,  -10,    1,    1,    1,    1,  -10,   15], 
                                            [ 15,  -10,    1,    1,    1,    1,  -10,   15], 
                                            [ 15,  -10,    1,    1,    1,    1,  -10,   15], 
                                            [-10,  -20,  -10,  -10,  -10,  -10,  -20,  -10], 
                                            [ 50,  -10,   15,   15,   15,   15,  -10,   50]])
        elif difficulty == 3:
            self.weight = np.array(     [   [ 20,   -3,   11,    8,    8,   11,   -3,   20], 
                                            [ -3,   -7,   -4,    1,    1,   -4,   -7,   -3], 
                                            [ 11,   -4,    2,    2,    2,    2,   -4,   11], 
                                            [  8,    1,    2,   -3,   -3,    2,    1,    8], 
                                            [  8,    1,    2,   -3,   -3,    2,    1,    8], 
                                            [ 11,   -4,    2,    2,    2,    2,   -4,   11], 
                                            [ -3,   -7,   -4,    1,    1,   -4,   -7,   -3], 
                                            [ 20,   -3,   11,    8,    8,   11,   -3,   20]])

        for x in range  (0, self.column+1) :
            line = cocos.draw.Line((x*self.square, 0), (x*self.square, self.height), (255, 0, 255, 255))
            self.add(line)
        for y in range  (0, self.row+1) :
            line = cocos.draw.Line((0, y*self.square), (self.width, y*self.square), (255, 0, 255, 255))
            self.add(line)

        # 스프라이트가 드어가는 위치
        self.disk = [[None for i in range(self.column)] for j in range(self.row)]

        for y in range (0, self.row) :
            for x in range (0, self.column) :
                # 센터값 찾고 위치에 돌을 놓게 됨
                centerPt = eu.Vector2(x*self.square + self.square/2, y*self.square + self.square/2)
                self.disk[y][x] = cocos.sprite.Sprite('ball.png', position = centerPt, color = (255, 255, 255))
                self.add(self.disk[y][x])

        self.setup()
        # 사람 턴
        self.turn = GameLayer.PERSON
        self.count = 0 #딜레이를 설정함
        self.schedule(self.update)

    def setup(self):
        for y in range (0, self.row) :
            for x in range (0, self.column) :
                self.table[y][x] = 0
        # 초기돌 설정
        self.table[3][3] = GameLayer.PERSON
        self.table[3][4] = GameLayer.COMPUTER
        self.table[4][3] = GameLayer.COMPUTER
        self.table[4][4] = GameLayer.PERSON
        
    def update(self, dt):
        computer = 0
        person = 0
        self.count += 1
        
        for y in range  (0, self.row) :
            for x in range  (0, self.column) :
                if self.table[y][x] == GameLayer.COMPUTER:
                    self.disk[y][x].color = (255, 255, 255)
                    self.disk[y][x].visible = True
                    computer += 1
                elif self.table[y][x] == GameLayer.PERSON:
                    self.disk[y][x].color = (0, 0, 0)
                    self.disk[y][x].visible = True
                    person += 1
                else:
                    self.disk[y][x].visible = False

        self.hud.update_score(person, computer)

        moves1 = self.getMoves(GameLayer.PERSON, self.table)
        moves2 = self.getMoves(GameLayer.COMPUTER, self.table)

        if self.turn == GameLayer.PERSON and len(moves1) == 0:
            self.turn *= -1

        if computer+person == self.row*self.column or (len(moves1) == 0 and len(moves2) == 0):
            if computer > person:
                self.hud.show_game_over('Computer win')
            elif computer < person:
                self.hud.show_game_over('You win')
            else:
                self.hud.show_game_over('Draw')

        if self.turn == GameLayer.COMPUTER and self.count > 100:
            self.computer()

    
    # 뒤집히는 좌표의 리스트를 반환함
    # 좌표와 누구의 턴인지, 보드를 호출한다.
    def isPossible(self, x, y, turn, board):
        rtnList = list()
        
        if board[y][x] != 0: return rtnList

        for dirX in range(-1, 2):
            for dirY in range(-1,2):
                # 자신의 위치는 건너뜀
                if dirX == 0 and dirY == 0: continue
                # 경계를 뛰어넘는 위치의 값은 계산하지 않음(바운더리 계산)
                if(x+dirX < 0 or x+dirX >= self.column): continue
                if(y+dirY < 0 or y+dirY >= self.row): continue
                
                
                xList = list()
                yList = list()
                
                
                if dirX == 0:
                    # 계산의 바운더리를 넓게 계산함
                    for yy in range(y+dirY*2, self.row*dirY, dirY):
                        # 넓은 바운더리의 처리는 break로 예외 처리 함
                        if(yy < 0 or yy >= self.row): break
                        xList.append(x)
                        yList.append(yy)
                elif dirY == 0:
                    for xx in range(x+dirX*2, self.column*dirX, dirX):
                        if(xx < 0 or xx >= self.column): break
                        xList.append(xx)
                        yList.append(y)
                else:
                    for xx, yy in zip(range(x+dirX*2, self.column*dirX,dirX), range(y+dirY*2, self.row*dirY,dirY)):
                        if(xx < 0 or xx >= self.column): break
                        if(yy < 0 or yy >= self.row): break
                        xList.append(xx)
                        yList.append(yy)

                bDetected = False
                revList = []
                # 상대방 돌인지 아닌지 확인함 맞다면 진행함.
                if board[y+dirY][x+dirX] == turn*-1:
                    revList.append((x+dirX, y+dirY))
                    for xx, yy in zip(xList, yList):
                        if xx >= self.column or xx < 0 or yy >= self.row or yy < 0:
                            break
                        # 만약 상대방 돌이라면 리스트에 계속해서 추가함.
                        if board[yy][xx] == turn*-1:
                            revList.append((xx, yy))
                        # 내 돌을 만나면 종료하고 트루를 반환함
                        if board[yy][xx] == turn:
                            bDetected = True
                            break
                        if board[yy][xx] == 0:
                            break
                    # 자신의 돌을 만났는지 여부를 확인하고 만나지 않았다면, 빈리스트를 반환함.
                    if(bDetected == False): revList = []

                rtnList += revList;

        return rtnList

    def on_mouse_release(self, x, y, buttons, mod):
        if self.turn != GameLayer.PERSON:
            return

        moves = self.getMoves(GameLayer.PERSON, self.table)

        if len(moves) > 0:    
            xx = x//self.square
            yy = y//self.square

            revList = self.isPossible(xx, yy, GameLayer.PERSON, self.table)

            if len(revList) == 0: return

            self.table[yy][xx] = GameLayer.PERSON
            for revX, revY in revList:
                self.table[revY][revX] = GameLayer.PERSON
            
        self.turn *= -1
        # 딜레이 시간 초기화
        self.count = 0     
    
    
    # AI 파트
    # 놓을 수 있는 위치에 대한 정보값을 다 저장함.
    def getMoves(self, turn, board):
        moves = []
        for y in range  (0, self.row) :
            for x in range  (0, self.column) :
                if board[y][x] != 0: continue

                revList = self.isPossible(x, y, turn, board)
                if len(revList) > 0 :
                    moves.append((x, y, revList))
        return moves

            
    def computer(self):  
        move = self.minimax(GameLayer.COMPUTER)

        if len(move) > 0:
            self.table[move[1]][move[0]] = GameLayer.COMPUTER

            for revX, revY in move[2]:
                self.table[revY][revX] = GameLayer.COMPUTER

        self.turn *= -1
        
    def minimax(self, player):
        moves = self.getMoves(player, self.table)

        if len(moves) == 0: return moves
        
        scores = np.zeros(len(moves))
        
        alpha = float("-inf")
        beta = float("inf")

        for i, move in enumerate(moves):
            boardCopy = self.getNewBoard(move[0], move[1], move[2], GameLayer.COMPUTER, np.copy(self.table))
            #scores[i] = self.maxMove(boardCopy, 1, alpha, beta)
            if 1 >= self.levelDepth:
                scores[i] = self.boardScore(boardCopy)
            else:
                scores[i] = self.minMove(boardCopy, 2, alpha, beta)

        maxIndex = np.argmax(scores) #가장 큰 것에 대한 인덱스 값

        return moves[maxIndex]


    def getNewBoard(self, x, y, revList, player, table):   
        table[y][x] = player
        for (x,y) in revList:
            table[y][x] = player
        return table    



    def minMove(self, board, depth, alpha, beta):
        # 사람이 놓을 수 있는 위치를 받아옴
        moves = self.getMoves(GameLayer.PERSON, board)
        # 점수에 대해서 0으로 세팅
        scores = np.zeros(len(moves))

        # 움직일 수 있는 곳이 없다면
        if len(moves)==0:
            # 만약 depth가 레벨 난이도 보다 작다면 maxMove를 계속해서 진행함
            if depth <= self.levelDepth:
                return self.maxMove(board, depth+1, alpha, beta)
            # 보드의 스코어를 반환함.
            else:
                return self.boardScore(board)

        for i, move in enumerate(moves):
            # 카피된 보드의 위치
            boardCopy = self.getNewBoard(move[0], move[1], move[2], GameLayer.PERSON, np.copy(board))
            # 레벨 깊이보다 매개 변수 depth의 크기가 크면 값을 더 이상 찾지 않는다.
            if depth >= self.levelDepth:
                scores[i] = self.boardScore(boardCopy)
            else:
                # maxMove를 이용해 찾을 값을 score에 넣는다.
                scores[i] = self.maxMove(boardCopy, depth+1, alpha, beta)
                # 그 값이 beta보다 작다면, beta에 그 값을 넣는다.
                if beta > scores[i]:
                    beta = scores[i]
                if beta <= alpha:
                    return scores[i]

        return min(scores)

    def maxMove(self, board, depth, alpha, beta):
        moves = self.getMoves(GameLayer.COMPUTER, board)
        scores = np.zeros(len(moves))

        if len(moves)==0:
            if depth <= self.levelDepth:
                return self.minMove(board, depth+1, alpha, beta)
            else:
                return self.boardScore(board)

        for i, move in enumerate(moves):
            boardCopy = self.getNewBoard(move[0], move[1], move[2], GameLayer.COMPUTER, np.copy(board))
            if depth >= self.levelDepth:
                scores[i] = self.boardScore(boardCopy)
            else:
                scores[i] = self.minMove(boardCopy, depth+1, alpha, beta)
                if scores[i] > alpha:
                    alpha = scores[i]
                if beta <= alpha:
                    return scores[i]
        return max(scores)

    # 보드의 스코어를 출력하는 함수 
    # ai의 버튼이 더 많으면 양수를 출력하고 / 플레이어의 버튼이 더 많으면 음수를 출력한다.
    def boardScore(self, board):
        computerWeightSum = 0
        personWeightSum = 0

        for y in range(0, self.row):
            for x in range(0, self.column):
                if board[y][x] == GameLayer.COMPUTER:
                    computerWeightSum += self.weight[y][x]

                if board[y][x] == GameLayer.PERSON:
                    personWeightSum += self.weight[y][x]

        return computerWeightSum - personWeightSum;
        
class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Game')
        self.font_title['font_name'] = 'Times New Roman'
        self.font_title['font_size'] = 60
        self.font_title['bold'] = True
        self.font_item['font_name'] = 'Times New Roman'
        self.font_item_selected['font_name'] = 'Times New Roman'

        self.selDifficulty = 0
        self.difficulty = ['Easy', 'Normal', 'Hard']

        items = list()
        items.append(MenuItem('New Game', self.start_game))
        items.append(MultipleMenuItem('Difficuly: ', self.set_difficulty, self.difficulty, 0))
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
        

    def set_difficulty(self, index):
        self.selDifficulty = index

if __name__ == '__main__':
    cocos.director.director.init(caption='Othello', width = 75*8, height = 75*8)

    scene = cocos.scene.Scene()
    scene.add(MainMenu())
    
    cocos.director.director.run(scene)
