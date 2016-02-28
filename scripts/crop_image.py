import os
import cv2
import numpy
from PIL import Image, ImageChops, ImageFilter

from data import PERCENTAGE_TO_CROP_SCAN_IMG, CROPPED_IMG_NAME


def crop_by_percentage(origin_im, percentage):
    width, height = origin_im.size
    left  = int(percentage * width)
    upper = int(percentage * height)
    right = int((1 - percentage) * width)
    lower = int((1 - percentage) * height)
    im = origin_im.crop((left, upper, right, lower))
    return im


def _restore_if_tild(filepath): # useless for now
    img = cv2.imread(filepath, 0)
    img = cv2.medianBlur(img, 5)

    import pdb
    pdb.set_trace()

    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 500, param1=50, param2=30, minRadius=10, maxRadius=1000)

    pdb.set_trace()

    circles = numpy.uint16(numpy.around(circles))
    pdb.set_trace()

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    # cv2.imshow('detected circles',cimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite("detected_circles.bmp", cimg)


def trim(origin_im, pre_percentage=None, upper_lower_cut=True):
    if pre_percentage:
        pre_percentage_to_crop = pre_percentage
    else:
        pre_percentage_to_crop = PERCENTAGE_TO_CROP_SCAN_IMG
    im_unblurred = crop_by_percentage(origin_im, pre_percentage_to_crop)
    im = im_unblurred.filter(ImageFilter.GaussianBlur(radius=2))

    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        if upper_lower_cut:
            return im_unblurred.crop(bbox)
        else:
            width, height = im_unblurred.size
            left, upper, right, lower = bbox
            return im_unblurred.crop((int(left - width * 0.1), 0, int(right + width * 0.1), height))
    else:
        # raise Exception("Error while cropping image, there is no bounding box to crop")
        return im_unblurred


def crop(filepath):
    im = Image.open(filepath)
    im = trim(im)
    trimmed_filepath = os.path.join(
        os.path.dirname(filepath),
        CROPPED_IMG_NAME
    )
    im.save(trimmed_filepath)
    return trimmed_filepath


# for MANUAL unit test
if __name__ == "__main__":
    import sys
    trimmed_filepath = crop(sys.argv[1])
    im = Image.open(trimmed_filepath)
    print trimmed_filepath

