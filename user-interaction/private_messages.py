class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        if username in self.users:
            return "User already exists."
        self.users[username] = {"password": password, "email": email, "role": "user"}
        return "User registered successfully."

    def login_user(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return "Login successful."
        return "Invalid credentials."

    def edit_profile(self, username, new_email=None, new_password=None):
        if username in self.users:
            if new_email:
                self.users[username]["email"] = new_email
            if new_password:
                self.users[username]["password"] = new_password
            return "Profile updated."
        return "User not found."

    def change_role(self, username, new_role):
        if username in self.users:
            self.users[username]["role"] = new_role
            return "Role updated."
        return "User not found."