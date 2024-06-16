LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45

def main():
    total_quick_picks = get_total_quick_picks()
    print(total_quick_picks)


def get_total_quick_picks():
    total_quick_picks = int(input("How many quick picks? "))
    return total_quick_picks


main()
