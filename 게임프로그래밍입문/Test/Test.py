
import tkinter as tk
from PIL import ImageTk, Image

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def delete(self):
        self.canvas.delete(self.item)


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

    def hit(self):
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])


class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.level = 0
        self.width = 610
        self.height = 400
        
        
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width, height=self.height,)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.menubar = tk.Menu(master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="9*9", command=self.start_game(1))
        self.filemenu.add_command(label="13*13", command=self.start_game(2))
        self.filemenu.add_command(label="20*20", command=self.start_game(3))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label= "file", menu=self.filemenu)
        master.config(menu=self.menubar)
        
        self.hud = None
        self.canvas.focus_set()

    
    # def setup_game(self, level):
    #     #여기서 레벨의 값을 입력을 받고 이것을 start_game에 값을 전달해 
    #     if (level == 1):
    #         self.start_game()
    #     self.canvas.bind('<space>', lambda _ : self.start_game())

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size='40'):
        font = ('Helvetica', size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        text = 'Lives: %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self, level):
        if (level == 1):
            for y in range(50, self.height - 5, 20):    
                for x in range(5, 65, 20):
                    self.add_brick(x + 5, y, 1)
        if (level == 2):
            for y in range(50, self.height - 5, 20):    
                for x in range(5, self.width - 5, 20):
                    self.add_brick(x + 5, y, 1)
        if (level == 3):
            for y in range(50, self.height - 5, 20):    
                for x in range(5, self.width - 5, 20):
                    self.add_brick(x + 5, y, 1)
        self.game_loop()

    def game_loop(self):
        num_bricks = len(self.canvas.find_withtag('brick'))
        if num_bricks == 0: 
            self.level += 1


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello, Mine!')
    game = Game(root)
    game.mainloop()