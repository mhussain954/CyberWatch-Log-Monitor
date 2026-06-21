import sqlite3

def save_logs(logs):
    connection = sqlite3.connect("cyberwatch.db")
    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log TEXT UNIQUE
    )
    """)

    for log in logs:
        try:
            
            cursor.execute(
                "INSERT OR IGNORE INTO logs(log) VALUES (?)",
                (log,)
            )
        except sqlite3.Error as e:
            print(f"[-] Database insertion error: {e}")

    connection.commit()
    connection.close()



def get_logs():

    connection = sqlite3.connect("cyberwatch.db")

    cursor = connection.cursor()


    cursor.execute("SELECT * FROM logs")

    data = cursor.fetchall()


    connection.close()

    return data