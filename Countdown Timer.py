import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_left = tk.StringVar()
        self.time_left.set("00:00")

        self.is_running = False
        self.start_time = 0
        self.end_time = 0

        self.label = tk.Label(root, textvariable=self.time_left, font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.time_entry = tk.Entry(root, width=10)
        self.time_entry.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.end_time = self.start_time + self.get_time_seconds()

            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)

    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            self.pause_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.time_left.set("00:00")

    def get_time_seconds(self):
        try:
            minutes = int(self.time_entry.get())
            return minutes * 60
        except ValueError:
            return 0

    def update_timer(self):
        if self.is_running:
            current_time = time.time()
            time_left = self.end_time - current_time

            if time_left <= 0:
                self.is_running = False
                self.pause_button.config(state=tk.DISABLED)
                self.start_button.config(state=tk.NORMAL)
                self.reset_button.config(state=tk.NORMAL)
                self.time_left.set("00:00")
            else:
                minutes = int(time_left // 60)
                seconds = int(time_left % 60)
                time_str = f"{minutes:02d}:{seconds:02d}"
                self.time_left.set(time_str)
                self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()
