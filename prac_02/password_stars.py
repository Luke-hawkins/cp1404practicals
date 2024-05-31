def main():
    password = get_password()
    print_hidden_password(password)

def get_password():
    password_minimun_length = 10
    password = input("Password:")
    while len(password) < password_minimun_length:
        password = input("invalid password\n Password: ")
    return password

def print_hidden_password(password):
    print(len(password) * "*")


main()

