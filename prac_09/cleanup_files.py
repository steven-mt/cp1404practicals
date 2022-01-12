"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Add a loop to rename the files
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print(f"Renaming {filename} to {new_name}")
            # new_name = os.path.join(directory_name, get_fixed_filename(filename))
            # os.rename(os.path.join(directory_name, filename), new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for i in range(len(filename)):
        if i < (len(filename) - 1):
            if filename[i].islower() and filename[i + 1].isupper():
                new_name += filename[i] + "_"
            elif filename[i].islower() and (filename[i - 1] == " " or filename[i - 1] == "("):
                new_name += filename[i].upper()
            elif filename[i] == " ":
                new_name += "_"
            else:
                new_name += filename[i]
        else:
            new_name += filename[i]

    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
