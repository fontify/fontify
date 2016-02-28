import string

COLUMNS = 10


def get_flat_chars():
    chars = string.lowercase
    chars += string.uppercase
    chars += string.octdigits
    chars += string.punctuation
    return chars


def get_chars():
    chars = get_flat_chars()
    result = [chars[i:i + COLUMNS] for i in xrange(0, len(chars), COLUMNS)]
    result[-1] = result[-1].ljust(10)
    return result
