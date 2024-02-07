import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 18), bd=10, insertwidth=4, width=14,
                                justify='right')
        result_entry.grid(row=0, column=0, columnspan=4)

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
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_result = self.result_var.get()

        if button == '=':
            try:
                result = str(eval(current_result))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            current_result += str(button)
            self.result_var.set(current_result)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
