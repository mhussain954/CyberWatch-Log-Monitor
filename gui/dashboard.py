import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from parser.log_parser import parse_log
from detection.threat_detection import detect_threats
from database.db_manager import save_logs

class CyberWatchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberWatch – Security Monitoring Dashboard")
        self.root.geometry("1100x650")
        self.root.configure(bg="#0b0f19")

        self.logs = []
        self.threats = []

        self.setup_styles()

        self.create_menu()
        self.create_header()
        self.create_body()
        self.create_status_bar()

    def setup_styles(self):
        """Configures modern styles for ttk components like Notebook tabs."""
        self.style = ttk.Style()
        self.style.theme_use("default")
        
        # Custom Notebook Tab Styling
        self.style.configure("TNotebook", background="#0b0f19", borderwidth=0)
        self.style.configure("TNotebook.Tab",
                             background="#1e293b",
                             foreground="#94a3b8",
                             font=("Segoe UI", 10, "bold"),
                             padding=[20, 8],
                             borderwidth=0)
        self.style.map("TNotebook.Tab",
                       background=[("selected", "#0ea5e9")],
                       foreground=[("selected", "#ffffff")])

    # ---------- MENU ----------
    def create_menu(self):
        menubar = tk.Menu(self.root, bg="#1e293b", fg="white", activebackground="#0ea5e9")
        file_menu = tk.Menu(menubar, tearoff=0, bg="#1e293b", fg="white", activebackground="#0ea5e9")
        file_menu.add_command(label="📥 Load Log File", command=self.load_logs)
        file_menu.add_separator()
        file_menu.add_command(label="❌ Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    # ---------- HEADER ----------
    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#020617", bd=0)
        header_frame.pack(fill="x")

        header = tk.Label(
            header_frame,
            text="🛡️ CYBERWATCH LOG MONITORING SYSTEM",
            bg="#020617",
            fg="#f8fafc",
            font=("Segoe UI", 16, "bold"),
            pady=18,
            padx=20,
            anchor="w"
        )
        header.pack(side="left")
        
        # Decorative branding subtitle
        subtitle = tk.Label(
            header_frame,
            text="SECURE AUDITING & ANALYSIS Engine v1.0",
            bg="#020617",
            fg="#38bdf8",
            font=("Segoe UI", 9, "bold"),
            padx=20
        )
        subtitle.pack(side="right", pady=22)

    # ---------- BODY ----------
    def create_body(self):
        # Outer containment frame supporting seamless window resizing
        body = tk.Frame(self.root, bg="#0b0f19")
        body.pack(fill="both", expand=True, padx=15, pady=15)
        
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        # ------------------ LEFT SIDEBAR (Metrics Dashboard) ------------------
        left_panel = tk.Frame(body, width=280, bg="#0f172a", relief="flat")
        left_panel.grid(row=0, column=0, sticky="nsw", padx=(0, 15))
        left_panel.pack_propagate(False)

        # Stat Card 1: Total Events
        self.total_logs_label = tk.Label(
            left_panel, 
            text="TOTAL LOG EVENTS\n0", 
            fg="#38bdf8",
            bg="#1e293b", 
            font=("Segoe UI", 12, "bold"), 
            pady=20,
            bd=0,
            relief="flat"
        )
        self.total_logs_label.pack(fill="x", padx=15, pady=(20, 10))

        # Stat Card 2: Threats Detected
        self.threats_label = tk.Label(
            left_panel, 
            text="THREATS DETECTED\n0", 
            fg="#f87171",
            bg="#1e293b", 
            font=("Segoe UI", 12, "bold"), 
            pady=20,
            bd=0,
            relief="flat"
        )
        self.threats_label.pack(fill="x", padx=15, pady=10)

        # High-Contrast Call-to-Action Action Button
        load_btn = tk.Button(
            left_panel, 
            text="📁 Load Source Log",
            command=self.load_logs,
            bg="#0ea5e9", 
            fg="white",
            activebackground="#0284c7",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            pady=12, 
            relief="flat",
            cursor="hand2"
        )
        load_btn.pack(side="bottom", pady=25, padx=15, fill="x")

        # ------------------ RIGHT PANEL (Interactive Log Viewer) ------------------
        right_panel = tk.Frame(body, bg="#0b0f19")
        right_panel.grid(row=0, column=1, sticky="nsew")

        self.tabs = ttk.Notebook(right_panel)
        self.tabs.pack(fill="both", expand=True)

        # All Logs Display Terminal Window
        self.all_logs_tab = tk.Text(
            self.tabs, 
            bg="#020617", 
            fg="#cbd5e1", 
            font=("Consolas", 10),
            padx=15,
            pady=15,
            bd=0,
            insertbackground="white" # Readable cursor text alignment
        )
        
        # Flagged Threats Terminal Window
        self.threats_tab = tk.Text(
            self.tabs, 
            bg="#020617", 
            fg="#f87171", 
            font=("Consolas", 10),
            padx=15,
            pady=15,
            bd=0,
            insertbackground="white"
        )

        self.tabs.add(self.all_logs_tab, text="📜 ALL EVENT LOGS")
        self.tabs.add(self.threats_tab, text="🚨 CRITICAL ALERTS")

    # ---------- STATUS ----------
    def create_status_bar(self):
        self.status = tk.Label(
            self.root, text="Status: Ready",
            bg="#020617", fg="white", anchor="w", padx=10
        )
        self.status.pack(fill="x", side="bottom")

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
            
            # Sync to SQLite when loaded through GUI
            save_logs(self.logs) 
            
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