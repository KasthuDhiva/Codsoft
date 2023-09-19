import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("400x400")
    root.configure(bg='#FFCDD2')  # Set the background color

    frame = tk.Frame(root, bg='#FFCDD2')  # Set the background color
    frame.pack(pady=10)

    entry = tk.Entry(frame, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT, ipadx=20)

    add_button = tk.Button(frame, text="Add Task", command=add_task, bg='#81C784', font=("Helvetica", 10))
    add_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(frame, text="Delete Task", command=delete_task, bg='#FF8A65', font=("Helvetica", 10))
    delete_button.pack(side=tk.LEFT)

    listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="yellow")
    listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
