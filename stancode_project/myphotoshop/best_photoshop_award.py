"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

THERSHOLD = 1.24

BLACK_PIXEL = 76


def main():

    fg = SimpleImage('images/me.JPG')
    bg = SimpleImage('images/beach.jpg')
    bg.make_as_big_as(fg)
    fg.show()
    bg.show()
    filter_img = filtered(fg, bg)
    filter_img.show()


def filtered(me, beach):

    for x in range(me.width):
        for y in range(me.height):
            me_pixel = me.get_pixel(x, y)
            total = (me_pixel.red + me_pixel.green + me_pixel.blue)
            avg = total/3

            if me_pixel.green > avg * THERSHOLD and total > BLACK_PIXEL:
                beach_pixel = beach.get_pixel(x, y)
                me_pixel.red = beach_pixel.red
                me_pixel.green = beach_pixel.green
                me_pixel.blue = beach_pixel.blue

    return me

if __name__ == '__main__':
    main()
