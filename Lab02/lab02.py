""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Lab 02

Write a program that has three functions: sepia(), remove_all_red(), and gray_scale() to process the image.
Plot all four images.  No global variables are allowed.
Each function needs parameter(s) in order to manipulate and draw the image.

@author: Dani Hooven
@version: 10/13/2020

-------------------------------------------------------------------------------------------------------------------- """

# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

import image


# ----------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def negative(i, win):
    """
    Function that takes an image, processes the pixels to negative values, and returns a new image
    :param win: window frame to display image
    :param i: image file
    :return: new image
    """
    # Creates and returns empty image object with width and height
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    # Image processing - do something with pixel at position (col,row)
    for row in range(i.getHeight()):
        for col in range(i.getWidth()):
            # get one pixel
            p = i.getPixel(col, row)

            #   change the properties
            new_red = 255 - p.getRed()
            new_green = 255 - p.getGreen()
            new_blue = 255 - p.getBlue()

            #   set pixel to new properties
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            newimg.setPixel(col, row, new_pixel)  # setter method
    return newimg.draw(win)


def sepia(i, win):
    """
    Function that takes an image, processes the pixels to sepia values, and returns a new image
    :param win: window frame to display image
    :param i: image file
    :return: new image
    """
    # Creates and returns empty image object with width and height
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    # Image processing - do something with pixel at position (col,row)
    for row in range(i.getHeight()):
        for col in range(i.getWidth()):
            # get one pixel
            p = i.getPixel(col, row)

            #   change the properties
            new_red = int((p.getRed() * 0.393) + (p.getGreen() * 0.769) + (p.getBlue() * 0.189))
            if new_red > 255:
                new_red = 255
            new_green = int((p.getRed() * 0.349) + (p.getGreen() * 0.686) + (p.getBlue() * 0.168))
            if new_green > 255:
                new_green = 255
            new_blue = int((p.getRed() * 0.272) + (p.getGreen() * 0.534) + (p.getBlue() * 0.131))
            if new_blue > 255:
                new_blue = 255

            #   set pixel to new properties
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            newimg.setPixel(col, row, new_pixel)  # setter method
    return newimg.draw(win)


def remove_all_red(i, win):
    """
    Function that takes an image, processes the pixels by removing all red values, and returns a new image
    :param win: window frame to display image
    :param i: image file
    :return: new image
    """
    # Creates and returns empty image object with width and height
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    # Image processing - do something with pixel at position (col,row)
    for row in range(i.getHeight()):
        for col in range(i.getWidth()):
            # get one pixel
            p = i.getPixel(col, row)

            #   change the properties
            new_red = 0
            new_green = p.getGreen()
            new_blue = p.getBlue()

            #   set pixel to new properties
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            newimg.setPixel(col, row, new_pixel)  # setter method
    return newimg.draw(win)


def gray_scale(i, win):
    """
    Function that takes an image, processes the pixels to gray values, and returns a new image
    :param win: window frame to display image
    :param i: image file
    :return: new image
    """
    # Creates and returns empty image object with width and height
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    # Image processing - do something with pixel at position (col,row)
    for row in range(i.getHeight()):
        for col in range(i.getWidth()):
            # get one pixel
            p = i.getPixel(col, row)

            #   change the properties
            new_red = int((p.getRed() * 0.289) + (p.getGreen() * 0.587) + (p.getBlue() * 0.114))
            if new_red > 255:
                new_red = 255
            new_green = int((p.getRed() * 0.289) + (p.getGreen() * 0.587) + (p.getBlue() * 0.114))
            if new_green > 255:
                new_green = 255
            new_blue = int((p.getRed() * 0.289) + (p.getGreen() * 0.587) + (p.getBlue() * 0.114))
            if new_blue > 255:
                new_blue = 255

            #   set pixel to new properties
            new_pixel = image.Pixel(new_red, new_green, new_blue)
            newimg.setPixel(col, row, new_pixel)  # setter method
    return newimg.draw(win)


# ----------------------------------------------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------------------------------------------

# Creates an Image object from the filename
img = image.Image("colors.png")

# ImageWin makes a frame to display image(s)
orig = image.ImageWin(img.getWidth(), img.getHeight(), "Original")
# new = image.ImageWin(img.getWidth(), img.getHeight(), "Negative")
sep = image.ImageWin(img.getWidth(), img.getHeight(), "Sepia")
red = image.ImageWin(img.getWidth(), img.getHeight(), "Remove All Red")
gray = image.ImageWin(img.getWidth(), img.getHeight(), "Gray Scale")


# ----------------------------------------------------------------------------------------------------------------------
# BEGIN PROGRAM"
# ----------------------------------------------------------------------------------------------------------------------

# draw the image on "orig" window frame
img.draw(orig)

# process and draw the image on "new" window frame
# negative(img, new)
sepia(img, sep)
remove_all_red(img, red)
gray_scale(img, gray)

# close window frame
orig.exitonclick()
# new.exitonclick()
sep.exitonclick()
red.exitonclick()
gray.exitonclick()
