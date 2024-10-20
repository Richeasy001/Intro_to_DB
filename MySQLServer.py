import mysql.connector

def create_database(host, user, password, database_name):
  try:
    # Connect to the MySQL server without specifying a database
    connection = mysql.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()

    # Create the database (will not fail if it already exists)
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    connection.commit()

    print(f"Database '{database_name}' created successfully!")
  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
  finally:
    if connection:
      connection.close()

if __name__ == "__main__":
  # Replace with your MySQL server details
  host = "localhost"
  user = "root"
  password = "IlamosiEmolewu100%"
  database_name = "alx_book_store"

  create_database(host, user, password, database_name)