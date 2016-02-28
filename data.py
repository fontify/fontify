import string

COLUMNS = 10


def get_chars():
    chars = string.lowercase
    chars += string.uppercase
    chars += string.octdigits
    chars += string.punctuation
    return [chars[i:i + COLUMNS] for i in xrange(0, len(chars), COLUMNS)]
