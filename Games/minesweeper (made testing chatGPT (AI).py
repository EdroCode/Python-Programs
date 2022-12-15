import random
import tkinter as tk

# Constants for the game
BOARD_SIZE = 10
NUM_MINES = 10

class Minesweeper:
    def __init__(self, root):
        # Set up the game board
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.buttons = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.num_mines_remaining = NUM_MINES
        self.num_tiles_revealed = 0
        self.game_over = False

        # Set up the GUI
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.label = tk.Label(self.frame, text=f"Mines remaining: {self.num_mines_remaining}")
        self.label.grid(row=0, column=0, columnspan=BOARD_SIZE)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j] = tk.Button(self.frame, text=" ", command=lambda row=i, col=j: self.reveal(row, col))
                self.buttons[i][j].bind("<Button-3>", lambda event, row=i, col=j: self.mark(row, col))
                self.buttons[i][j].grid(row=i+1, column=j)

        # Place the mines randomly on the board
        self.place_mines()

    def place_mines(self):
        """Places mines randomly on the board"""
        mines_placed = 0
        while mines_placed < NUM_MINES:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines_placed += 1

    def mark(self, row, col):
        """Marks the square at (row, col) as a mine"""
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = "X"
            self.num_mines_remaining -= 1
        elif self.buttons[row][col]["text"] == "X":
            self.buttons[row][col]["text"] = " "
            self.num_mines_remaining += 1
        self.label["text"] = f"Mines remaining: {self.num_mines_remaining}"
    
    def reveal(self, row, col):
        """Reveals the square at (row, col)"""
        if self.game_over:
            return
        if self.buttons[row][col]["text"] == "X":
            return
        if self.board[row][col] == -1:
            # Game over
            self.game_over = True
            self.buttons[row][col]["text"] = "M"
            self.label["text"] = "Game over! You lose."
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if self.board[i][j] == -1:
                        self.buttons[i][j]["text"] = "M"
                    self.buttons[i][j]["state"] = "disabled"
            return
        if self.board[row][col] != 0:
            # Square has already been revealed
            return

        # Reveal the square
        self.board[row][col] = self.get_adjacent_mines(row, col)
        self.buttons[row][col]["text"] = str(self.board[row][col])
        self.num_tiles_revealed += 1
        if self.num_tiles_revealed + NUM_MINES == BOARD_SIZE ** 2:
            # Player has won
            self.game_over = True
            self.label["text"] = "You win!"
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    self.buttons[i][j]["state"] = "disabled"

        # Check if we should reveal more squares
        if self.board[row][col] == 0:
            self.reveal(row - 1, col)
            self.reveal(row + 1, col)
            self.reveal(row, col - 1)
            self.reveal(row, col + 1)

    def get_adjacent_mines(self, row, col):
        """Returns the number of mines adjacent to the square at (row, col)"""
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE:
                    continue
                if self.board[i][j] == -1:
                    count += 1
        return count

# Run the game
root = tk.Tk()
minesweeper = Minesweeper(root)
root.mainloop()    
