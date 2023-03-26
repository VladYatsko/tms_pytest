import mysql.connector as mysql


db = mysql.connect(host="localhost",
                   user="root",
                   passwd="Bristleback123!",
                   database="test_db")

cursor = db.cursor()
cursor.execute("SELECT ord_no, ord_date, purch_amt FROM orders "
               "WHERE salesman_id = 5002")
print(cursor.fetchall())
cursor.execute("SELECT DISTINCT salesman_id FROM orders")
print(cursor.fetchall())
cursor.execute("SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders")
print(cursor.fetchall())
cursor.execute("SELECT * FROM orders "
               "WHERE ord_no BETWEEN 70001 AND 70007 "
               "ORDER BY ord_no")
print(cursor.fetchall())
db.close()
