import tkinter as tk
from tkinter import ttk, messagebox
import os

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("650x400")

        self.tasks = []
        self.current_id = 1

        self.create_widgets()
        self.charger_taches()  # Charger les tâches au démarrage
    def create_widgets(self):
        self.task_label = ttk.Label(self.root, text="Tâche:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_entry = ttk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        self.urgent_var = tk.BooleanVar()
        self.urgent_check = ttk.Checkbutton(self.root, text="Urgent", variable=self.urgent_var)
        self.urgent_check.grid(row=0, column=2, padx=10, pady=10)

        self.add_button = ttk.Button(self.root, text="Ajouter", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=10, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Tâche", "Urgent"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tâche", text="Tâche")
        self.tree.heading("Urgent", text="Urgent")
        self.tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.modify_button = ttk.Button(self.root, text="Modifier", command=self.modify_task)
        self.modify_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = ttk.Button(self.root, text="Supprimer", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.save_button = ttk.Button(self.root, text="Sauvegarder", command=self.sauvegarder_taches)
        self.save_button.grid(row=2, column=2, padx=10, pady=10)

        self.load_button = ttk.Button(self.root, text="Charger", command=self.charger_taches)
        self.load_button.grid(row=2, column=3, padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            urgent = self.urgent_var.get()
            self.tasks.append({"id": self.current_id, "task": task_text, "urgent": urgent})
            self.tree.insert("", "end", values=(self.current_id, task_text, "Oui" if urgent else "Non"))
            self.current_id += 1
            self.task_entry.delete(0, tk.END)
            self.urgent_var.set(False)
        else:
            messagebox.showwarning("Attention", "Veuillez entrer une tâche.")

    def modify_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            item_id = item['values'][0]
            new_task_text = self.task_entry.get()
            if new_task_text:
                new_urgent = self.urgent_var.get()
                for task in self.tasks:
                    if task["id"] == item_id:
                        task["task"] = new_task_text
                        task["urgent"] = new_urgent
                        break
                self.tree.item(selected_item, values=(item_id, new_task_text, "Oui" if new_urgent else "Non"))
                self.task_entry.delete(0, tk.END)
                self.urgent_var.set(False)
            else:
                messagebox.showwarning("Attention", "Veuillez entrer une nouvelle tâche.")
        else:
            messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à modifier.")

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            item_id = item['values'][0]
            for task in self.tasks:
                if task["id"] == item_id:
                    self.tasks.remove(task)
                    break
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à supprimer.")

    def sauvegarder_taches(self):
        with open("taches.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['id']},{task['task']},{task['urgent']}\n")
        messagebox.showinfo("Information", "Tâches sauvegardées avec succès.")

    def charger_taches(self):
        if os.path.exists("taches.txt"):
            with open("taches.txt", "r") as file:
                self.tasks = []
                self.tree.delete(*self.tree.get_children())
                for line in file:
                    task_id, task_text, urgent = line.strip().split(",")
                    task_id = int(task_id)
                    urgent = urgent == 'True'
                    self.tasks.append({"id": task_id, "task": task_text, "urgent": urgent})
                    self.tree.insert("", "end", values=(task_id, task_text, "Oui" if urgent else "Non"))
                    if task_id >= self.current_id:
                        self.current_id = task_id + 1
            messagebox.showinfo("Information", "Tâches chargées avec succès.")
        else:
            messagebox.showwarning("Attention", "Aucun fichier de sauvegarde trouvé.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

