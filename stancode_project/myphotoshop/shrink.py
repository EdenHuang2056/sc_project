"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """

    in original picture, I take near four pixels in a unit, and I take the left upper pixel to the new blank picture.

    """

    blank_poppy = SimpleImage.blank(filename.width//2, filename.height//2)

    for x in range(filename.width):
        for y in range(filename.height):

            filename_pixel = filename.get_pixel(x, y)

            if x % 2 == 0 and y % 2 == 0:
                a = x / 2
                b = y / 2
                blank_poppy_pixel = blank_poppy.get_pixel(a, b)
                blank_poppy_pixel.red = filename_pixel.red
                blank_poppy_pixel.green = filename_pixel.green
                blank_poppy_pixel.blue = filename_pixel.blue

    return blank_poppy


def main():
    """

    This program can make original picture become little 1/4.

    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink(original)
    after_shrink.show()


if __name__ == '__main__':
    main()
