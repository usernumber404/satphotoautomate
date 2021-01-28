import os
import ezgmail
import shutil

def main():
    movefilesintofolder()
    sendEmail()
    deleteleftovers()

def sendEmail():
    os.chdir(r'') #path to the folder python script is in
    ezgmail.send('','','', [''])
    #'email', 'subject', 'body',['pathtozip']

def movefilesintofolder():
    os.chdir('')  # change this to the filepath that you need
    os.mkdir('') #add path to folder you want to create
    for files in os.listdir():
        if files != '':  #change filename to whatever you do not want to delete
            shutil.move(files,'') #add path to folder made on line 18
    shutil.make_archive('','zip','')
    #'path to folder on line 18', 'zip', 'path to folder on line 18'
def deleteleftovers():
    os.remove('') #path to zip folder created on line 22
    shutil.rmtree('') #path to folder created on line 18
main()