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
parser.add_argument('-w', '--width', help='The width in pixels to make the new images. Aspect ratio is always maintained', type=int, metavar='W', default=720)
parser.add_argument('-r', '--recursive', help='Whether to recursively search sub-directories from the main source directory or not', action='store_const', const=True, default=False)

args = parser.parse_args()
logger.debug(f"Established arguments passed in as:\n{str(args)}")


logger.debug("Image Sizer setup complete.")

def isImageFilename(filename):
    """
    checks to see whether a filename is a valid image file type (extension).
    Returns true if it is, false otherwise.
    """
    logger.debug(f"Commencing function 'isImageFilename' with filename {filename}")
    
    listOfImageExtensions = [".jpg", ".png", ".tiff", ".bmp", ".gif"]

    filename = getPath(filename)

    if filename.suffix.lower() in listOfImageExtensions:
        logger.debug(f"Found the image extension {filename} within list of Image extensions {str(listOfImageExtensions)}. Returning True.")
        return True
    logger.debug(f"Did not find the extension of {filename} within the list of Image extensions {str(listOfImageExtensions)}. Returning False.")
    return False

def getPath(filePath):
    """
    Function to check to see if a parameter is actually a file path, and attempt to convert it if it isn't. Returns the object passed in if it is a path, and a path object otherwise (if it can).
    """
    logger.debug(f"Started function 'getPath' with file {filePath} whose type is {type(filePath)}") 
    if type(filePath) != type(Path.cwd()):
        logger.debug(f"User didn't pass a Path object. Attempting to correct this")
        filePath = Path(filePath)
    logger.debug(f"Returning object whose type is {type(filePath)}.")
    return filePath

def convertImage(imagePath, destDir=Path.cwd(), width=720):
    """
    Function to convert a single image to a new size (based on its width).
    If not provided, the new width becomes the default of 720.
    """
    logger.debug(f"Commenced function 'convertImage' with:\nimage path:{imagePath}\ndestinationDirectory: {destDir}\nWidth: {width}")
    
    #ensure we are working with Path objects
    imagePath = getPath(imagePath)
    destDir = getPath(destDir)

    #TODO create a new image object based on the current imagefile
    
    #TODO Call function to resize image object
    
    #TODO Save new image in destination dir
    
    logger.debug("Completed convertImage function")



def convertDir(newWidth, source_Directory, dest_Directory=None, recursive=False):
    """
    Goes through a directory converting all images found into a new image with the new width.
    Steps through all files within the directory path. 
    If they are images, it will call 'convertImage' function on them.
    """
    logger.debug(f"Commenced convertImagesInDir function with:\nnewWidth: {newWidth}\nsource_Directory: {source_Directory}\ndestination_Directory: {dest_Directory}\nrecursive: {recursive}")
    
    if dest_Directory is None:
        logger.debug(f"No destination directory provided. Creating a new one off source directory")
        dest_Directory = source_Directory/Path('/convertedImages')
    
    
    for thisFolder, subFolders, filenames in os.walk(source_Directory):
        logger.debug(f"Walking through {source_Directory}. This folder is {thisFolder}. Sub-folders are \n{str(subFolders)}\nfilenames are {str(filenames)}")
        
        if not recursive:
            logger.debug(f"Since this call is not recursive, removing subFolders {str(subFolders)}")
            subFolders.clear()
            logger.debug(f"The subfolders list is now {str(subFolders)}.")
        
        for filePath in filenames:
            logger.debug(f"Checking to see whether {filePath} has an image extension")
            if isImageFilename(filePath):
                logger.debug(f"The file {filePath} is an image file.")
                convertImage(os.path.join(thisFolder, filePath), dest_Directory, newWidth)
                
        logger.debug(f"Completed looking at the files in directory '{thisFolder}'. Moving to next")
    
    logger.debug("Completed function convertImagesInDir")

if __name__ == "__main__":
    """
    main function
    """
    logger.debug("Beginning Main function")
    

    convertDir(args.width, args.source_dir, args.dest_dir, args.recursive)


    logger.debug("Finished Main method")




