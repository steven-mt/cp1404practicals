import os
import shutil


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split(".")[1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, extension)


main()
