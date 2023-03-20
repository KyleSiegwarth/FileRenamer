# add a drop down to search for specific file types
# add an option to recursively change file names in all sub directories  will have to use something like an os.walk
# add a way to check/ deal with member not having permissions to folder.
# request the user to add the basic filename found in all files so that you can change only the portion that matters to the end.
# provide the user with a count of the files in directory and how the naming convention is.
# entry widget to allow changing of default naming convention.
import os
from tkinter import *
from tkinter.filedialog import askdirectory

srcPath = ""
dstPath = ""
root = Tk()
root.title("Renamer")

def grabPath(Label, path, isSource): #(Label, path)
    path = askdirectory(title="Select Folder") #shows dialog box and returns the path
    if path == "":
        Label.config(text="Please enter a valid Path")
        runBtn.config(state="disabled")
    else:
        if isSource == True:
            global srcPath
            srcPath = path
        else:
            global dstPath
            dstPath = path
        if ":" in srcPath and ":" in dstPath:
            runBtn.config(state="normal")
            print("good to go")
        else: runBtn.config(state="disabled")
        Label.config(text=path)
        print("Files and directories in ", path, ":")
        #print(os.listdir(path))
def warningMessage(srcPath, dstPath):
    files = os.listdir(srcPath)
    extention = files[0][-4:] #last 4 characters
    exampleTxt = " 1 Example of " + str(len(files)) + " files.\n   Before: " + files[0] + "\n   After: " + (files[0][0:-4] + files[0][0] + extention) 
    if ":" in srcPath and ":" in dstPath:
        print("2 valid paths")
    else:
        print("not valid path entries") 
        runBtn.config(state="disabled")
        return
    # if path is "~~~ Path or Please enter a valid path" then don't run.
    files = os.listdir(srcPath)
    global warningWin
    warningWin = Toplevel(root)
    warningWin.grab_set()
    warningWin.title("Warning")
    warningLabel = Label(warningWin, text="Change files in: " + srcPath + "\n to " + dstPath)
    warningLabelEx = Label(warningWin, text=exampleTxt)
    warningBtnRight = Button(warningWin, text="Yes", command=changeNames)
    warningBtnLeft = Button(warningWin, text="No", command=warningWin.destroy)
    warningLabel.pack()
    warningLabelEx.pack()
    warningBtnLeft.pack(side="left")
    warningBtnRight.pack(side="right")
def changeNames():
    for item in os.listdir(srcPath):
        os.rename(srcPath + "/" + item, dstPath + "/" + item[0:-4] + item[0] + item[-4:])
        print(srcPath + "/" + item + " to: " + dstPath + "/" + item[0:-4] + item[0] + item[-4:])
    warningWin.destroy()

topLabel = Label(text="Hello! Please choose a path for files to be renamed.")
srcLabel = Label(text="Source Path")
srcBtn = Button(text="click to choose source directory.", command=lambda : grabPath(srcLabel, srcPath, True))
dstLabel = Label(text="Destination Path")
dstBtn = Button(text="click to choose destination directory.", command=lambda : grabPath(dstLabel, dstPath, False))
runLabel = Label(text="Would you like to run the name changing?")
runBtn = Button(text="Change Names", command=lambda : warningMessage(srcPath, dstPath), state="disabled")
topLabel.pack()
srcLabel.pack()
srcBtn.pack()
dstLabel.pack()
dstBtn.pack()
runLabel.pack()
runBtn.pack()
root.mainloop()
