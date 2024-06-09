def main():
    question_one()
    question_two()
    question_three()

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
    in_file = open("files.txt", 'r')


main()