import tkinter as tk
class CounterApp:
    def __init__(self, master):
        self.master = master
        master.title('counter app')

        self.counter = 0 

        self.label = tk.Label(master, text=str(self.counter), font=("Arial", 25))
        self.label.pack(pady=10)

        self.increament_button = tk.Button(master, text='increament', command=self.increment)
        self.increament_button.pack(pady=10)

        self.decreament_button = tk.Button(master, text='decreament', command=self.decrement)
        self.decreament_button.pack(pady=10)

    def increment(self):
        self.counter += 1
        self.label.config(text=str(self.counter))

    def decrement(self):
        self.counter -= 1
        self.label.config(text=str(self.counter))

if __name__ == '__main__':
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()


    