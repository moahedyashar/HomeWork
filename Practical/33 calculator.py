import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('calculator app')

        self.expression = ""

        self.entry = tk.Entry(root, font=('Arial', 24), bd=10, width=14, borderwidth=4, insertwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '+',
            '0', 'c', '=', '-'
        ]

        row_val = 1
        col_val = 0

        for text in button_texts:
            button = tk.Button(root, font=('Arial', 24), text=text, padx=20, pady=20, command=lambda txt=text: self.on_click_button(txt))
            button.grid(row=row_val, column=col_val)

            col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1
                
    def on_click_button(self, char):
        if char == 'c':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = 'error'
        else:
            self.expression += str(char)

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()

