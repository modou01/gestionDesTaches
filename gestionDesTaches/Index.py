import tkinter as tk
from tkinter import messagebox
import json

class TaskManager:
    def __init__(self):
        self.tasks = []  # Liste de tâches
        self.load_tasks()  # Charger les tâches depuis le fichier

    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline, "done": False})
        self.save_tasks()  # Enregistrer les tâches

    def mark_task_done(self, index):
        self.tasks[index]["done"] = True
        self.save_tasks()  # Enregistrer les tâches

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()  # Enregistrer les tâches

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

class TaskManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de tâches")

        self.task_manager = TaskManager()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.deadline_label = tk.Label(root, text="Date d'échéance:")
        self.deadline_label.pack()

        self.deadline_entry = tk.Entry(root)
        self.deadline_entry.pack()

        self.add_button = tk.Button(root, text="Ajouter", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack()

        self.mark_done_button = tk.Button(root, text="Marquer comme terminée", command=self.mark_task_done)
        self.mark_done_button.pack()

        self.delete_button = tk.Button(root, text="Supprimer", command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks_button = tk.Button(root, text="Charger les tâches", command=self.load_tasks)
        self.load_tasks_button.pack()

        self.save_tasks_button = tk.Button(root, text="Enregistrer les tâches", command=self.save_tasks)
        self.save_tasks_button.pack()

        self.load_tasks()  # Charger les tâches au démarrage de l'application
        self.update_task_listbox()  # Mettre à jour l'affichage de la liste des tâches

    def add_task(self):
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()
        self.task_manager.add_task(description, deadline)
        self.update_task_listbox()
        self.description_entry.delete(0, tk.END)  # Effacer la zone de texte
        self.deadline_entry.delete(0, tk.END)

    def mark_task_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_manager.mark_task_done(index)
            self.update_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_manager.delete_task(index)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            status = "Terminée" if task["done"] else "En cours"
            self.task_listbox.insert(tk.END, f"{task['description']} (Échéance: {task['deadline']}, Statut: {status})")

    def load_tasks(self):
        self.task_manager.load_tasks()
        self.update_task_listbox()

    def save_tasks(self):
        self.task_manager.save_tasks()
        messagebox.showinfo("Enregistrement", "Les tâches ont été enregistrées avec succès.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox
import json

class TaskManager:
    def __init__(self):
        self.tasks = []  # Liste de tâches
        self.load_tasks()  # Charger les tâches depuis le fichier

    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline, "done": False})
        self.save_tasks()  # Enregistrer les tâches

    def mark_task_done(self, index):
        self.tasks[index]["done"] = True
        self.save_tasks()  # Enregistrer les tâches

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()  # Enregistrer les tâches

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

class TaskManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de tâches")

        self.task_manager = TaskManager()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.deadline_label = tk.Label(root, text="Date d'échéance:")
        self.deadline_label.pack()

        self.deadline_entry = tk.Entry(root)
        self.deadline_entry.pack()

        self.add_button = tk.Button(root, text="Ajouter", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack()

        self.mark_done_button = tk.Button(root, text="Marquer comme terminée", command=self.mark_task_done)
        self.mark_done_button.pack()

        self.delete_button = tk.Button(root, text="Supprimer", command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks_button = tk.Button(root, text="Charger les tâches", command=self.load_tasks)
        self.load_tasks_button.pack()

        self.save_tasks_button = tk.Button(root, text="Enregistrer les tâches", command=self.save_tasks)
        self.save_tasks_button.pack()

        self.load_tasks()  # Charger les tâches au démarrage de l'application
        self.update_task_listbox()  # Mettre à jour l'affichage de la liste des tâches

    def add_task(self):
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()
        self.task_manager.add_task(description, deadline)
        self.update_task_listbox()
        self.description_entry.delete(0, tk.END)  # Effacer la zone de texte
        self.deadline_entry.delete(0, tk.END)

    def mark_task_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_manager.mark_task_done(index)
            self.update_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_manager.delete_task(index)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            status = "Terminée" if task["done"] else "En cours"
            self.task_listbox.insert(tk.END, f"{task['description']} (Échéance: {task['deadline']}, Statut: {status})")

    def load_tasks(self):
        self.task_manager.load_tasks()
        self.update_task_listbox()

    def save_tasks(self):
        self.task_manager.save_tasks()
        messagebox.showinfo("Enregistrement", "Les tâches ont été enregistrées avec succès.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()
