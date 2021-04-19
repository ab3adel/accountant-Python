import sqlite3
conn = sqlite3.connect('goodlife.db')
curs=conn.cursor()
curs.execute('DELETE FROM safe ;')
conn.commit()

conn.close()    