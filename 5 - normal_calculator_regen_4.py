import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying input and results
entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Additional buttons
tk.Button(root, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
tk.Button(root, text='AC', width=5, height=2, command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val + 1)
tk.Button(root, text='%', width=5, height=2, command=lambda: on_click('%')).grid(row=row_val, column=col_val + 2)

# Configure column weights to make them expandable
for i in range(4):
    root.columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
