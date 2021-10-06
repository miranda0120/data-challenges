# pylint: disable=missing-docstring

import sys

def full_name(first_name, last_name):
    # """returns the full name"""
    if first_name == "":
        return last_name.capitalize().strip()
    elif last_name == "":
        return first_name.capitalize().strip()
    else:
        return f"{first_name.capitalize().strip()} {last_name.capitalize().strip()}"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You must provide a first name and a last name as arguments!")
    else:
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}")
