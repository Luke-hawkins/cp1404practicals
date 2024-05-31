"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
while score > 100 or score < 0:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad :(")
