from os import get_terminal_size
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
            '6': '-....', '7': '--...',  '8': '---..',
            '9': '----.', ' ': '/'
            }


def filterstring(input, length):
    """This function accepts two arguments: a string (input)
        and an integer (length).
        output: a list of words from <input>
        that have a length greater than <length>.
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


def ft_tqdm(lst: range) -> None:
    size = int(get_terminal_size().columns - get_terminal_size().lines)
    for i, item in enumerate(lst, start=1):
        percentage = int(100 * float(i) / float(len(lst)))
        filled = int(size * percentage / 100)
        bar = '█' * filled + ' ' * (size - filled)
        print(f"\r{percentage:3}%|{bar}| {i}/{len(lst)}", end='', flush=True)
        yield item
