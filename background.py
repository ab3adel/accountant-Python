import sqlite3
conn = sqlite3.connect('mytable.db')
curs=conn.cursor()
instru="""SELECT * FROM selling_register  
 ;"""
data=curs.execute(instru)
check=data.fetchall()
print(check)
conn.close()           

