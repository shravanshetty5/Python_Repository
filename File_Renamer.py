from os import listdir, rename
from os.path import isfile, join
def file_renamer():
    #Get File names from a folder
    mypath = "/Users/hadoop/GitHub/Python_Repository/prank"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    # For each file, rename file
    removeValues = "0123456789"
    for f in onlyfiles:
        rename(join(mypath, f), join(mypath, f.translate(None,removeValues)))

file_renamer()




