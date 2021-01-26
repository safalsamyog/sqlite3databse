import sqlite3
conn=sqlite3.connect("samyog.db")
cursor=conn.cursor()
#adding query
#cursor.execute("CREATE TABLE Users (id INTEGER, name TEXT ,email TEXT)")
loop=True
a=0
while loop:
    try:
        dd=int(input("enter 1 for inputing data and 2 for seeing,3 for deleting data ,4 for uptading,5 for exit... : "))
        if dd==1:
            a=int(input("enter the id number: "))
            
            b=input("enter the name: ")
            c=input("enter the email: ")
            cursor.execute("INSERT INTO Users (id,name,email) values(?,?,?)",(a,b,c))
           
        elif dd==2:
            cursor.execute("SELECT*FROM Users")
            users=cursor.fetchall()
            for row in users:
                print(row)
        elif dd==3:
            e=int(input("enter id for deleting: "))
            cursor.execute("DELETE FROM Users WHERE id=%s"%e)
            print("successfully deleted...")
        elif dd==4:
             a=int(input("enter the id number: "))
             b=input("enter the name: ")
             c=input("enter the email: ")
            #  sql_update_query = """Update Users set name = ?, email = ? where id = ?"""
            #  data = (b,c,a)
             cursor.execute("UPDATE Users SET name = ?, email = ? WHERE id = ?",(b,c,a))
            #  cursor.execute(sql_update_query, data)
        elif dd==5:
            loop=False
            

    except:
        print("error find out!!")

conn.commit()

conn.close()
#cursor.execute("INSERT INTO Users VALUES(1,'safal','safal@gmail.com')")
# a=3
# b="safal"
# c="dd"
# cursor.execute("INSERT INTO Users (id,name,email) values(?,?,?)",(a,b,c))
# conn.commit()
# conn.close()