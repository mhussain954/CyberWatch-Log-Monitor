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



if __name__ == "__main__":

    export_csv()