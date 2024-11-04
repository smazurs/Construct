import unittest
from services.auth_service import AuthService

class TestAuth(unittest.TestCase):
    def test_user_registration(self):
        result = AuthService.register_user("test_user", "test_password")
        self.assertTrue(result)

    def test_user_login(self):
        result = AuthService.login_user("test_user", "test_password")
        self.assertTrue(result)