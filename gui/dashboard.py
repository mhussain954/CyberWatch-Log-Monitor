import tkinter as tk
from tkinter import filedialog
from parser.log_parser import parse_log

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberWatch Dashboard")
        self.root.geometry("900x600")

        self.label = tk.Label(root, text="CyberWatch Log Monitor", font=("Arial", 18))
        self.label.pack(pady=10)

        self.btn = tk.Button(root, text="Load Log File", command=self.load_file)
        self.btn.pack(pady=10)

        self.text = tk.Text(root, height=25, width=100)
        self.text.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            logs = parse_log(file_path)
            self.text.delete("1.0", tk.END)
            for log in logs:
                self.text.insert(tk.END, log + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()