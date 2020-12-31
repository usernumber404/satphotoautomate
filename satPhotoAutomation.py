import os

os.chdir('add file path here') #change this to the filepath that you need
def deletefiles():
    for files in os.listdir():
        if files != 'DONOTDELETE':  #change filename to whatever you do not want to delete
            os.remove(files)
            #print(files)    #to test this code add a pound sign in front of os.remove(files)
                            #then remove the pound sign in front of the print statement.

deletefiles()