import wikipedia
import tkinter as tk
from tkinter import messagebox

def get_random_article():
    return wikipedia.random()

def show_article():
    article_title = get_random_article()
    result_label.config(text=f"Random Article: {article_title}")

def read_article():
    article_title = result_label.cget("text").split(": ")[1]
    try:
        article_content = wikipedia.summary(article_title)
        article_text.delete(1.0, tk.END)
        article_text.insert(tk.END, article_content)
    except wikipedia.exceptions.DisambiguationError as e:
        messagebox.showinfo("Error", f"There are multiple options for '{e.title}'. Please refine your search.")
    except wikipedia.exceptions.HTTPTimeoutError:
        messagebox.showinfo("Error", "Timeout error. Please try again later.")

# Create GUI
root = tk.Tk()
root.title("Random Wikipedia Article Viewer")

show_button = tk.Button(root, text="Show Random Article", command=show_article)
show_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

read_button = tk.Button(root, text="Read Article", command=read_article)
read_button.pack(pady=10)

article_text = tk.Text(root, width=80, height=20)
article_text.pack()

root.mainloop()
