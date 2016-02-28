from PIL import Image, ImageChops, ImageFilter

from data import PERCENTAGE_TO_CROP


def _trim(origin_im):
    width, height = origin_im.size
    left  = int(PERCENTAGE_TO_CROP * width)
    upper = int(PERCENTAGE_TO_CROP * height)
    right = int((1 - PERCENTAGE_TO_CROP) * width)
    lower = int((1 - PERCENTAGE_TO_CROP) * height)

    im = origin_im.crop((left, upper, right, lower))
    im = im.filter(ImageFilter.GaussianBlur(radius=3))

    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
      return im.crop(bbox)
    else:
      raise Exception("Error while cropping image, there is no bounding box to crop")


def crop(filepath):
    im = Image.open(filepath)
    im = _trim(im)
    trimmed_filepath = "cropped_picture.bmp"
    im.save(trimmed_filepath)
    return trimmed_filepath


# for MANUAL unit test
if __name__ == "__main__":
    import sys
    trimmed_filepath = crop(sys.argv[1])
    im = Image.open(trimmed_filepath)
    im.show()

