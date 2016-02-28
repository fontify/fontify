#!/usr/bin/env python2
import argparse
import tempfile
import shutil
import os
import crop_image


def check_input(image):
    if not os.path.isfile(image):
        raise FileNotFoundError
    _, ext = os.path.splitext(image)
    if ext.lower() not in [".jpg", ".png"]:
        raise ValueError("Unrecognized image extension")


def setup_work_dir(image):
    tmpdir = tempfile.mkdtemp(prefix="fontify")
    _, ext = os.path.splitext(image)
    shutil.copyfile(image, os.path.join(tmpdir, 'input' + ext))
    return tmpdir


def process(image, font_name):
    crop_image.crop()


def tear_down(tmpdir, output):
    if output == "":
        output = "fontify.ttf"
    shutil.copyfile(os.path.join(tmpdir, 'fontify.ttf'), output)
    shutil.rmtree(tmpdir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image", help="input image (JPG or PNG)"
    )
    parser.add_argument(
        "-n", "--name", default="Fontify", help="font name (default: Fontify)"
    )
    parser.add_argument(
        "-o", metavar="OUTPUT", default="",
        help="output font file (default to fontify.ttf in current directory)"
    )
    args = parser.parse_args()
    check_input(args.image)
    tmpdir = setup_work_dir()
    process(tmpdir, args.name)
    tear_down(tmpdir, args.output)
