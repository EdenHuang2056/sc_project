"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the RayGreenScreen.png
    :return: SimpleImage, Put Ray's photo into the Millennium Falcon space ship
    """

    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_pixel = figure_img.get_pixel(x, y)
            background_pixel = background_img.get_pixel(x, y)
            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > bigger * 2:
                figure_pixel.red = background_pixel.red
                figure_pixel.green = background_pixel.green
                figure_pixel.blue = background_pixel.blue

    return figure_img


def main():
    """

    This program can make green screen in original picture become new screen.

    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.show()
    figure.show()
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
