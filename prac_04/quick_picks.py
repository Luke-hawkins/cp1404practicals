import random
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45
TOTAL_NUMBER_OF_NUMBERS = 6

def main():
    """Generates quick pick for user"""
    total_quick_picks = get_total_quick_picks()
    generate_quick_picks(total_quick_picks)


def generate_quick_picks(total_quick_picks):
    """Produces quick picks based on total quick picks"""
    quick_picks = []
    for i in range(total_quick_picks):
        for number in range(TOTAL_NUMBER_OF_NUMBERS):
            quick_picks.append(random.randint(LOWEST_NUMBER, HIGHEST_NUMBER))
        quick_picks.sort()
        display_quick_pick(quick_picks)
        quick_picks.clear()


def display_quick_pick(quick_picks):
    """display quick picks"""
    print(*quick_picks, sep=", ")


def get_total_quick_picks():
    """return total number of quick picks"""
    total_quick_picks = int(input("How many quick picks? "))
    return total_quick_picks


main()
