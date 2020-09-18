#! /usr/env/python3
"""
imagesizer.py
Program designed to resize images in bulk from a specified directory. Defaults to the current directory if none is specified.
The newWidth parameter should be an integer. The directory parameter can be relative or absolute, and is optional

"""

import os, sys
import logging
from pathlib import Path
import argparse

#logger.basicConfig(level=logger.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

logfile = Path.home()/Path('.imagesizer/imagesizer.log')
desiredLogLevel = logging.DEBUG

logger = logging.getLogger('Logger for image sizer program')
logger.setLevel(logging.DEBUG)

logFormatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

streamHandler = logging.StreamHandler()
streamHandler.setLevel(desiredLogLevel)
streamHandler.setFormatter(logFormatter)

fileHandler = logging.FileHandler(filename=logfile, mode='w')
fileHandler.setLevel(desiredLogLevel)
fileHandler.setFormatter(logFormatter)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

logger.debug(f"Logging has been established")


try:
    from PIL import Image
except ModuleNotFoundError as e:
    logger.debug(f"Error trying to import Pillow Image module: {str(e)}.\nHave you installed it?\nTry: pip3 install Pillow")
    sys.exit(1)

logger.debug("Importing complete, Starting parser setup.")

parser = argparse.ArgumentParser(description='Find all images in a directory and resize them into a new directory')

parser.add_argument('--source_dir', help='The directory to search for images', default=Path.cwd())
parser.add_argument('--dest_dir', help='The directory to put all of the resized images', default=Path.cwd()/Path('ResizedImages/'))
parser.add_argument('-w', '--width', help='The width in pixels to make the new images. Aspect ratio is always maintained', type=int, metavar='W', default=750)
parser.add_argument('-r', '--recursive', help='Whether to recursively search sub-directories from the main source directory or not', action='store_const', const=True, default=False)

if __name__ == "__main__":
    """
    main function
    """
    logger.debug("Beginning Main method")
    
    args = parser.parse_args()
    logger.debug(f"Established arguments passed in as:\n{str(args)}")

    #Step through all files within the directory path. If they are images, resize them with new width (maintain aspect ratio, so write a function for the resizing. May need a function to test if something is an image too...)

    #for imagePath in directoryPath.glob('*')
        
        #Call function to create a new image based on the current imagefile

    logger.debug("Finished Main method")




