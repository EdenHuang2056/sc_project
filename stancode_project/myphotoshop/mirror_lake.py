"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(original):
    """

    we need to make the blank picture that height is twice as height as original picture, and make a mirror image
    under the original picture.

    """

    blank_mt = SimpleImage.blank(original.width, original.height*2)
    blank_mt.show()

    for x in range(original.width):
        for y in range(original.height):

            original_pixel = original.get_pixel(x, y)

            mirror_mt1_pixel = blank_mt.get_pixel(x, y)
            mirror_mt2_pixel = blank_mt.get_pixel(x, blank_mt.height-y-1)

            mirror_mt1_pixel.red = original_pixel.red
            mirror_mt1_pixel.green = original_pixel.green
            mirror_mt1_pixel.blue = original_pixel.blue

            mirror_mt2_pixel.red = original_pixel.red
            mirror_mt2_pixel.green = original_pixel.green
            mirror_mt2_pixel.blue = original_pixel.blue

    return blank_mt


def main():
    """

    This program can make the mirror image under the original picture that we input.

    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect(original_mt)
    reflected.show()


if __name__ == '__main__':
    main()
