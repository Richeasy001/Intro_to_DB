import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': 'IlamosiEmolewu100%',
    'host': 'localhost',
}

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Create database if it does not exist
    database_name = 'alx_book_store'
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store;")

    print(f"Database '{database_name}' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(f"Error: {err}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up and close connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()