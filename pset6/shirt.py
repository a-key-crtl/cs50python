# program overlays shirt from one file onto anoth
#
#

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    # Open image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open shirt
    shirtfile = Image.open("pset6/shirt.png")
    # Get size of shirt
    size = shirtfile.size
    # Resize muppet image to fit shirt
    muppet = ImageOps.fit(imagefile, size)
    # Paste shirt in muppet
    muppet.paste(shirtfile, shirtfile)
    # create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    # Check number of elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    # check if it is a Image file
    if check_extension(file1[1]) is False or check_extension(file2[1]) is False:
        sys.exit("Invalid output")
    # Check if extension of both files are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")
def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False
    
if __name__ == "__main__":
    main()