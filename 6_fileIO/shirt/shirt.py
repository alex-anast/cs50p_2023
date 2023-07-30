"""
Implement a program that expects exactly two command-line arguments:
- in sys.argv[1], the name (or path) of a JPEG or PNG to read
  (i.e., open) as input
- in sys.argv[2], the name (or path) of a JPEG or PNG to write
  (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background)
on the input after resizing and cropping the input to be the same size, saving
the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:
- if the user does not specify exactly two command-line arguments,
- if the input's and output's names do not end in .jpg, .jpeg, or .png,
  case-insensitively,
- if the input's name does not have the same extension as the output's name, or
- if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way,
like these demos, so that, when they’re resized and cropped, the shirt appears
to fit perfectly.
"""


import os
import sys
from PIL import Image, ImageOps


def main():
    file_input, file_output = get_input()
    convert(file_input, file_output)


def convert(img_name_in, img_name_out="out.png"):
    try:
        shirt = Image.open("shirt.png")  # .convert('RGBA')
        img = Image.open(img_name_in).convert('RGBA')
        img_out = img
        # match photo and shirt
        img_out = ImageOps.fit(img_out, shirt.size)
        # paste over it - overlay
        img_out.paste(shirt, shirt)
        # save to file_output
        img_out_rgb = img_out.convert("RGB")
        img_out_rgb.save(img_name_out)
        # close the image x2
        shirt.close()
        img.close()
    except FileNotFoundError:
        sys.exit("FileNotFoundError")


def get_input() -> list:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (
        not os.path.isfile(sys.argv[1])
        or sys.argv[1].lower().rstrip().split(".")[-1] not in ["png", "jpg", "jpeg"]
        or sys.argv[2].lower().rstrip().split(".")[-1] not in ["png", "jpg", "jpeg"]
    ):
        sys.exit("Invalid input")
    elif sys.argv[1][-3:] != sys.argv[2][-3:]:
        sys.exit("Input and output have different extensions")
    else:
        return (sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
