import sqlite3
import traceback
conn=None
try:
    conn = sqlite3.connect("D:/DBpython/library.db")
    print("Connection done successfully")
    cr = conn.cursor()
    cr.execute("select bookname,bookprice from allbooks")
    for x in cr:
        print(x)

except(sqlite3.DatabaseError):
    print("Connection is not possible")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()