import csv
import sqlite3


def export_csv():

    connection = sqlite3.connect("cyberwatch.db")

    cursor = connection.cursor()


    cursor.execute("SELECT * FROM logs")

    logs = cursor.fetchall()


    with open("reports/log_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["ID", "Log"])

        writer.writerows(logs)


    connection.close()


def get_security_verdict():
    connection = sqlite3.connect("cyberwatch.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    connection.close()

    threat_count = 0
    for log in logs:
        if "failed" in str(log).lower() or "unauthorized" in str(log).lower():
            threat_count += 1

    if threat_count == 0:
        print("✅ All Clear — No suspicious activity detected!")
    elif threat_count <= 5:
        print("⚠️ Minor Alerts —", threat_count, "events need review.")
    else:
        print("🚨 High Alert —", threat_count, "suspicious activities detected!")
if __name__ == "__main__":

    export_csv()
    get_security_verdict()