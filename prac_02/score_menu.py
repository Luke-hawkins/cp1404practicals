def main():
    """Allow user to input score and output results based on the score"""
    MENU = "(G)et a valid score (must be 0-100 inclusive) \n(P)rint result \n(S)how stars \n(Q)uit"
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Some kind of fair well :/")

def get_valid_score():
    """get a valid score from 0 to 100"""
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def get_result(score):
    """Return results based on score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad :("

def print_stars(score):
    """prints a star for every mark out of 100"""
    print("*" * int(score))


main()
