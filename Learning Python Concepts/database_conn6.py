import sqlite3
import traceback
conn = None
cur = None
try:
    conn = sqlite3.connect("d:/pythonProject/DBpython/library.db")
    print("Connection is done successfully")
    cur = conn.cursor()
    cur.execute("select bookname, bookprice from allbooks order by bookprice desc")
    all = cur.fetchall()
    if all is not None:
        for row in all:
            item1,item2 = row
            print(item1,item2)

except(sqlite3.DatabaseError)as ex:
    print(ex)
    print("python error msg is:\n",traceback.format_exc())
finally:
    if(cur is not None):
        cur.close()
    if conn is not None:
        conn.close()