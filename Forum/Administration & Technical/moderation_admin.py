class Security:
    def __init__(self):
        self.spam_filters = []
        self.encryption_key = "secure_key"

    def add_spam_filter(self, filter_rule):
        self.spam_filters.append(filter_rule)
        return "Spam filter added."

    def encrypt_data(self, data):
        # Пример простого "шифрования"
        encrypted = "".join(chr(ord(char) + 1) for char in data)
        return encrypted

    def decrypt_data(self, encrypted_data):
        # Пример простого "дешифрования"
        decrypted = "".join(chr(ord(char) - 1) for char in encrypted_data)
        return decrypted

    def detect_spam(self, message):
        for rule in self.spam_filters:
            if rule in message:
                return True
        return False