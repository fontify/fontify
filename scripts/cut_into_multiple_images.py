import os
from PIL import Image, ImageChops

from data import (COLUMNS,
                  ROWS,
                  RELA_PIXELS_CHARACTER_BAR_HEIGHT,
                  RELA_PIXELS_WRITING_BOX_HEIGHT,
                  RELA_PIXELS_WRITING_BOX_WIDTH,
                  RELA_PIXELS_BORDER_WIDTH,
                  get_flat_chars,
                  PERCENTAGE_TO_CROP_CHAR_IMG,
                  CUT_CHAR_IMGS_DIR)
from crop_image import crop, trim


def _calculate_actual_pixels(image_width, image_height):
    rela_width_unit_percentage  = (1.0 / (RELA_PIXELS_BORDER_WIDTH * 2 +
                                          COLUMNS *
                                          (RELA_PIXELS_WRITING_BOX_WIDTH + 1)))
    rela_height_unit_percentage = (1.0 / (RELA_PIXELS_BORDER_WIDTH * 2 +
                                          ROWS * 
                                          (RELA_PIXELS_WRITING_BOX_HEIGHT +
                                           RELA_PIXELS_CHARACTER_BAR_HEIGHT
                                           + 1)))

    actual_character_bar_height = (RELA_PIXELS_CHARACTER_BAR_HEIGHT *
                                   rela_height_unit_percentage * image_height)
    actual_writing_box_height   = (RELA_PIXELS_WRITING_BOX_HEIGHT *
                                   rela_height_unit_percentage * image_height)
    actual_writing_box_width    = (RELA_PIXELS_WRITING_BOX_WIDTH *
                                   rela_width_unit_percentage * image_width)
    actual_border_width         = (RELA_PIXELS_BORDER_WIDTH *
                                   rela_width_unit_percentage * image_width)

    return (int(actual_character_bar_height),
            int(actual_writing_box_height),
            int(actual_writing_box_width),
            int(actual_border_width),
            int(rela_width_unit_percentage * image_width))


def cut(filepath):
    im = Image.open(filepath)
    imdir = os.path.dirname(filepath)
    if imdir == "":
        imdir = "."
    image_width, image_height = im.size

    actual_pixels = _calculate_actual_pixels(image_width, image_height)
    bar_height, box_height, box_width, border_width, one_unit = actual_pixels

    row = 0
    col = 0

    for char in get_flat_chars():
        left  = border_width + col * (box_width + one_unit)
        upper = border_width + row * (bar_height + box_height + one_unit) + bar_height
        right = left + box_width
        lower = upper + box_height

        char_im = im.crop((left, upper, right, lower))
        char_im = trim(char_im, PERCENTAGE_TO_CROP_CHAR_IMG, False)
        char_im.save("{}/bmp/{}.bmp".format(imdir, hex(ord(char))))

        col += 1
        if col >= 10:
            col = 0
            row += 1


if __name__ == "__main__":
    import sys
    image_filepath = sys.argv[1]
    cut(image_filepath)
    print "./{}/".format(CUT_CHAR_IMGS_DIR)







