from models.user_model import UserModel

class AuthService:
    @staticmethod
    def register(username, password):
        UserModel.create_user(username, password)
    
    @staticmethod
    def login(username, password):
        return UserModel.authenticate(username, password)
    
    @staticmethod
    def has_users():
        return UserModel.count_users() > 0
