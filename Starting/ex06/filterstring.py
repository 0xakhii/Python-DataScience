import sys as sys


def filterstring(input, length):
    """This function accepts two arguments:
        a string (input) and an integer (length).
        output: a list of words from <input> that have
        a length greater than <length>.
    """
    try:
        error = "AssertionError: the arguments are bad"
        for dig in length:
            if dig.isnumeric():
                pass
            else:
                raise AssertionError(error)
                sys.exit(1)
        length = int(length)
        for chr in input:
            if chr.isalpha() or chr.isspace():
                pass
            else:
                raise AssertionError(error)
                sys.exit(1)
    except AssertionError as error:
        print(error)
        sys.exit(1)
    newList = input.split(' ')
    ret = [word for word in newList if (lambda w: len(w) >= length)(word)]
    return ret


def main():
    """Main function. acts as the program starting point"""
    try:
        error = "AssertionError: the arguments are bad"
        if len(sys.argv) > 3 or len(sys.argv) < 3:
            raise AssertionError(error)
            sys.exit(1)
        print(filterstring(str(sys.argv[1]), sys.argv[2]))
    except AssertionError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
