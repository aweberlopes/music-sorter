from os import walk
import os, sys
import logging

# Set Logging Config
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',  level=logging.DEBUG)

# Check Path in command
if len(sys.argv) < 2:
   logging.error("You have to specify a path example python3 .\\main.py C:\\Users\\weberlopes\\Musik")
   exit(2)

path=sys.argv[1]

logging.info("Start Musik-sorter on PATH: " + path)
logging.info("Check for avaiable folder and files")


# Check avaiable folder and files
f = []
d = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    d.extend(dirnames)
    break

# Check files for sorting avaiable
if f == []:
    logging.info("No Files to sort. Exit Programm")
    exit(3)

# Start sorting
logging.info("Start the sorting mechanism")
for file in f:
    folderName = file.split('-')[0].strip()
    
    # Create Folder if not avaiable and add Folder to directory list
    if not folderName in d:
        logging.info("Folder: " + folderName + " not found. Create new folder")
        os.mkdir(path +"\\" + folderName)
        d.append(folderName)
    logging.info("Move File: " + file + " to " + folderName)
    
    # Move File to the right folder
    os.replace(path +"\\" + file , path +"\\" + folderName + "\\" + file)

logging.info("Music Sorter done")   
