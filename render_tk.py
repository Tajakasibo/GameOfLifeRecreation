'''Render Game of Life boards to a TK Gui.'''
import tkinter as tk
import game_of_life

X = game_of_life.X
Y = game_of_life.Y
PIXEL = 10

class MainWindow():

    def __init__(self, root):
        self.root = root
        self.active = False

        # Divide up GUI into frames
        button_frame = tk.Frame(root)
        button_frame.pack()
        canvas_frame = tk.Frame(root)
        canvas_frame.pack()

        # Buttons for the user
        self.button = tk.Button(button_frame, text="Exit", fg="red", command=quit)
        self.button.pack(side=tk.LEFT)
        self.restart_button = tk.Button(button_frame, text="Randomize", command=self.init_board)
        self.restart_button.pack(side=tk.LEFT)
        self.start_button = tk.Button(button_frame, text="Start", command=self.starting)
        self.start_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stopping)
        self.stop_button.pack(side=tk.LEFT)
        self.step_button = tk.Button(button_frame, text="Step", command=self.step)
        self.step_button.pack(side=tk.LEFT)

        # Canvas for the 'life'
        self.canvas = tk.Canvas(canvas_frame, width=X*PIXEL, height=Y*PIXEL)
        self.canvas.pack(side=tk.LEFT)

        # Initialize the board and launch the auto-running process
        self.init_board()
        self.looping()

    def starting(self):
        self.active = True

    def stopping(self):
        self.active = False

    def step(self):
        self.active = False
        self.update_board()

    def init_board(self):
        self.board = game_of_life.init_board()
        self.draw()

    def update_board(self):
        self.board = game_of_life.next_board(self.board)
        self.draw()

    def looping(self):
        if self.active:
            self.update_board()
        self.root.after(250, self.looping)

    def draw(self):
        '''Render the current gameboard to the Canvas window.'''
        self.canvas.delete('all')
        for y, row in enumerate(self.board):
            for x, pixel in enumerate(row):
                if self.board[y][x]:
                    self.canvas.create_rectangle(
                        x*PIXEL, y*PIXEL,
                        (x+1)*PIXEL, (y+1)*PIXEL,
                        fill="#6a0dad"
                    )


def test():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    test()



