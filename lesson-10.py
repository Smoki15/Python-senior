import sqlite3

connection=sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

# print(connection)
# print(cur)
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# cur.execute("INSERT INTO first_table (name) VALUES ('BueatifulSoup');")
# for i in cur.execute("SELECT rowid, name FROM first_table"):
#    print(i)
cur.execute("UPDATE first_table SET name='Danil' WHERE rowid=2;")
cur.execute("UPDATE first_table SET name='Sup' WHERE rowid=3;")
cur.execute("DELETE FROM first_table WHERE rowid=4;")
cur.execute("UPDATE first_table SET name='Ivan' WHERE rowid=5;")
connection.commit()

connection.close()