def detect_threats(logs):
    threats = []

    high_keywords    = ["unauthorized", "denied"]
    medium_keywords  = ["failed", "invalid"]
    low_keywords     = ["error"]

    for log in logs:
        log_lower = log.lower()

        if any(word in log_lower for word in high_keywords):
            threats.append({"log": log, "severity": "HIGH"})
        elif any(word in log_lower for word in medium_keywords):
            threats.append({"log": log, "severity": "MEDIUM"})
        elif any(word in log_lower for word in low_keywords):
            threats.append({"log": log, "severity": "LOW"})

    return threats


if __name__ == "__main__":
    sample_logs = [
        "Failed login attempt",
        "User logged in successfully",
        "Unauthorized access detected",
        "System error occurred"
    ]

    for threat in detect_threats(sample_logs):
        print(f"[{threat['severity']}] {threat['log']}")