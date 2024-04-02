import secrets
import string

def create_password(password_length = 12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    password = ''
    password_strong = False

    while not password_strong:
        password = ''
        for i in range(password_length):
            password += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in password) and
            sum(char in digits for char in password) >= 2):
            password_strong = True
    return password

#The __name__ variable is a built-in variable in Python that is automatically set by the interpreter.
if __name__ == '__main__':
    print(create_password())