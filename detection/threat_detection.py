def detect_threats(logs):
    threats = []
    keywords = ["failed", "denied", "unauthorized", "error", "invalid"]

    for log in logs:
        for word in keywords:
            if word in log.lower():
                threats.append(log)
                break

    return threats


if __name__ == "__main__":
    sample_logs = [
        "Failed login attempt",
        "User logged in successfully",
        "Unauthorized access detected",
        "System error occurred"
    ]

    print(detect_threats(sample_logs))