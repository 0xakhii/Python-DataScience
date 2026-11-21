import sys as sys
import re as re


def building(input: str):
    """this is the building function"""
    print("The text contains", len(input), "charachters:")
    cap = re.findall('([A-Z])', input)
    print(len(cap), "upper letters")
    low = re.findall('([a-z])', input)
    print(len(low), "lower letters")
    punc = re.findall(r'[^\w\s]', input)
    print(len(punc), "punctuation marks")
    wspc = re.findall(r'\s', input)
    print(len(wspc), "spaces")
    num = re.findall('([0-9])', input)
    print(len(num), "digits")


def main():
    """Main function. act as the starting point of the program"""
    try:
        if len(sys.argv) > 2:
            error = "AssertionError: more than 1 argument was provided"
            raise AssertionError(error)
        elif len(sys.argv) == 2:
            building(sys.argv[1])
        elif len(sys.argv):
            print("What is the text to count? ", end="\n", flush=True)
            building(sys.stdin.read())
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
