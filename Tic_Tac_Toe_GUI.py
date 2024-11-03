import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables
current_player = "X"
board = [" "]*9
buttons = []

# Check for a winner or tie
def check_winner():
    global current_player
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
            return
    if " " not in board:
        messagebox.showinfo("Game Over", "It's a Tie!")
        reset_game()

# Handle a player's move
def player_move(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Reset the game board
def reset_game():
    global current_player, board
    current_player = "X"
    board = [" "]*9
    for button in buttons:
        button.config(text="")

# Create and place buttons on the board
for i in range(9):
    button = tk.Button(root, text="", font="Arial 24", width=8, height=4,
                       command=lambda i=i: player_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the game loop
root.mainloop()