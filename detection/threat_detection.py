# detection/threat_detection.py
# Contributor: Huraira
# Improvement: Added IP extraction and timestamp tagging

import re
from datetime import datetime

HIGH_KEYWORDS   = ["unauthorized", "denied"]
MEDIUM_KEYWORDS = ["failed", "invalid"]
LOW_KEYWORDS    = ["error"]

IP_PATTERN = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

def detect_threats(logs):
    threats = []
    for log in logs:
        log_lower = log.lower()
        if any(word in log_lower for word in HIGH_KEYWORDS):
            severity = "HIGH"
        elif any(word in log_lower for word in MEDIUM_KEYWORDS):
            severity = "MEDIUM"
        elif any(word in log_lower for word in LOW_KEYWORDS):
            severity = "LOW"
        else:
            continue

        ip_match = IP_PATTERN.search(log)
        threats.append({
            "log":         log,
            "severity":    severity,
            "ip":          ip_match.group() if ip_match else None,
            "detected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
    return threats


if __name__ == "__main__":
    sample_logs = [
        "Failed login attempt from 192.168.1.15",
        "User logged in successfully",
        "Unauthorized access detected from 10.0.0.5",
        "System error occurred",
    ]
    for threat in detect_threats(sample_logs):
        ip_info = f" | IP: {threat['ip']}" if threat['ip'] else ""
        print(f"[{threat['severity']}] {threat['log']}{ip_info}")