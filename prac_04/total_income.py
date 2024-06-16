"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    display_income_summary(incomes)


def display_income_summary(incomes):
    """display income total over months"""
    print("\nIncome Report\n-------------")
    total = 0
    month_count = 0
    for income in incomes:
        month_count += 1
        total += income
        print(f"Month {month_count:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()