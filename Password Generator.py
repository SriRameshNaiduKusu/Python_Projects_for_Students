import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())

    if password_length < 8:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy the generated password to clipboard
def copy_password():
    generated_password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()

# Function to regenerate a new random password
def regenerate_password():
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")  # Default password length
    generate_password()

# Create GUI
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=10)
length_entry.pack()
length_entry.insert(0, "12")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack()

regenerate_button = tk.Button(root, text="Regenerate Password", command=regenerate_password)
regenerate_button.pack()

root.mainloop()
