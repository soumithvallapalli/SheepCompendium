import pymysql

# Connect to the base MySQL server
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='pantherfan18'
)

try:
    with connection.cursor() as cursor:
        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS sandwich_maker_api;")
        print("Database created successfully! You are good to go.")
finally:
    connection.close()