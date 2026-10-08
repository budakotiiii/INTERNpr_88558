import tkinter as tk

root = tk.Tk()
root.title("Connect Four")

board = [["" for _ in range(7)] for _ in range(6)]
player = "X"

def check_win(r, c):
    p = board[r][c]

    for dr, dc in [(1,0), (0,1), (1,1), (1,-1)]:
        count = 1

        for x in [1, -1]:
            nr, nc = r + dr*x, c + dc*x
            while 0 <= nr < 6 and 0 <= nc < 7 and board[nr][nc] == p:
                count += 1
                nr += dr*x
                nc += dc*x

        if count >= 4:
            return True
    return False

def play(c):
    global player

    for r in range(5, -1, -1):
        if board[r][c] == "":
            board[r][c] = player
            buttons[r][c]["text"] = player

            if check_win(r, c):
                print(player, "Wins!")
                root.after(100, root.destroy)

            player = "O" if player == "X" else "X"
            break

buttons = []

for r in range(6):
    row = []
    for c in range(7):
        b = tk.Button(root, text="", width=4, height=2,
                      font=("Arial", 18),
                      command=lambda c=c: play(c))
        b.grid(row=r, column=c)
        row.append(b)
    buttons.append(row)

root.mainloop()