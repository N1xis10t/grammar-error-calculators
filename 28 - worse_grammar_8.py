import tkinter as tk

def on_click(button_value):
    current_text = result_var.get()
    
    if button_value == "=":
        try:
            result_var.set(eval(current_text))
        except Exception as e:
            result_var.set("Error")
    elif button_value == "C":
        result_var.set("")
    else:
        result_var.set(current_text + str(button_value))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Variable to store the result
result_var = tk.StringVar()

# Entry widget to display the result
result_entry = tk.Entry(root, textvariable=result_var, font=('Arial', 18), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
