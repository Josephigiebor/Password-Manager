import unittest
import sqlite3
from auth import register, login
from password_manager import add_password, get_password, delete_password
from encryption import load_key

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        # Setup an in-memory SQLite database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)')
        self.cursor.execute('CREATE TABLE passwords (id INTEGER PRIMARY KEY, user_id INTEGER, service TEXT, encrypted_password TEXT)')
        self.conn.commit()
        self.key = load_key()

    def tearDown(self):
        self.conn.close()

    def test_register_and_login(self):
        username = 'testuser'
        password = 'testpass'
        self.assertTrue(register(username, password))
        user_id = login(username, password)
        self.assertIsNotNone(user_id)

    def test_add_and_get_password(self):
        username = 'testuser'
        password = 'testpass'
        register(username, password)
        user_id = login(username, password)

        service = 'testservice'
        service_password = 'servicepass'
        add_password(user_id, service, service_password, self.key)
        retrieved_password = get_password(user_id, service, self.key)
        self.assertEqual(service_password, retrieved_password)

    def test_delete_password(self):
        username = 'testuser'
        password = 'testpass'
        register(username, password)
        user_id = login(username, password)

        service = 'testservice'
        service_password = 'servicepass'
        add_password(user_id, service, service_password, self.key)
        delete_password(user_id, service)
        retrieved_password = get_password(user_id, service, self.key)
        self.assertIsNone(retrieved_password)

if __name__ == '__main__':
    unittest.main()