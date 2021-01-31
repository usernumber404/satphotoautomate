import os
import shutil
import datetime


projectfolder = '' #path to folder
pathtodrive = '' #path to drive
currentdateandtime = datetime.datetime.now()
currentdateandtimestring = str(currentdateandtime)
perminatefolder = 'projections'
newfolder = currentdateandtimestring


def movefilesintofolder():
    os.chdir(projectfolder)
    os.mkdir(newfolder)
    for files in os.listdir():
            if files != perminatefolder:
                shutil.move(files, newfolder)



def checkifemptythenmove():
    if len(os.listdir(newfolder)) == 0:
        os.remove(newfolder)
    else:
        shutil.move(newfolder, pathtodrive)


movefilesintofolder()
checkifemptythenmove()

