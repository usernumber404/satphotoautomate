import os
import shutil
import datetime


projectfolder = '/Users/jaredparker1/Desktop/testfolder'
pathtodrive = '/Users/jaredparker1/Google Drive/satphotos/'
currentdateandtime = datetime.datetime.now()
currentdateandtimestring = str(currentdateandtime)
perminatefolder = 'projections'
newfolder = pathtodrive + currentdateandtimestring


def movefilesintofolder():
    os.chdir(pathtodrive)
    os.mkdir(newfolder)
    os.chdir(projectfolder)
    for files in os.listdir():
            if files != perminatefolder:
                shutil.move(files, newfolder)


def checkifempty():
    if len(os.listdir(newfolder)) == 0:
        os.remove(newfolder)


movefilesintofolder()
checkifempty()
