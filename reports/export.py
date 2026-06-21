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

   # Replace the loop inside get_security_verdict() in export.py with this:
    threat_count = 0
    for row in logs:
        log_text = row[1].lower()  # Access the text column safely from the tuple
        if "failed" in log_text or "unauthorized" in log_text:
            threat_count += 1

    if threat_count == 0:
        print("✅ All Clear — No suspicious activity detected!")
    elif threat_count == 1:
        print("⚠️ Minor Alert — 1 event needs review.")
    elif threat_count <= 5:
        print(f"⚠️ Minor Alerts — {threat_count} events need review.")
    else:
        print(f"🚨 High Alert — {threat_count} suspicious activities detected!")
if __name__ == "__main__":

    export_csv()
    get_security_verdict()