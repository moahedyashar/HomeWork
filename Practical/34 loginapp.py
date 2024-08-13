import tkinter as tk 

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Login App')

        self.username_label = tk.Label(root, text="enter your username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(root, text="enter your password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(root)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.grid(row=2, column=1, padx=10, pady=10)

        self.label_result = tk.Label(root, text="")
        self.label_result.grid(row=3, column=1, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == 'password':
            self.label_result.config(text= "login successful", fg='green')
        else:
            self.label_result.config(text='login failed, try again', fg='red')

root = tk.Tk()
app = LoginApp(root)
root.mainloop()