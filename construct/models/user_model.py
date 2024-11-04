from . import get_db_connection

class UserModel:
    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

    @staticmethod
    def authenticate(username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None

    @staticmethod
    def count_users():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM User")
        count = cursor.fetchone()[0]
        conn.close()
        return count