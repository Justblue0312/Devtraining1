import csv
import pandas as pd
from sqlalchemy import create_engine
from mysql.connector import Error
import mysql.connector


df = pd.read_csv('customer.csv')
# print(df.to_string())

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine('mysql+mysqldb://root:@localhost/ex2')
conn = mysql.connector.connect(
    user='root', password='', host='localhost', database='ex2')
cursor = conn.cursor()

try:
    if conn.is_connected():
        cursor.execute("""CREATE TABLE customer( customerid int not null primary key,
    firstname varchar(255),lastname varchar(255), companyname varchar(255),
    billingaddress1 varchar(255),billingaddress2 varchar(255),
    city varchar(255),state varchar(255),postalcode varchar(255),country varchar(255),
    phonenumber varchar(255),emailaddress varchar(255),createddate varchar(255));""")
except mysql.connector.Error as error:
    print("Failed creating database: {}".format(error))
    exit(1)

df.to_sql(name='customer', con=engine, if_exists='replace')
conn.commit()
cursor.close()
conn.close()
