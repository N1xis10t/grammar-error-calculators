import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.result_var = tk.StringVar()

        # Entry widget to display the result
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 14), bd=10, insertwidth=4, width=14, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons and add them to the grid
        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'C':
            self.result_var.set('')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator_app = CalculatorApp(root)
    root.mainloop()
