import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;Database=WideWorldImporters;Trusted_Connection=True;')

# # Using a DSN, but providing a password as well
# cnxn = pyodbc.connect('DSN=Gowtham;PWD=gowtham')

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;Database=WideWorldImporters;UID=Test;PWD=gowtham123#@')

#Create a cursor from the connection
cursor = cnxn.cursor()

cursor.execute("select ORDERid, CUSTOMERID from SALES.ORDERS")
row = cursor.fetchone()
if row:
    print(row)