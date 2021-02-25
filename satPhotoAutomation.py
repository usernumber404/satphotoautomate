import os
import shutil
import datetime
import sys


projectfolder = ''   #path to folder
pathtodrive = ''   #path to drive DO NOT FORGET TO ADD AN / to the end
currentdateandtime = datetime.datetime.now()
currentdateandtimestring = str(currentdateandtime)
perminatefolder = 'projections'  #name of projections folder
newfolder = pathtodrive + currentdateandtimestring


def checkfolder():
    if len(os.listdir(projectfolder)) > 2:
        os.mkdir(newfolder)
    else:
        #print('exit')
        sys.exit()


def movefilesintofolder():
    os.chdir(projectfolder)
    for files in os.listdir(projectfolder):
        if files != perminatefolder:
            shutil.move(files, newfolder)


def main():
    checkfolder()
    movefilesintofolder()



