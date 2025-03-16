import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  # For copying to clipboard


class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("400x400")  # Adjusted size for complexity options
        self.root.configure(bg="#f0f0f0")  # Background color

        # Title Label
        self.title_label = tk.Label(self.root, text="Secure Password Generator", font=("Arial", 14, "bold"),
                                    bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        # Password Length
        self.length_label = tk.Label(self.root, text="Password Length:", font=("Arial", 12), bg="#f0f0f0")
        self.length_label.pack()
        self.length_entry = tk.Entry(self.root, font=("Arial", 12), width=10)
        self.length_entry.pack(pady=5)

        # Password Complexity
        self.complexity_label = tk.Label(self.root, text="Password Complexity:", font=("Arial", 12), bg="#f0f0f0")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Low")  # Default selection

        self.complexity_option = tk.OptionMenu(self.root, self.complexity_var, "Low", "Medium", "High")
        self.complexity_option.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(self.root, text="Generate Password", font=("Arial", 12),
                                         command=self.generate_password, bg="#4CAF50", fg="white")
        self.generate_button.pack(pady=10)

        # Password Display
        self.password_label = tk.Label(self.root, text="Generated Password:", font=("Arial", 12), bg="#f0f0f0")
        self.password_label.pack()
        self.password_display = tk.Entry(self.root, font=("Arial", 12, "bold"), bg="white", fg="blue", width=30,
                                         justify="center", state='readonly')
        self.password_display.pack(pady=5)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", font=("Arial", 12),
                                     command=self.copy_password, bg="#008CBA", fg="white")
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length should be at least 8 characters.")
                return

            complexity = self.complexity_var.get()

            if complexity == "Low":
                characters = string.ascii_lowercase
            elif complexity == "Medium":
                characters = string.ascii_letters
            else:
                characters = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")

    def copy_password(self):
        password = self.password_display.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
