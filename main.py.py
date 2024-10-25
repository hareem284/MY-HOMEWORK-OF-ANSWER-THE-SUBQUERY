#I LITTERALY DO NOT KNOW WHY MY CCODE IS NOT WORKING BUT WHEN I CHECK IT LOOKS ABSOULUTLY CORRECT TO ME


#importing sqlite3
import sqlite3
#importing pandas
import pandas as pd
#connecting with database file
connectingdatabase=sqlite3.connect("basketball.sqlite")
print("connection is established with the database file")
#reading database file
reading=pd.read_sql("SELECT * FROM Team;",connectingdatabase)
print(reading.info())
readingattributes=pd.read_sql("SELECT * FROM Team_Attributes;",connectingdatabase)
print(readingattributes.info())
checkingstatenewyork=pd.read_sql("SELECT FROM Team WHERE state LIKE "%NEWYORK%";",connectingdatabase)
print(checkingstatenewyork)