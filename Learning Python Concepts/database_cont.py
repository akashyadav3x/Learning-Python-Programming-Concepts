import sqlite3
import traceback
conn=None
try:
    conn= sqlite3.connect("d:/DBpython/mydatabase.db")
    print("Connection done successfully")
    cr = conn.cursor()
    cr.execute("select Name,age,salary from Employee")
    for x in cr:
        print(x)

except(sqlite3.DatabaseError):
    print("Could not connect to DB")
    print(traceback.format_exc())

finally:
    if conn is not None:
        conn.close()
        print("Connection close successfully!")