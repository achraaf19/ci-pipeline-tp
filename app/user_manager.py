class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        if not username:
            raise ValueError("Nom obligatoire")
        if username in self.users:
            raise ValueError("Existe deja")
        self.users.append(username)

    def count_users(self):
        return len(self.users)