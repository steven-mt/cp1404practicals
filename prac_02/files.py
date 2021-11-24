def main():
    # 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
    name = input("Enter name: ")
    name_file = open("name.txt", "w")
    print(f"{name}", file=name_file)
    name_file.close()

    # 2. Write code that opens "name.txt" and reads the name (as above) then prints,
    #    "Your name is Bob" (or whatever the name is in the file).
    name_file = open("name.txt", "r")
    print(f"Your name is {name_file.read()}")
    name_file.close()

    # 3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the
    #    result, which should be... 59.
    numbers_file = open("numbers.txt", "r")
    line1 = int(numbers_file.readline())
    line2 = int(numbers_file.readline())
    print(line1 + line2)
    numbers_file.close()

    # 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any
    #    number of numbers.
    numbers_file = open("numbers.txt", "r")
    total_lines = len(numbers_file.readlines())
    print(f"The total number of lines is {total_lines}")
    numbers_file.close()


main()
