import sqlite3
conn=sqlite3.connect("datafile")
cursor=conn.cursor()
print(cursor)
cursor.execute("create table test (name text, count integer)")
cursor.execute("insert into test (name, count) values ('Bob', 1)")
cursor.execute("insert into test (name, count) values ('Jill', 15)")
result = cursor.execute("select * from test")
for row in result:
    print(row)

cursor.execute("update test set count=? where name=?", (20, "Jill"))
conn.commit()
result = cursor.execute("select * from test")

for row in result:
    print(row)
conn.close()
