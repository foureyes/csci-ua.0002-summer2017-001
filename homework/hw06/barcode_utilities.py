"""
barcode_utilities.py
=====

This file will contain two functions that will be used in a pre-written
program that generates barcodes based on numeric input. You'll write these
two functions and test them in this file. When you're certain that they work,
download both draw_barcode.py and upc.py from the homework listing and try
running draw_barcode.py. All of these files MUST BE IN THE SAME DIRECTORY.
(For example, if you are working off of your desktop, all of the files 
must be located on your desktop).

Implement the following two functions as specified in the docstrings below:

1. generate_bar_widths(s)
2. valid_barcode(s)

The docstrings are comments within the function that describes what the 
function does. There some notation below that specifies the parameters
and return of the functions:

:param name: -> a description of the parameter, name
:type name: -> the expected type of the parameter, name
:return: -> a description of the return value of the function
:rtype: -> the type of the return value of the function

Skim through the resources below for background information on generating
barcodes.

* https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding
* http://electronics.howstuffworks.com/gadgets/high-tech-gadgets/upc3.htm
* http://www.adams1.com/upccode.html

"""
def generate_bar_widths(s):
    """Takes a barcode number as a string and translates it to a series
    of bar widths (a string that consists of 1's, 2's, 3's and 4's with
    each number corresponding to a width of a bar). For example, a
    series of bar widths starting with '1113 ... ' would consists of
    a black single width bar, a white single width bar, a black single
    width bar... and then a white triple width bar'.

    generate_bar_widths('043000181706')
    # --> '11132111132141132113211321111111222112132221131232111114111'

    :param s: the number to be translated to a series of bar widths
    :type s: str
    :return: a string representing the width of each bar, including the
    start, middle and end patterns (111, 11111, and 111)
    :rtype: str
    """
    # TODO: implement this function!
    return ''

def valid_barcode(s):
    """Determines whether a barcode is valid or not based on length and
    the check digit. A "UPC-A" barcode consists of 12 digits, with the
    last digit being the check digit. Some examples:

    valid_barcode('036000291452') # --> True
    valid_barcode('036000291450') # --> False
    valid_barcode('075678164125') # --> True
    valid_barcode('')            # --> False

    :param s: barcode number
    :type s: str
    :return: true if the barcode is valid, false otherwise
    :rtype: bool
    """
    # TODO: implement this function!
    return True

if __name__ == '__main__':
    print('Test your functions here!')
    print(generate_bar_widths('075678164125'))
    # (should be 11132111312123111141312121311111222111141132222121221231111)

    print(valid_barcode('075678164125'))
    # (should be valid!)




