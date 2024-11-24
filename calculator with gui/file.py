import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            display_var.set(result)
            expression = str(result)
        except Exception as e:
            display_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        display_var.set("")
    else:
        expression += text
        display_var.set(expression)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""  # Store the current input and calculation
display_var = tk.StringVar()

# Display Screen
display = tk.Entry(root, textvar=display_var, font=("Arial", 20), bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button Layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font=("Arial", 18), relief=tk.RAISED, bd=5, padx=10, pady=10)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:  # Move to the next row after 4 buttons
        row += 1
        col = 0

# Adjust row/column weight for resizing
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
