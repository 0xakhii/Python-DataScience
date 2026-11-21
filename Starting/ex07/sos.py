import sys as sys


MORSE_CODE = {
                'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..',
                '0': '-----', '1': '.----',  '2': '..---',
                '3': '...--', '4': '....-',  '5': '.....',
            }


def morse_encode(input):
    """ A function that decodes alphanumeric strings to morse code"""
    try:
        for chr in input:
            if chr.isalnum() or chr.isspace():
                pass
            else:
                raise AssertionError("AssertionError: bad argument")
        print(' '.join(MORSE_CODE.get(c.upper()) for c in input))
    except AssertionError as error:
        print(error)
        sys.exit(1)


def main():
    """Main function. acts as the program starting point"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: bad arguments")
        morse_encode(str(sys.argv[1]))
    except AssertionError as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
