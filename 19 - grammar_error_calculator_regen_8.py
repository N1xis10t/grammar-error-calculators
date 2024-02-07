import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expression
entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
              command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text='C', width=5, height=2, font=('Arial', 14), command=clear_entry).grid(row=5, column=0, columnspan=3)
# Backspace button
tk.Button(root, text='⌫', width=5, height=2, font=('Arial', 14), command=lambda: entry.delete(len(entry.get()) - 1, tk.END)).grid(row=5, column=3)

# Equal button
tk.Button(root, text='=', width=5, height=2, font=('Arial', 14), command=evaluate_expression).grid(row=5, column=2)

# Run the Tkinter event loop
root.mainloop()
