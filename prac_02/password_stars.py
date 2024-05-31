def main():
    """Gets password and return passwords length in *'s"""
    password = get_password()
    print_hidden_password(password)

def get_password():
    """Get password that meets the required length"""
    password_minimun_length = 10
    password = input("Password:")
    while len(password) < password_minimun_length:
        password = input("invalid password\n Password: ")
    return password

def print_hidden_password(password):
    """Prints *'s the length of the password"""
    print(len(password) * "*")


main()

