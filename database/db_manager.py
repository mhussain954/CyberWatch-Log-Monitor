import sqlite3


def save_logs(logs):

    connection = sqlite3.connect("cyberwatch.db")

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log TEXT
    )
    """)


    for log in logs:

        cursor.execute(
            "INSERT INTO logs(log) VALUES (?)",
            (log,)
        )


    connection.commit()

    connection.close()



def get_logs():

    connection = sqlite3.connect("cyberwatch.db")

    cursor = connection.cursor()


    cursor.execute("SELECT * FROM logs")

    data = cursor.fetchall()


    connection.close()

    return data