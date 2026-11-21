import sys as sys
try:
    if (len(sys.argv) > 2):
        ErrorMsg = "AssertionError: more than one argument is provided"
        raise AssertionError(ErrorMsg)
    elif len(sys.argv) == 1:
        sys.exit(0)
    try:
        arg = int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")

    arg = int(sys.argv[1])
    if arg < 0:
        arg = arg * -1
    if arg % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except AssertionError as error:
    print(error)
