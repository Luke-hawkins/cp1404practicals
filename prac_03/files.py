def main():
    # question_one()
    # question_two()
    question_three()
    question_four()

def question_one():
    name = input("Name: ")
    out_file = open("name.txt", 'w')
    print(name,file=out_file)
    out_file.close()

def question_two():
    in_file = open("name.txt", 'r')
    name = in_file.read()
    print(f"hello {name}")
    in_file.close()

def question_three():
    with open("numbers.txt", 'r') as in_file:
        first_number = int(in_file.readline())
        second_number = int(in_file.readline())
    print(first_number + second_number)

def question_four():
    sum_of_numbers = 0
    with open("numbers.txt", 'r') as in_file:
        for line in in_file:
            sum_of_numbers += int(line)
    print(sum_of_numbers)


main()