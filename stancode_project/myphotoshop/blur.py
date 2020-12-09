"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """

    we need to get every pixel and make the summary near the pixel then get average, so we can get the new pixel.

    """

    for x in range(img.width):
        for y in range(img.height):

            blur_img_pixel = img.get_pixel(x, y)

            if x == 0 and y == 0:
                # the left upper corner point
                img_pixel = img.get_pixel(x, y)
                right_pixel = img.get_pixel(x + 1, y)
                down_pixel = img.get_pixel(x, y + 1)
                right_down_pixel = img.get_pixel(x + 1, y + 1)

                blur_img_pixel.red = (img_pixel.red + right_pixel.red + right_down_pixel.red + down_pixel.red)/4
                blur_img_pixel.green = (img_pixel.green + right_pixel.green + right_down_pixel.green + down_pixel.green)/4
                blur_img_pixel.blue = (img_pixel.blue + right_pixel.blue + right_down_pixel.blue + down_pixel.blue)/4

            elif x == 0 and y == (img.height-1) :
                # the left down corner point
                upper_pixel = img.get_pixel(x, y - 1)
                right_upper_pixel = img.get_pixel(x + 1, y - 1)
                img_pixel = img.get_pixel(x, y)
                right_pixel = img.get_pixel(x + 1, y)

                blur_img_pixel.red = (img_pixel.red + upper_pixel.red + right_upper_pixel.red + right_pixel.red)/4
                blur_img_pixel.green = (img_pixel.green + upper_pixel.green + right_upper_pixel.green + right_pixel.green) / 4
                blur_img_pixel.blue = (img_pixel.blue + upper_pixel.blue + right_upper_pixel.blue + right_pixel.blue)/4

            elif x == (img.width-1) and y == 0:
                # the right upper corner point
                left_pixel = img.get_pixel(x - 1, y)
                img_pixel = img.get_pixel(x, y)
                left_down_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)

                blur_img_pixel.red = (img_pixel.red + down_pixel.red + left_down_pixel.red + left_pixel.red)/4
                blur_img_pixel.green = (img_pixel.green + down_pixel.green + left_down_pixel.green + left_pixel.green)/4
                blur_img_pixel.blue = (img_pixel.blue + down_pixel.blue + left_down_pixel.blue + left_pixel.blue)/4

            elif x == (img.width-1) and y == (img.height-1):
                # the right down corner point
                left_upper_pixel = img.get_pixel(x - 1, y - 1)
                upper_pixel = img.get_pixel(x, y - 1)
                left_pixel = img.get_pixel(x - 1, y)
                img_pixel = img.get_pixel(x, y)

                blur_img_pixel.red = (img_pixel.red + left_pixel.red + left_upper_pixel.red + upper_pixel.red)/4
                blur_img_pixel.green = (img_pixel.green + left_pixel.green + left_upper_pixel.green + upper_pixel.green)/4
                blur_img_pixel.blue = (img_pixel.blue + left_pixel.blue + left_upper_pixel.blue + upper_pixel.blue)/4

            elif 0 < x < (img.width-1) and y == 0:
                # the point on first row except corner point
                left_pixel = img.get_pixel(x - 1, y)
                img_pixel = img.get_pixel(x, y)
                right_pixel = img.get_pixel(x + 1, y)
                left_down_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)
                right_down_pixel = img.get_pixel(x + 1, y + 1)

                blur_img_pixel.red = (img_pixel.red + right_pixel.red + right_down_pixel.red + down_pixel.red + left_down_pixel.red + left_pixel.red)/6
                blur_img_pixel.green = (img_pixel.green + right_pixel.green + right_down_pixel.green + down_pixel.green + left_down_pixel.green + left_pixel.green)/6
                blur_img_pixel.blue = (img_pixel.blue + right_pixel.blue + right_down_pixel.blue + down_pixel.blue + left_down_pixel.blue + left_pixel.blue)/6

            elif 0 < x < (img.width-1) and y == (img.height-1):
                # the point on last row except corner point
                left_upper_pixel = img.get_pixel(x - 1, y - 1)
                upper_pixel = img.get_pixel(x, y - 1)
                right_upper_pixel = img.get_pixel(x + 1, y - 1)
                left_pixel = img.get_pixel(x - 1, y)
                img_pixel = img.get_pixel(x, y)
                right_pixel = img.get_pixel(x + 1, y)

                blur_img_pixel.red = (img_pixel.red + left_pixel.red + left_upper_pixel.red + upper_pixel.red + right_upper_pixel.red + right_pixel.red)/6
                blur_img_pixel.green = (img_pixel.green + left_pixel.green + left_upper_pixel.green + upper_pixel.green + right_upper_pixel.green + right_pixel.green)/6
                blur_img_pixel.blue = (img_pixel.blue + left_pixel.blue + left_upper_pixel.blue + upper_pixel.blue + right_upper_pixel.blue + right_pixel.blue)/6

            elif x == 0 and 0 < y < (img.height-1):
                # the point on first column except corner point
                upper_pixel = img.get_pixel(x, y - 1)
                right_upper_pixel = img.get_pixel(x + 1, y - 1)
                img_pixel = img.get_pixel(x, y)
                right_pixel = img.get_pixel(x + 1, y)
                down_pixel = img.get_pixel(x, y + 1)
                right_down_pixel = img.get_pixel(x + 1, y + 1)

                blur_img_pixel.red = (img_pixel.red + upper_pixel.red + right_upper_pixel.red + right_pixel.red + right_down_pixel.red + down_pixel.red)/6
                blur_img_pixel.green = (img_pixel.green + upper_pixel.green + right_upper_pixel.green + right_pixel.green + right_down_pixel.green + down_pixel.green)/6
                blur_img_pixel.blue = (img_pixel.blue + upper_pixel.blue + right_upper_pixel.blue + right_pixel.blue + right_down_pixel.blue + down_pixel.blue)/6

            elif x == (img.width-1) and 0 < y < (img.height-1):
                # the point on the last column except corner point
                left_upper_pixel = img.get_pixel(x - 1, y - 1)
                upper_pixel = img.get_pixel(x, y - 1)
                left_pixel = img.get_pixel(x - 1, y)
                img_pixel = img.get_pixel(x, y)
                left_down_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)

                blur_img_pixel.red = (img_pixel.red + down_pixel.red + left_down_pixel.red + left_pixel.red + left_upper_pixel.red + upper_pixel.red)/6
                blur_img_pixel.green = (img_pixel.green + down_pixel.green + left_down_pixel.green + left_pixel.green + left_upper_pixel.green + upper_pixel.green)/6
                blur_img_pixel.blue = (img_pixel.blue + down_pixel.blue + left_down_pixel.blue + left_pixel.blue + left_upper_pixel.blue + upper_pixel.blue)/6

            else:
                left_upper_pixel = img.get_pixel(x - 1, y - 1)
                upper_pixel = img.get_pixel(x, y - 1)
                right_upper_pixel = img.get_pixel(x + 1, y - 1)
                left_pixel = img.get_pixel(x - 1, y)
                img_pixel = img.get_pixel(x, y)
                right_pixel = img.get_pixel(x + 1, y)
                left_down_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)
                right_down_pixel = img.get_pixel(x + 1, y + 1)

                blur_img_pixel.red = (img_pixel.red + right_pixel.red + right_down_pixel.red + down_pixel.red + left_down_pixel.red + left_pixel.red + left_upper_pixel.red + upper_pixel.red + right_upper_pixel.red)/9
                blur_img_pixel.green = (img_pixel.green + right_pixel.green + right_down_pixel.green + down_pixel.green + left_down_pixel.green + left_pixel.green + left_upper_pixel.green + upper_pixel.green + right_upper_pixel.green)/9
                blur_img_pixel.blue = (img_pixel.blue + right_pixel.blue + right_down_pixel.blue + down_pixel.blue + left_down_pixel.blue + left_pixel.blue + left_upper_pixel.blue + upper_pixel.blue + right_upper_pixel.blue)/9

    return img


def main():
    """

    This program can make the picture we input become blur.

    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
