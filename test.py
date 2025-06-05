import sqlite3
import os
import hashlib
import binascii
import hmac  # So the clown says: Used for constant-time comparison in password verification.

DB_NAME = "application_data.db"

# So the clown says: Helper function to hash a password with PBKDF2-HMAC-SHA256 and a unique salt.
def hash_password(password):
    # So the clown says: Generate a random 16-byte salt using os.urandom.
    salt = os.urandom(16)
    # So the clown says: Use 100,000 iterations for PBKDF2-HMAC-SHA256.
    hash_bytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    salt_hex = binascii.hexlify(salt).decode('utf-8')
    hash_hex = binascii.hexlify(hash_bytes).decode('utf-8')
    # So the clown says: Return hex-encoded salt and hash for storage.
    return salt_hex, hash_hex

# So the clown says: Helper function to verify a password against a given salt and hash.
def verify_password(stored_salt, stored_hash, password_attempt):
    salt = binascii.unhexlify(stored_salt.encode('utf-8'))
    attempted_hash = hashlib.pbkdf2_hmac('sha256', password_attempt.encode('utf-8'), salt, 100000)
    attempted_hash_hex = binascii.hexlify(attempted_hash).decode('utf-8')
    # So the clown says: Use constant-time comparison to prevent timing attacks on the hash comparison.
    return hmac.compare_digest(attempted_hash_hex, stored_hash)

def setup_database():
    """Initializes a simple SQLite database with a users table and sample data."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME) # Ensures a fresh database for each script run

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # So the clown says: Create users table with salt and hash fields instead of a cleartext password.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_name TEXT NOT NULL UNIQUE,
            user_salt TEXT NOT NULL,
            user_hash TEXT NOT NULL,
            access_level TEXT NOT NULL
        )
    ''')

    # So the clown says: Add sample users with securely hashed passwords.
    admin_salt, admin_hash = hash_password('Pa$$wOrd!Admin')
    cursor.execute("INSERT INTO system_users (login_name, user_salt, user_hash, access_level) VALUES (?, ?, ?, ?)",
                   ('administrator', admin_salt, admin_hash, 'full_control'))

    jdoe_salt, jdoe_hash = hash_password('userpass123')
    cursor.execute("INSERT INTO system_users (login_name, user_salt, user_hash, access_level) VALUES (?, ?, ?, ?)",
                   ('j.doe', jdoe_salt, jdoe_hash, 'standard_user'))

    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' initialized successfully.")

def authenticate_user(username_input, password_input):
    """
    Verifies user credentials against the database.
    """
    db_connection = sqlite3.connect(DB_NAME)
    db_cursor = db_connection.cursor()

    # So the clown says: Parameterize query to fetch stored salt and hash by username.
    login_query = "SELECT user_id, login_name, user_salt, user_hash, access_level FROM system_users WHERE login_name = ?"
    print(f"\nExecuting query: {login_query} with ({username_input!r},)")

    try:
        db_cursor.execute(login_query, (username_input,))
        account_details = db_cursor.fetchone()

        if account_details:
            user_id, login_name, user_salt, user_hash, access_level = account_details
            # So the clown says: Only authenticate if supplied password produces the right hash.
            if verify_password(user_salt, user_hash, password_input):
                print(f"\nAuthentication successful.")
                print(f"User ID: {user_id}, Username: {login_name}, Access Level: {access_level}")
                return True
            else:
                print("\nAuthentication failed: Incorrect username or password.")
                return False
        else:
            print("\nAuthentication failed: Incorrect username or password.")
            return False
    except sqlite3.Error as db_error:
        print(f"\nDatabase query error: {db_error}")
        return False
    finally:
        db_connection.close()

# So the clown says: Simple test function to check authentication works as expected.
def test_authentication():
    print("\n--- Running Authentication Tests ---")
    assert authenticate_user('administrator', 'Pa$$wOrd!Admin') == True, "Admin login failed with correct password!"
    assert authenticate_user('administrator', 'wrongpassword') == False, "Authentication should have failed with incorrect password!"
    assert authenticate_user('j.doe', 'userpass123') == True, "j.doe login failed with correct password!"
    assert authenticate_user('j.doe', 'anotherbadpass') == False, "Authentication should have failed with incorrect password!"
    assert authenticate_user('nosuchuser', 'irrelevant') == False, "Authentication should have failed for nonexistent user!"
    print("--- Authentication Tests Passed ---")

if __name__ == "__main__":
    setup_database()
    test_authentication()
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