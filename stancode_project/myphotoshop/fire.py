"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(original):

    """

    we need to find the fire and make it bright red and make the other points become gray.

    """

    for pixel in original:
        avg = (pixel.red + pixel.green + pixel.blue)/3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = pixel.green = pixel.blue = avg

    return original


def main():
    """

    This program can detect the picture where is fire, and emphasize the fire to become red.

    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires(original_fire)
    highlighted_fire.show()


if __name__ == '__main__':
    main()
