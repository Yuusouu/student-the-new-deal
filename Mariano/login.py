# login.py
class Login:
    def __init__(self):
        self.username = "admin"
        self.password = "password123"

    def authenticate(self, username, password):
        return username == self.username and password == self.password
