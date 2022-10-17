from doctest import master
import tkinter as tk

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

class Brick(GameObject):
    COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}

    def __init__(self, canvas, x, y, hits):
        self.width = 20
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2,
                                        x + self.width / 2, y + self.height / 2,
                                        fill=color, tags='brick')
        super(Brick, self).__init__(canvas, item)

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.level = 1
        self.reset = 1
        self.width = 300
        self.height = 300
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="9*9", command= self.)
        filemenu.add_command(label="9*9", command = self.begin)

        self.items = {}
        self.ball = None

        self.hud = None
        self.setup_game(self.level, self.reset)
        self.canvas.focus_set()

    def make_brick(self, level):
        if (level == 1):
            for y in range(10, 180, 20):
                for x in range(-25, 180, 20):
                    self.add_brick(x + 40, y, 1)
        
        if (level == 2):
            for y in range(10, 380, 20):
                for x in range(5, 380, 20):
                    self.add_brick(x + 40, y, 1)
        if (level == 3):
            for y in range(10, 380, 20):
                for x in range(5, 380, 20):
                    self.add_brick(x + 40, y, 1)

    def setup_game(self, level, reset):

        
        if (reset == 1):
            self.make_brick(level)
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def start_game(self):
        self.canvas.unbind('<space>')
        self.canvas.delete(self.text)
        self.game_loop()

    def game_loop(self):
        i = (int)(input("choose level"))
        self.after(1000, self.setup_game(i, self.reset))

if __name__ == '__main__':
    root = tk.Tk()
    root.title('mine!')
    game = Game(root)
    game.mainloop()