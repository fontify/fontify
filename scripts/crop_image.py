import os
# import cv2
# import numpy
from PIL import Image, ImageChops, ImageFilter

from data import PERCENTAGE_TO_CROP_SCAN_IMG, CROPPED_IMG_NAME


def crop_by_percentage(origin_im, percentage):
    width, height = origin_im.size
    left = int(percentage * width)
    upper = int(percentage * height)
    right = int((1 - percentage) * width)
    lower = int((1 - percentage) * height)
    im = origin_im.crop((left, upper, right, lower))
    return im


# def _restore_if_tild(filepath): # useless for now
#     img = cv2.imread(filepath, 0)
#     img = cv2.medianBlur(img, 5)

#     import pdb
#     pdb.set_trace()

#     cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#     circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 500, param1=50, param2=30, minRadius=10, maxRadius=1000)

#     pdb.set_trace()

#     circles = numpy.uint16(numpy.around(circles))
#     pdb.set_trace()

#     for i in circles[0,:]:
#         # draw the outer circle
#         cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#         # draw the center of the circle
#         cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

#     # cv2.imshow('detected circles',cimg)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#     cv2.imwrite("detected_circles.bmp", cimg)


def trim(origin_im, blur=True,
         pre_percentage=PERCENTAGE_TO_CROP_SCAN_IMG, upper_lower_cut=True):
    im = crop_by_percentage(origin_im, pre_percentage)
    if blur:
        im_blurred = im.filter(ImageFilter.GaussianBlur(radius=2))
        bg = Image.new(im_blurred.mode, im_blurred.size, im.getpixel((0, 0)))
        diff = ImageChops.difference(im_blurred, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
    else:
        bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
        diff = ImageChops.difference(im, bg)
        bbox = diff.getbbox()
    if bbox:
        if upper_lower_cut:
            return im.crop(bbox)
        else:
            width, height = im.size
            bbox = list(bbox)
            bbox[0] = max(0, bbox[0] - int(width * 0.05))
            bbox[1] = 0
            bbox[2] = min(width, bbox[2] + int(width * 0.05))
            bbox[3] = height
            print bbox
            return im.crop(bbox)
    else:
        # raise Exception("Error while cropping image, there is no bounding box to crop")
        return im


def crop_whole(filepath):
    im = Image.open(filepath)
    im = trim(im)
    trimmed_filepath = os.path.join(
        os.path.dirname(filepath),
        CROPPED_IMG_NAME
    )
    im.save(trimmed_filepath)
    return trimmed_filepath


def crop_char(filepath):
    im = Image.open(filepath)
    im = trim(im, blur=False, pre_percentage=0, upper_lower_cut=False)
    im.save(filepath)


# for MANUAL unit test
if __name__ == "__main__":
    import sys
    trimmed_filepath = crop_whole(sys.argv[1])
    im = Image.open(trimmed_filepath)
    print trimmed_filepath
