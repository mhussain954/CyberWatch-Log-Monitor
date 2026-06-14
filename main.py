# main.py
# CyberWatch Log Monitoring Tool
# Project Leader: Muhammad Hussain

from parser.log_parser import parse_log
from detection.threat_detection import detect_threats
from database.db_manager import save_logs
from gui.dashboard import start_dashboard

def main():
    print("=== CyberWatch Log Monitoring Tool ===")

    log_file = "parser/sample_logs/auth.log"

    print("[+] Loading logs...")
    logs = parse_log(log_file)

    if not logs:
        print("No logs found.")
        return

    print(f"[+] {len(logs)} logs loaded")

    print("[+] Detecting threats...")
    threats = detect_threats(logs)

    if threats:
        print("[!] Threats detected:")
        for threat in threats:
            print(" -", threat)
    else:
        print("[+] No threats detected")

    print("[+] Saving logs to database...")
    save_logs(logs)

    print("[+] Process completed successfully")

    # 🔹 START GUI AFTER BACKEND
    start_dashboard()

if __name__ == "__main__":
    main()