#! /usr/env/python3
"""
imagesizer.py newWidth[, directory]
Program designed to resize images in bulk from a specified directory. Defaults to the current directory if none is specified.
The newWidth parameter should be an integer. The directory parameter can be relative or absolute, and is optional

"""

import os, sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

try:
   from PIL import Image
except ModuleNotFoundError as e:
   logging.debug(f"Error trying to import Pillow Image module: {str(e)}.\nHave you installed it?\nTry: pip3 install Pillow")
   sys.exit(1)

logging.debug("Importing complete, Starting program")

def usage():
   """
   Function to print the correct usage and quit. Invoked when user error is made.
   """
   logging.critical(f"Usage: imagesizer.py newWidth [, directory]")
   sys.exit(1)

def getArguments(argv=None):
   """
   Function to pull out the arguments provided to the function and provide input validation.
   """
   logging.debug(f"Commencing 'getArguments' function")
   logging.debug(f"At this point, __name__ is {__name__}")
   directoryPath = Path('.')
   logging.debug(f"The length of argv is {len(argv)}")
   if len(argv) < 2:
      logging.debug(f"Printing usage as arguments passed were insufficient: {str(argv)}")
      usage()
   
   elif len(argv) > 2:
      directoryPath = Path(argv[2])
      logging.debug(f"There where more than 2 arguments. Setting the directory path as {directoryPath}")
      if len(argv) > 3:
         logging.debug(f"Printing usage as there were more than 3 arguments: {argv}")
         usage()
   logging.debug("Attempting to extract the new width")
   try:
      #TODO: Strip a comma off the end of the next value. Python includes the comma with this argument, or the next argument depending on how you do it. Perhaps split it off the first and last (as well as spaces) char of all arguments.
      newWidth = int(argv[1])
      logging.debug(f"The extracted new width is {newWidth}.")
   except ValueError as e:
      logging.debug(f"Printing usage as the first argument was not an int: {argv[1]}")
      usage() 
   
   logging.debug(f"Finished getArguments function and returning {(newWidth, directoryPath)}")
   return (newWidth, directoryPath)

def main():
   """
   main function
   """
   logging.debug("Beginning Main method")

   logging.debug(f"Calling getArguments function with input: {str(sys.argv)}")
   newWidth, directoryPath = getArguments(sys.argv)
   logging.debug(f"Main function shows newWidth={newWidth} and directoryPath={directoryPath}")


   #TODO: Step through all files within the directory path. If they are images, resize them with new width (maintain aspect ratio, so write a function for the resizing. May need a function to test if something is an image too...)



   logging.debug("Finished Main method")

if __name__ == "__main__":
    main()

