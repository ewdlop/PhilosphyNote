import json
import datetime
import tkinter as tk
from tkinter import messagebox


class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Famous Scientists' Birthdays")
        self.root.geometry("450x450")

        # Load scientists' data
        self.scientists = self.load_scientists()

        # UI Elements
        tk.Label(root, text="Famous Scientists' Birthdays", font=("Arial", 14, "bold")).pack(pady=10)

        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.pack(pady=5)

        tk.Button(root, text="Search", command=self.search_birthday).pack(pady=5)
        tk.Button(root, text="Show Today's Birthdays", command=self.show_todays_birthdays).pack(pady=5)
        tk.Button(root, text="Show All Birthdays", command=self.show_all_birthdays).pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400)
        self.result_label.pack(pady=10)

    def load_scientists(self):
        """Load scientists' data from JSON file."""
        try:
            with open("scientists_with_family.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "scientists_with_family.json file not found!")
            return []

    def search_birthday(self):
        """Search for a scientist's birthday and display family name."""
        name = self.search_entry.get().strip().lower()
        for scientist in self.scientists:
            if name in scientist["name"].lower():
                self.result_label.config(
                    text=f"{scientist['name']} was born on {scientist['birth_date']}.\n"
                         f"Family (Tree of Life): {scientist['family']}"
                )
                return
        self.result_label.config(text="Scientist not found!")

    def show_todays_birthdays(self):
        """Show scientists born on today's date."""
        today = datetime.date.today().strftime("%m-%d")
        birthdays = [
            f"{s['name']} ({s['family']})" for s in self.scientists if s["birth_date"][5:] == today
        ]

        if birthdays:
            self.result_label.config(text="Today's famous birthdays:\n" + "\n".join(birthdays))
        else:
            self.result_label.config(text="No famous scientist birthdays today.")

    def show_all_birthdays(self):
        """Show all scientists' birthdays with family classification."""
        all_birthdays = "\n".join(
            [f"{s['name']} ({s['family']}) - {s['birth_date']}" for s in self.scientists]
        )
        self.result_label.config(text=all_birthdays)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayApp(root)
    root.mainloop()
