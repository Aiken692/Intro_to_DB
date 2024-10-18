import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'yourusername',         # Replace with your MySQL username
    'password': 'yourpassword',     # Replace with your MySQL password
    'host': 'localhost',            # Change if your MySQL server is hosted elsewhere
}

try:
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create the database if it doesn't already exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    
    # Commit the changes
    conn.commit()
    
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection if they were opened
    if cursor:
        cursor.close()
    if conn:
        conn.close()
