import string

COLUMNS = 14
TMPL_OPTIONS = {
    'page-size': 'Letter'
}


def get_flat_chars():
    chars = unicode(string.lowercase)
    chars += unicode(string.uppercase)
    chars += unicode(string.octdigits)
    chars += unicode(string.punctuation)
    return chars


def get_chars():
    chars = get_flat_chars()
    result = [chars[i:i + COLUMNS] for i in xrange(0, len(chars), COLUMNS)]
    result[-1] = result[-1].ljust(10)
    return result


def get_sample_chars():
    return iter("AaBbCcDd")
