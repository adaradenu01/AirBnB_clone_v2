#!/usr/bin/python3

import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user="root", passwd="gbenga", db="HBNB_PROJECT")

# Create a cursor object
cursor = db.cursor()

# Get the number of current records in the `states` table
cursor.execute("SELECT COUNT(*) FROM states")
before_count = cursor.fetchone()[0]

# Run the console command to add a new state to the `states` table
# (Assuming you have a function to execute console commands)
#execute_console_command("create State name='California'")

# Get the number of current records in the `states` table again
cursor.execute("SELECT COUNT(*) FROM states")
after_count = cursor.fetchone()[0]

# Assert that the difference between the before_count and after_count is 1
assert (after_count - before_count) == 1, "Failed to add new state to the `states` table"

# Close the database connection
db.close()
