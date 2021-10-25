import sqlite3
import traceback
conn = None
try:
    conn = sqlite3.connect("d:/pythonProject/DBpython/library.db")
    print("Connection is done successfully")
    cur = conn.cursor()
    cur.execute("select bookname,bookprice from allbooks")

    for x,y in cur:
        print(x,y)

except(sqlite3.DatabaseError)as ex:
    print(ex)
    print("python error msg is:\n",traceback.format_exc())
finally:
    if(conn is not None):
        conn.close()