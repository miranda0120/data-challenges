# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys

def main():
    """Implement the calculator"""

    arg1 = int(sys.argv[1])
    arg2 = sys.argv[2]
    arg3 = int(sys.argv[3])

    if arg2 == '+':
        return arg1 + arg3
    elif arg2 == '-':
        return arg1 - arg3
    elif arg2 == '*':
        return arg1 * arg3







if __name__ == "__main__":
    print(main())
