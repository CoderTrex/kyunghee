import Tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.live = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvans(self, bg="#aaaaff",
                                 width = self.width,
                                 height = self.height)
        self.canvas.pack()
        self.pack()
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Hello')
    game= Game(root)
    game.mainloop()

