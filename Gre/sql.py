import sqlite3 as lite 
conn = lite.connect('107_law.db')
c = conn.cursor()
sqls  ="""Create  table law_main (url,Search_row)""" 

c.execute(sqls)

conn.commit()
conn.close()