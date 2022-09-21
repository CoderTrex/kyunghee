import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.live = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg="#aaaaff",
                                 width = self.width,
                                 height = self.height)
        self.ball = tk.PhotoImage(file="게임프로그래밍입문\\PongGame\\Ball\\ball.png")
        self.Canvas.create_image(50, 50, image=self.ball)
        self.canvas.pack()
        self.pack()
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Hello')
    game= Game(root)
    game.mainloop()