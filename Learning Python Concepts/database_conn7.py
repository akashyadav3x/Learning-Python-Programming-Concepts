import sqlite3
conn=None
try:
	conn=sqlite3.connect("d:/pythonProject/DBpython/library.db")
	print("Connected successfully to the DB")
	cur=conn.cursor()
	cur.execute("Select bookname,bookprice from allbooks order by bookprice desc")
	booklist=cur.fetchall()
	recnum=int(input("Enter the record number(1 to "+str(len(booklist))+"):"))

	if recnum <1 or recnum>len(booklist):
		print("Record number should be between 1 to "+str(len(booklist)))
	else:
		row=booklist[recnum-1]
		print(row[0],row[1])

except (sqlite3.DatabaseError)as ex:
	print("Error in connecting to Sqlite:",ex)
finally:
		if conn is not None:
			conn.close()
			print("Disconnected successfully from the DB")
