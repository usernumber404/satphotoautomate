import os
import shutil
import datetime


projectfolder = ''   #path to folder
pathtodrive = ''   #path to drive DO NOT FORGET TO ADD AN / to the end
currentdateandtime = datetime.datetime.now()
currentdateandtimestring = str(currentdateandtime)
perminatefolder = ''  #name of projections folder
newfolder = currentdateandtimestring


def movefilesintofolder():
    os.chdir(projectfolder)
    os.mkdir(newfolder)
    for files in os.listdir():
        if files != perminatefolder:
            shutil.move(files, newfolder)


def checkifemptythenmove():
    if len(os.listdir(newfolder)) == 0:
        os.rmdir(newfolder)
    else:
        shutil.move(newfolder, pathtodrive)


def main():
    movefilesintofolder()
    checkifemptythenmove()