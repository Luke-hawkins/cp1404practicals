"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    """Generates a score bases on results"""
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    score = random.randint(0,100)
    result = get_result(score)
    print(f"Random result is {result}")

def get_result(score):
    """Return results based on score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad :("


main()
