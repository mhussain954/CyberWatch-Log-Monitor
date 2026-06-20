import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from parser.log_parser import parse_log
from detection.threat_detection import detect_threats

class CyberWatchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberWatch – Security Monitoring Dashboard")
        self.root.geometry("1100x650")
        self.root.configure(bg="#0f172a")

        self.logs = []
        self.threats = []

        self.create_menu()
        self.create_header()
        self.create_body()
        self.create_status_bar()

    # ---------- MENU ----------
    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load Log File", command=self.load_logs)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    # ---------- HEADER ----------
    def create_header(self):
        header = tk.Label(
            self.root,
            text="CyberWatch – Log Monitoring & Threat Detection",
            bg="#020617",
            fg="white",
            font=("Segoe UI", 20, "bold"),
            pady=15
        )
        header.pack(fill="x")

    # ---------- BODY ----------
    def create_body(self):
        body = tk.Frame(self.root, bg="#0f172a")
        body.pack(fill="both", expand=True)

        # Left Panel (Stats)
        left = tk.Frame(body, width=250, bg="#020617")
        left.pack(side="left", fill="y")

        self.total_logs_label = tk.Label(
            left, text="Total Logs\n0", fg="#38bdf8",
            bg="#020617", font=("Segoe UI", 16, "bold"), pady=20
        )
        self.total_logs_label.pack(fill="x")

        self.threats_label = tk.Label(
            left, text="Threats Detected\n0", fg="#ef4444",
            bg="#020617", font=("Segoe UI", 16, "bold"), pady=20
        )
        self.threats_label.pack(fill="x")

        load_btn = tk.Button(
            left, text="Load Log File",
            command=self.load_logs,
            bg="#22c55e", fg="white",
            font=("Segoe UI", 12, "bold"),
            pady=10, relief="flat"
        )
        load_btn.pack(pady=30, padx=20, fill="x")

        # Right Panel (Tabs)
        right = tk.Frame(body, bg="#0f172a")
        right.pack(side="right", fill="both", expand=True)

        self.tabs = ttk.Notebook(right)
        self.tabs.pack(fill="both", expand=True)

        self.all_logs_tab = tk.Text(self.tabs, bg="#020617", fg="#e5e7eb", font=("Consolas", 11))
        self.threats_tab = tk.Text(self.tabs, bg="#020617", fg="#ef4444", font=("Consolas", 11))

        self.tabs.add(self.all_logs_tab, text="All Logs")
        self.tabs.add(self.threats_tab, text="Threats Only")

    # ---------- STATUS ----------
    def create_status_bar(self):
        self.status = tk.Label(
            self.root, text="Status: Ready",
            bg="#020617", fg="white", anchor="w", padx=10
        )
        self.status.pack(fill="x", side="bottom")

    # ---------- LOAD LOGS ----------
    def load_logs(self):
        file_path = filedialog.askopenfilename(
            title="Select Log File",
            filetypes=[("Log files", "*.log"), ("All files", "*.*")]
        )

        if not file_path:
            return

        try:
            self.logs = parse_log(file_path)
            self.threats = detect_threats(self.logs)
            self.update_ui()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load log file:\n{e}")
            self.status.config(text=f"Status: Error loading file - {e}")

    # ---------- UPDATE UI ----------
    def update_ui(self):
        self.all_logs_tab.delete("1.0", tk.END)
        self.threats_tab.delete("1.0", tk.END)

        for log in self.logs:
            self.all_logs_tab.insert(tk.END, log + "\n")

        for threat in self.threats:
            ip = threat.get("ip", "N/A")
            severity = threat.get("severity", "UNKNOWN")
            log = threat.get("log", "")
            detected_at = threat.get("detected_at", "")

            threat_text = (
                f"[{severity}] "
                f"{log} "
                f"| IP: {ip} "
                f"| Detected: {detected_at}\n"
            )

            self.threats_tab.insert(tk.END, threat_text)

        self.total_logs_label.config(text=f"Total Logs\n{len(self.logs)}")
        self.threats_label.config(text=f"Threats Detected\n{len(self.threats)}")

        self.status.config(text="Status: Log file loaded successfully")


def start_dashboard():
    root = tk.Tk()
    app = CyberWatchGUI(root)
    root.mainloop()