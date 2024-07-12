from tkinter import *
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.geometry('480x600+500+200')
        self.root.title('TodoList')
        self.root.config(bg='#1e1e1e')
        self.root.resizable(width=False, height=False)

        self.frame = Frame(self.root, bg='#1e1e1e')
        self.frame.pack(pady=8)

        self.lb = Listbox(
            self.frame,
            width=40,
            height=20,
            font=('Courier New', 12),  # Updated font
            bd=0,
            fg='white',
            bg='#333333',
            highlightthickness=4,
            highlightcolor='#61afef',
            selectbackground='#61afef',
            activestyle="none",
        )
        self.lb.pack(side=LEFT, fill=BOTH)
        self.sb = Scrollbar(self.frame)
        self.sb.pack(side=RIGHT, fill=BOTH)

        self.lb.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.lb.yview)

        self.my_entry = Entry(
            self.root,
            font=('Times', 18),  # Updated font
            fg='white',
            bg='#333333',
            insertbackground='white',
            bd=2,
            highlightthickness=2,
            highlightcolor='#61afef',
        )
        self.my_entry.pack(pady=20, padx=20, fill=X)

        self.button_frame = Frame(self.root, bg='#1e1e1e')
        self.button_frame.pack(pady=20)

        self.addTask_btn = Button(
            self.button_frame,
            text='Add Task',
            font=('Helvetica', 14, 'bold'),  # Updated font
            bg='#61afef',
            fg='white',
            pady=10,
            command=self.newTask
        )
        self.addTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

        self.delTask_btn = Button(
            self.button_frame,
            text='Delete Task',
            font=('Helvetica', 14, 'bold'),  # Updated font
            bg='#e06c75',
            fg='white',
            pady=10,
            command=self.deleteTask
        )
        self.delTask_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

        self.exit_btn = Button(
            self.button_frame,
            text='Exit',
            font=('Helvetica', 14, 'bold'),  # Updated font
            bg='#61afef',
            fg='white',
            pady=10,
            command=self.root.quit
        )
        self.exit_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

        self.loadTasks()

    def newTask(self):
        task = self.my_entry.get()
        if task != "":
            padded_task = f"  {task}  "
            self.lb.insert(END, padded_task)
            self.saveTasks()
            self.my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter a task first.")

    def deleteTask(self):
        try:
            task_index = self.lb.curselection()[0]
            self.lb.delete(task_index)
            self.saveTasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def saveTasks(self):
        with open("tasks.txt", "w") as f:
            tasks = self.lb.get(0, END)
            for task in tasks:
                f.write(task.strip() + "\n")

    def loadTasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    padded_task = f"  {line.strip()}  "
                    self.lb.insert(END, padded_task)
        except FileNotFoundError:
            pass

root = Tk()
todo_list = TodoList(root)
root.mainloop()
