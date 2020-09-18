#! /usr/env/python3
"""
imagesizer.py
Program designed to resize images in bulk from a specified directory. Defaults to the current directory if none is specified.


"""

import os, sys
import logging
from pathlib import Path
import argparse


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
    logger.critical(f"Error trying to import Pillow Image module: {str(e)}.\nHave you installed it?\nTry: pip3 install Pillow")
    sys.exit(1)

logger.debug("Importing complete, Starting argument parser setup.")

parser = argparse.ArgumentParser(description='Find all images in a directory and resize them into a new directory')

parser.add_argument('--source_dir', help='The directory to search for images', default=Path.cwd())
parser.add_argument('--dest_dir', help='The directory to put all of the resized images', default=Path.cwd()/Path('ResizedImages/'))
parser.add_argument('-w', '--width', help='The width in pixels to make the new images. Aspect ratio is always maintained', type=int, metavar='W', default=750)
parser.add_argument('-r', '--recursive', help='Whether to recursively search sub-directories from the main source directory or not', action='store_const', const=True, default=False)

args = parser.parse_args()
logger.debug(f"Established arguments passed in as:\n{str(args)}")


logger.debug("Image Sizer setup complete.")


def convertDir(newWidth, source_Directory, dest_Directory=None, recursive=False):
    """
    Goes through a directory converting all images found into a new image with the new width.
    Steps through all files within the directory path. 
    If they are images, it will copy them to the destinaton directory and resize them with the new width (maintaining aspect ratio).
    """
    logger.debug(f"Commenced convertImagesInDir function with:\nnewWidth: {newWidth}\nsource_Directory: {source_Directory}\ndestination_Directory: {dest_Directory}\nrecursive: {recursive}")
    
    if dest_Directory is None:
        logger.debug(f"No destination directory provided. Creating a new one off source directory")
        dest_Directory = source_Directory/Path('/convertedImages')
    
    #TODO LOOK UP HOW TO DO A RECURSIVE GLOB!!!
    
    for imagePath in source_Directory.glob('*'):
        logger.debug(f"Looking through image files. Up to file {imagePath}")
        #TODO create a new image object based on the current imagefile
        
        #TODO Call function to resize image object
    
        #TODO Save new image in destination dir
    
    logger.debug("Completed function convertImagesInDir")

if __name__ == "__main__":
    """
    main function
    """
    logger.debug("Beginning Main function")
    

    convertDir(args.width, args.source_dir, args.dest_dir, args.recursive)


    logger.debug("Finished Main method")




