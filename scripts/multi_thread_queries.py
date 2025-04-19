import threading
import mysql.connector
import os

db_user = os.getenv("MYSQL_USER", "root")
db_password = os.getenv("MYSQL_PASSWORD", "Rambo@123")

def db_task(query):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user=db_user,
        password=db_password,
        database="project_db"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

queries = [
    "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('Calgary', '2023-06-03', 20.0, 6.0, 65.0)",
    "UPDATE ClimateData SET humidity = 70.0 WHERE location = 'Toronto'",
    "SELECT * FROM ClimateData WHERE temperature > 20"
]

threads = []
for q in queries:
    t = threading.Thread(target=db_task, args=(q,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
