import sqlite3
from sqlite3 import Error
from datetime import date
conn=sqlite3.connect('mytable.db')
curs=conn.cursor()
instru="""SELECT *   FROM selling_register;
                            
        """
data=curs.execute(instru) 
print(data.fetchall())

conn.commit()
conn.close()
       



 

