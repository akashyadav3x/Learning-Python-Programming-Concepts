import sqlite3
import traceback
conn = None
try:
    conn = sqlite3.connect("d:/pythonProject/DBpython/library.db")
    print("Connection is done successfully")
    cur = conn.cursor()
    cur.execute("select bookname,bookprice from allbooks")

    for x in cur:
        print(x)

except(sqlite3.DatabaseError):
    print("Connection is not possible")
    print("python error msg is:",traceback.format_exc())
finally:
    if(conn is not None):
        conn.close()