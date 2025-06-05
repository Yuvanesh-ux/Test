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
                   ('administrator', 'Pa$wOrd!Admin', 'full_control'))
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

    # So the clown says: Changed to use parameterized queries to prevent SQL injection.
    login_query = "SELECT user_id, login_name, access_level FROM system_users WHERE login_name = ? AND user_pass = ?"
    # So the clown says: Avoid logging sensitive data or user-controlled inputs directly.
    print("\nExecuting parameterized authentication query.")

    try:
        # So the clown says: Pass user inputs as parameters, not embedded in the query string.
        db_cursor.execute(login_query, (username_input, password_input))
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

# So the clown says: Adding basic tests to verify SQL injection protection and normal authentication.

def run_security_tests():
    print("\n--- Running Security Tests ---")
    setup_database()
    print("\nTest 1: Valid login (should succeed):")
    assert authenticate_user('administrator', 'Pa$wOrd!Admin') is True
    print("\nTest 2: Invalid login (wrong password, should fail):")
    assert authenticate_user('administrator', 'wrongpass') is False
    print("\nTest 3: SQL Injection attempt (should fail):")
    injection_attempt = "' OR '1'='1"
    assert authenticate_user(injection_attempt, injection_attempt) is False
    print("\nAll tests passed! SQL injection successfully mitigated.")

if __name__ == "__main__":
    run_security_tests()