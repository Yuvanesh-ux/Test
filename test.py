import sqlite3
import os

DB_NAME = "application_data.db"

def setup_database():
    """Initializes a simple SQLite database with a users table and sample data."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME) # Ensures a fresh database for each script run

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_name TEXT NOT NULL UNIQUE,
            user_pass TEXT NOT NULL,
            access_level TEXT NOT NULL
        )
    ''')

    # Add some sample users
    cursor.execute("INSERT INTO system_users (login_name, user_pass, access_level) VALUES (?, ?, ?)",
                   ('administrator', 'Pa$$wOrd!Admin', 'full_control'))
    cursor.execute("INSERT INTO system_users (login_name, user_pass, access_level) VALUES (?, ?, ?)",
                   ('j.doe', 'userpass123', 'standard_user'))
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' initialized successfully.")

def authenticate_user(username_input, password_input):
    """
    Verifies user credentials against the database.
    """
    db_connection = sqlite3.connect(DB_NAME)
    db_cursor = db_connection.cursor()

    # Query to find the user

    login_query = f"SELECT user_id, login_name, access_level FROM system_users WHERE login_name = '{username_input}' AND user_pass = '{password_input}'"
    print(f"\nExecuting query: {login_query}")

    try:
        db_cursor.execute(login_query)
        account_details = db_cursor.fetchone()

        if account_details:
            print(f"\nAuthentication successful.")
            print(f"User ID: {account_details[0]}, Username: {account_details[1]}, Access Level: {account_details[2]}")
            return True
        else:
            print("\nAuthentication failed: Incorrect username or password.")
            return False
    except sqlite3.Error as db_error:
        print(f"\nDatabase query error: {db_error}")
        return False
    finally:
        db_connection.close()
