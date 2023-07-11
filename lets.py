#!/usr/bin/python3

import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user="root", passwd="gbenga", db="HBNB_PROJECT")

#cursor = db.cursor()
#cursor.execute("CREATE TABLE states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# Get the number of current records in the `states` table
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM states")
after_count = cursor.fetchone()[0]
db.close()
