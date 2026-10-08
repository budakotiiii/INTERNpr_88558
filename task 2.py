import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")

player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]


def check_winner():
    for i in range(3):
        if (buttons[i][0]["text"] == buttons[i][1]["text"] ==
                buttons[i][2]["text"] != ""):
            return True

        if (buttons[0][i]["text"] == buttons[1][i]["text"] ==
                buttons[2][i]["text"] != ""):
            return True

    # Check diagonals
    if (buttons[0][0]["text"] == buttons[1][1]["text"] ==
            buttons[2][2]["text"] != ""):
        return True

    if (buttons[0][2]["text"] == buttons[1][1]["text"] ==
            buttons[2][0]["text"] != ""):
        return True

    return False


def is_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True


def click(button):
    global player

    if button["text"] == "":
        button["text"] = player

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"
def reset_game():
    global player
    player = "X"

    for row in buttons:
        for button in row:
            button["text"] = ""
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root,
            text="",
            font=("Arial", 30),
            width=5,
            height=2,
            command=lambda i=i, j=j: click(buttons[i][j])
        )
        buttons[i][j].grid(row=i, column=j)
reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 15),
    command=reset_game
)
reset_button.grid(row=3, column=0, columnspan=3, pady=15)

root.mainloop()