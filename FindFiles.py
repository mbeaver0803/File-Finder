import os
import sys
import shutil
"WHAT DRIVE ARE WE LOOKING THROUGH?"
direc = str(input("Enter location program will be searching through\n\nC drive is 'C://'\n\n"))
fType = str(input("What type of file are we looking for?\n\nText files is '.txt'\n\n"))
fName = str(input("What do you want to name this folder?\n\n"))
newDirec = os.path.join(os.getcwd(), fName)
try:
    os.mkdir(newDirec)
except OSError:
    print("\n!!! Making Folder Failed !!!\n")
else:
    print("\n*** Making Folder Succeeded ***\n")
for root, directory, files in os.walk(direc): 
    for file in files:
        if file.endswith(fType):
            print(file)
            try:
                shutil.move(os.path.join(direc, file), newDirec)
            except FileNotFoundError:
                print("\n!!! Moving %s Failed !!!\n"%(file))
            else:
                print("\n*** Moving %s Succeeded ***\n"%(file))

