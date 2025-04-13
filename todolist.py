import tkinter as tk
from tkinter import messagebox, font

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Moja To-Do Lista")
        self.root.geometry("400x500")
        self.root.configure(bg="#f7f4ea")

        self.custom_font = font.Font(family="Helvetica", size=12)
        self.strikethrough_font = font.Font(family="Helvetica", size=12, overstrike=True)

        self.tasks_frame = tk.Frame(root, bg="#f7f4ea")
        self.tasks_frame.pack(pady=20)

        self.task_entry = tk.Entry(root, font=self.custom_font, width=30, bd=2, relief="groove")
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Dodaj zadanie ➕", command=self.add_task, bg="#a3d2ca", font=self.custom_font)
        add_button.pack()

        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Błąd", "Pole nie może być puste.")
            return

        var = tk.BooleanVar()
        cb = tk.Checkbutton(self.tasks_frame, text=task_text, variable=var,
                           onvalue=True, offvalue=False,
                           command=lambda: self.toggle_task(cb, var),
                           font=self.custom_font, bg="#f7f4ea", anchor="w")

        cb.pack(anchor="w", pady=2)
        self.tasks.append((cb, var))
        self.task_entry.delete(0, tk.END)

    def toggle_task(self, checkbox, var):
        if var.get():
            checkbox.config(fg="gray", font=self.strikethrough_font)
        else:
            checkbox.config(fg="black", font=self.custom_font)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
