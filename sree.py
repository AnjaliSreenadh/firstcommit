import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server's hostname or IP address
    user="sree",  # Replace with your MySQL username
    password="10121985",  # Replace with your MySQL password
    database="dtb"  # Replace with your MySQL database name
)

mycursor = mydb.cursor()
# Create a table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Insert data
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

# Select data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

# Update data
sql = "UPDATE customers SET address = 'Mountain 21' WHERE name = 'John'"
mycursor.execute(sql)
mydb.commit()

# Delete data
sql = "DELETE FROM customers WHERE name = 'John'"
mycursor.execute(sql)
mydb.commit()
