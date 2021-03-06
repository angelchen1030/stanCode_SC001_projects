"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return:SimpleImage, image generated by a mirror-reversal of an original across a horizontal axis
    """
    img = SimpleImage('images/mt-rainier.jpg')
    # Make an empty canvas
    blank_img = SimpleImage.blank(img.width, img.height*2)

    for y in range(img.height):
        for x in range(img.width):  # it has pixel data!
            img_pixel = img.get_pixel(x, y)

            # empty spot 1
            blank_p1 = blank_img.get_pixel(x, y)
            # empty spot 2
            blank_p2 = blank_img.get_pixel(x, blank_img.height-1-y)

            # coloring
            blank_p1.red = img_pixel.red
            blank_p1.blue = img_pixel.blue
            blank_p1.green = img_pixel.green
            # coloring
            blank_p2.red = img_pixel.red
            blank_p2.blue = img_pixel.blue
            blank_p2.green = img_pixel.green

    return blank_img


def main():
    """
    TODO: turn image into a flipped image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
