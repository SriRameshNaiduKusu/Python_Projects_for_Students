import tkinter as tk
from tkinter import messagebox
import pyshorteners
import clipboard

def shorten_url():
    original_url = url_entry.get()

    # Initialize a URL shortener
    s = pyshorteners.Shortener()

    try:
        # Shorten the URL
        short_url = s.tinyurl.short(original_url)
        result_label.config(text=f"Shortened URL: {short_url}")
        copy_button.config(state=tk.NORMAL)  # Enable the copy button after shortening
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def copy_shortened_url():
    shortened_url = result_label.cget("text").split(": ")[1]
    clipboard.copy(shortened_url)


# Create GUI
root = tk.Tk()
root.title("URL Shortener")

url_label = tk.Label(root, text="Enter the URL:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

copy_button = tk.Button(root, text="Copy Shortened URL", command=copy_shortened_url, state=tk.DISABLED)
copy_button.pack()

root.mainloop()
