import string

COLUMNS = 10


def get_chars():
    chars = string.lowercase
    chars += string.uppercase
    chars += string.octdigits
    chars += string.punctuation
    result = [chars[i:i + COLUMNS] for i in xrange(0, len(chars), COLUMNS)]
    result[-1] = result[-1].ljust(10)
    return result
