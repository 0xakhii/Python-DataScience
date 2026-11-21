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
    """ ft_tqdm is an implementation of
        tqdm function with the yeild operator """
    total = len(lst)
    if total == 0:
        return

    try:
        columns = get_terminal_size().columns
    except OSError:
        columns = 80
    for i, item in enumerate(lst, start=1):
        percentage = int(100 * i / total)
        prefix = f"{percentage:3}%|"
        suffix = f"| {i}/{total}"
        bar_size = max(10, columns - len(prefix) - len(suffix) - 1)
        filled = int(bar_size * i / total)
        bar = '█' * filled + ' ' * (bar_size - filled)
        print(f"\r{prefix}{bar}{suffix}", end='', flush=True)
        yield item
