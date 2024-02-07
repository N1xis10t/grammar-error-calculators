import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    
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
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget to display the current expression/result
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, justify="right", font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(window, text=button_text, padx=20, pady=20, font=('Arial', 12),
              command=lambda text=button_text: on_click(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
window.mainloop()
