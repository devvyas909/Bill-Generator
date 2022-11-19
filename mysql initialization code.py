#COMPUTER PROJECT
#Initialization code
import mysql.connector as sqLtor
mycon=sqLtor.connect(host="localhost",user="root",passwd="password123")
cursor=mycon.cursor()
cursor.execute("CREATE DATABASE billing_system")
print("Database created")
cursor.execute("USE billing_system")

#Creating table
cursor.execute("CREATE TABLE grocery_store(Srno int(5),Item_name varchar(20),Item_code varchar(20),Brand varchar(20),Price int(5))")
print("Table is created")

#Inserting values
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(1, 'Kitkat       ',860,'Nestle      ',40 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(2, 'Milk         ',243,'Amul        ',70 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(3, 'Bread        ',308,'Lakshmi     ',90 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(4, 'Eggs         ',700,'Motherdairy ',60 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(5, 'Dairymilk    ',767,'Cadbury     ',50 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(6, 'Chips        ',555,'Frito lay   ',20 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(7, 'Nutella      ',876,'Ferrero     ',200))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(8, 'Bisleri      ',778,'Aqua        ',10 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(9, 'Oreo         ',443,'Cadbury     ',65 ))
cursor.execute("INSERT INTO grocery_store(Srno,Item_name,Item_code,Brand,Price) VALUES('{}','{}','{}','{}','{}')".format(10,'Orange  juice',981,'Tropicana   ',115))
mycon.commit()

cursor.close()
mycon.close()
print("The initialization was successful")

     




