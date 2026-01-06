import sqlite3

## it is required to communicate between database and python file

## Here we will use few functions

##1. connect(): it is presnt in sqlite3 module, which helps to establish the connection between python filr and database
##2. Cursor(): it is a function which helps the contro to point particular database
##3. execute(): it is a function which helps to execute the quarries
##4. commit(): it is a function which helps to save the changes we made
##5. close(): it is a function which helps to break the connection between python filr and database

################################################################################

## Inserting the data into database

# import sqlite3
# var = sqlite3.connect('Employee.db')
# var1 = var.cursor()
# var1.execute('create table EMP_TABLE(E_Name char , EMP_ID char)')
# var1.execute('insert into EMP_TABLE values("A", "123")')
# var1.execute('insert into EMP_TABLE values("B", "124")')
# var1.execute('insert into EMP_TABLE values("C", "125")')
# var1.execute('insert into EMP_TABLE values("D", "126")')
# var1.execute('insert into EMP_TABLE values("E", "127")')
# var.commit()
# var.close()

## Extraction

# var = sqlite3.connect('Employee.db')
# var1 = var.cursor()
# var1.execute('select * from EMP_TABLE where E_name = "B"')
# res = var1.fetchall()
# print(res)
# var.commit()
# var.close()























