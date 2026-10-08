import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
clock_label = tk.Label(
    root,
    font=("Arial", 50),
    bg="black",
    fg="cyan"
)
clock_label.pack(expand=True, fill="both")
update_clock()

root.mainloop()