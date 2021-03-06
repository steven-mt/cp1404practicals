"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Reads subject details from a file and then displays it."""
    data = get_data()
    display_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    file_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        file_data.append(parts)
    input_file.close()
    return file_data


def display_details(data):
    """Display subject details."""
    for details in data:
        print(f"{details[0]} is taught by {details[1]:12} and has {details[2]:3} students")


main()
