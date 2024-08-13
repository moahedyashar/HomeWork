import tkinter as tk 

class ToDOApp:
    def __init__(self, root):
        self.root = root 
        self.root.title('to do app')

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady = 10)

        self.listbox = tk.Listbox(self.root, height=10, width=50, bg='white', fg='black', selectbackground='grey')
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(pady=10)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, font=('Arial', 12))
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text='Add Task', width=48, command=self.add_task)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(self.root, text='remove task', width=48, command=self.remove_task)
        self.remove_button.pack(pady=10)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            pass

root = tk.Tk()
app = ToDOApp(root)
root.mainloop()
        

