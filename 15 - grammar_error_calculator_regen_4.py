import tkinter as tk

def on_click(button_value):
    current_expression = entry_var.get()
    
    if button_value == "=":
        try:
            result = eval(current_expression)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    else:
        entry_var.set(current_expression + str(button_value))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to display the current expression
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, justify="right", font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col)

# Run the application
window.mainloop()
