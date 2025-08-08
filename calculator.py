import tkinter as tk

# Function to handle button click
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Initialize main window
root = tk.Tk()
root.title("BHAI KO SAHU BOLTE HAI")
root.geometry("400x500")
root.configure(bg="lightblue")  # Background color of the window

# Screen where the numbers and results will be shown
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, insertwidth=4, width=15, justify='right')
screen.pack(pady=20)

# Button Frame
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

# Button Texts
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

# Create buttons and place them in the grid
row = 0
col = 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="lucida 15 bold", relief="raised", bd=3, width=5, height=2, bg="white", fg="black")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()