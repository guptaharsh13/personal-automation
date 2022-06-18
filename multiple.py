import os
from organizer import organize


def multiple_organizer(path, want_name):
    os.chdir(path=path)
    for f_name in os.listdir():
        if not os.path.isdir(f_name):
            continue
        organize(os.path.join(os.getcwd(), f_name), want_name)


def main():
    path = input('Enter the absolute path to your course folder - ')
    path = fr'{path}'.format(path=path)
    want_name = input("Do you want name (y/n) - ")
    want_name = want_name.lower()
    while not (want_name == "y" or want_name == "n"):
        want_name = input("Do you want name - ")

    multiple_organizer(path, want_name=want_name)


if __name__ == "__main__":
    main()
