from sqlite3 import connect

from cx_Oracle import connect
from traceback import *

class Test_Oracle:
        conn = None
        try:
            conn = connect("mojo/mojo@127.0.0.1/xe")
            print("Connection done successfully")
            print("DB Version ", conn.version)
            print("User Name ", conn.username)

        except DatabaseError:
            print("Connection failed!!!")
            print(traceback.format_exc())

        finally:
            if conn is not None:
                conn.close()
                print("DataBase close successfully")


if __name__ == '__main__':
    Test_Oracle()