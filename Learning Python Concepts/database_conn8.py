import sqlite3
import traceback
conn = None
cur = None
try:
	conn = sqlite3.connect("d:/pythonProject/DBpython/library.db")
	print("Connection is Done successfully!")

	cur = conn.cursor()
	cur.execute("select bookname,bookprice from allbooks")
	allrow = cur.fetchall()
	a = totalrow = allrow
	#print(totalrow)
	choice = int(input(f"Enter a number bitween 1 to {len(totalrow)}:"))
	#recnum = int(input("Enter the record number(1 to " + str(len(totalrow)) + "):"))
	if choice<len(a):
		i = 1
		for my in allrow:
			if i == choice:
				print(my)
			i+=1

	else:
		print(f"Rong input!....input should be in 1 to {totalrow}..")
except sqlite3.DatabaseError as ex:
	print(ex)
	print(traceback.format_exc())

finally:
	if cur is not None:
		cur.close()
		print("curser is closed...")
	if conn is not None:
		conn.close()
		print("connection is coosed!")
