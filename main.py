import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_config = config['db']

cnx = mysql.connector.connect(
    user=db_config['user'],
    password=db_config['password'],
    host=db_config['host'],
    database=db_config['database']
)

# Use the connection to interact with the database
cursor = cnx.cursor()
query = "SELECT * FROM users"
cursor.execute(query)
results = cursor.fetchall()
cursor.close()
cnx.close()

import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_config = config['db']

# Connect to the MySQL database
cnx = mysql.connector.connect(
    user=db_config['user'],
    password=db_config['password'],
    host=db_config['host'],
    database=db_config['database']
)

# Create a cursor object to execute SQL queries
c = cnx.cursor()

# Define functions for CRUD operations
def create_user(first_name, last_name, contact_number ):
    """Create a new user."""
    c.execute("INSERT INTO users (first_name, last_name, contact_number ) VALUES ( %s, %s, %s)", ( first_name, last_name, contact_number, ))
    cnx.commit()
    print("User created successfully.")

def read_user(id):
    """Read user details by ID."""
    sql = "SELECT * FROM users WHERE id=%s"
    c.execute(sql, (id,))
    user = c.fetchone()
    if user:
        print(f"ID: {user[0]}, first_name: {user[1]}, last_name: {user[2]}, contact_number: {user[5]}")
    else:
        print("User not found.")

def update_user(user_id, first_name, last_name):
    """Update user details by ID."""
    c.execute("UPDATE users SET first_name=%s, last_name=%s WHERE id=%s", (first_name, last_name, user_id))
    cnx.commit()
    print("User updated successfully.")

def delete_user(user_id):
    """Delete user by ID."""
    c.execute("DELETE FROM users WHERE id=%s", (user_id,))
    cnx.commit()
    print("User deleted successfully.")

# Main program loop for CRUD operations
while True:
    print("1. Create User")
    print("2. Read User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        contact_number = input("Enter phone: ")
        create_user(first_name, last_name, contact_number)

    elif choice == '2':
        user_id = input("Enter user ID: ")
        read_user(user_id)

    elif choice == '3':
        user_id = input("Enter user ID: ")
        first_name = input("Enter first_name: ")
        last_name = input("Enter last_name: ")
        update_user(user_id, first_name, last_name)

    elif choice == '4':
        user_id = input("Enter user ID: ")
        delete_user(user_id)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

# Close the cursor and connection
c.close()
cnx.close()

