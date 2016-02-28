import string

ROWS = 12
COLUMNS = 14
TMPL_OPTIONS = {
    'page-size': 'Letter'
}

PERCENTAGE_TO_CROP_SCAN_IMG = 0.005
PERCENTAGE_TO_CROP_CHAR_IMG = 0.1

CROPPED_IMG_NAME = "cropped_picture.bmp"
CUT_CHAR_IMGS_DIR = "cutting_output_images"

MAX_COLUMNS_PER_PAGE = 14
MAX_ROWS_PER_PAEG = 12
RELA_PIXELS_CHARACTER_BAR_HEIGHT = 30
RELA_PIXELS_WRITING_BOX_HEIGHT = 100
RELA_PIXELS_WRITING_BOX_WIDTH = 100
RELA_PIXELS_BORDER_WIDTH = 1


def get_flat_chars():
    chars = unicode(string.lowercase)
    chars += unicode(string.uppercase)
    chars += unicode(string.digits)
    chars += unicode(string.punctuation)
    print chars
    return chars


def get_chars():
    chars = get_flat_chars()
    result = [chars[i:i + COLUMNS] for i in xrange(0, len(chars), COLUMNS)]
    result[-1] = result[-1].ljust(COLUMNS)
    result.extend([' ' * COLUMNS for i in xrange(len(result), ROWS)])
    return result


def get_sample_chars():
    return iter("AaBb")
