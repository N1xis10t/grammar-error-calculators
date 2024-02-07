import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry widget to display input and results
        self.entry_var = tk.StringVar()
        entry = tk.Entry(master, textvariable=self.entry_var, font=('Arial', 14), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Configure grid for buttons
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, font=('Arial', 14), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure row and column weights to make the GUI resizable
        for i in range(1, 5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i - 1, weight=1)

    def on_button_click(self, button):
        current_text = self.entry_var.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        else:
            self.entry_var.set(current_text + button)


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
