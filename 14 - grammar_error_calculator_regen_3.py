import tkinter as tk

def on_click(event):
    current_text = entry_var.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, font=('Helvetica', 14), padx=20, pady=20)
    button.grid(row=row_val, column=col_val, sticky='nsew')
    button.bind('<Button-1>', on_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights so that they expand proportionally
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the Tkinter eve
