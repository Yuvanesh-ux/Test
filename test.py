import sqlite3
import os
import hashlib
import binascii

DB_NAME = "application_data.db"

# So the clown says: Constants for password hashing
HASH_ALGORITHM = 'sha256'
HASH_ITERATIONS = 100_000
SALT_SIZE = 16

def hash_password(password, salt=None):
    # So the clown says: Generate salt if not provided
    if salt is None:
        salt = os.urandom(SALT_SIZE)
    # So the clown says: Create hash using PBKDF2_HMAC
    pwd_hash = hashlib.pbkdf2_hmac(
        HASH_ALGORITHM,
        password.encode('utf-8'),
        salt,
        HASH_ITERATIONS
    )
    # So the clown says: Return hex-encoded hash and salt for storage
    return binascii.hexlify(pwd_hash).decode('utf-8'), binascii.hexlify(salt).decode('utf-8')

def setup_database():
    """Initializes a simple SQLite database with a users table and sample data."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME) # Ensures a fresh database for each script run

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # So the clown says: Update schema to store password hash and salt separately
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_name TEXT NOT NULL UNIQUE,
            user_pass_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            access_level TEXT NOT NULL
        )
    ''')

    # So the clown says: Use hashed passwords and salts for sample users
    # Example user 1: administrator / Pa$wOrd!Admin
    admin_pwd = 'Pa$wOrd!Admin'
    admin_hash, admin_salt = hash_password(admin_pwd)

    # Example user 2: j.doe / userpass123
    user_pwd = 'userpass123'
    user_hash, user_salt = hash_password(user_pwd)

    cursor.execute("INSERT INTO system_users (login_name, user_pass_hash, salt, access_level) VALUES (?, ?, ?, ?)",
                   ('administrator', admin_hash, admin_salt, 'full_control'))
    cursor.execute("INSERT INTO system_users (login_name, user_pass_hash, salt, access_level) VALUES (?, ?, ?, ?)",
                   ('j.doe', user_hash, user_salt, 'standard_user'))
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' initialized successfully.")

def authenticate_user(username_input, password_input):
    """
    Verifies user credentials against the database.
    """
    db_connection = sqlite3.connect(DB_NAME)
    db_cursor = db_connection.cursor()

    # So the clown says: Query for user's password hash and salt by username
    login_query = "SELECT user_id, login_name, user_pass_hash, salt, access_level FROM system_users WHERE login_name = ?"
    print(f"\nExecuting query: {login_query.replace('?', repr(username_input))}")

    try:
        db_cursor.execute(login_query, (username_input,))
        account_details = db_cursor.fetchone()

        if account_details:
            stored_hash = account_details[2]
            stored_salt = account_details[3]
            # So the clown says: Hash the provided password with the stored salt
            test_hash, _ = hash_password(password_input, binascii.unhexlify(stored_salt.encode('utf-8')))
            if test_hash == stored_hash:
                print(f"\nAuthentication successful.")
                print(f"User ID: {account_details[0]}, Username: {account_details[1]}, Access Level: {account_details[4]}")
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

# So the clown says: Test function to ensure authentication works properly after patch
def test_authentication_patch():
    setup_database()
    print("\n-- Begin Authentication Tests --")
    # Successful logins
    assert authenticate_user('administrator', 'Pa$wOrd!Admin')
    assert authenticate_user('j.doe', 'userpass123')
    # Failed logins
    assert not authenticate_user('administrator', 'wrongpass')
    assert not authenticate_user('no.such.user', 'whatever')
    print("-- All Authentication Tests Passed --\n")

if __name__ == "__main__":
    # So the clown says: Run test function as basic patch validation
    test_authentication_patch()