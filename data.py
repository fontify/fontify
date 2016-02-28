import string

ROWS = 12
COLUMNS = 14
TMPL_OPTIONS = {
    'page-size': 'Letter'
}

PERCENTAGE_TO_CROP = 0.005

MAX_COLUMNS_PER_PAGE = 10
MAX_ROWS_PER_PAEG = 10
RELA_PIXELS_CHARACTER_BAR_HEIGHT= 30
RELA_PIXELS_WRITING_BOX_HEIGHT= 100
RELA_PIXELS_WRITING_BOX_WIDTH = 100
RELA_PIXELS_BORDER_WIDTH = 5

def get_flat_chars():
    chars = unicode(string.lowercase)
    chars += unicode(string.uppercase)
    chars += unicode(string.octdigits)
    chars += unicode(string.punctuation)
    return chars


def get_chars():
    chars = get_flat_chars()
    result = [chars[i:i + COLUMNS] for i in xrange(0, len(chars), COLUMNS)]
    result[-1] = result[-1].ljust(COLUMNS)
    result.extend([' ' * COLUMNS for i in xrange(len(result), ROWS)])
    return result


def get_sample_chars():
    return iter("AaBbCcDd")
