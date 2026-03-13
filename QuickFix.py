
import os
import easygui
def main():
    filepath = easygui.fileopenbox()



        


def filterFiles(file):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.webp') or file.endswith('.jpeg'):
        return True
    return False
def getAlterName(file):
     return file.split("_")[0].split(".")[0]

if __name__ == "__main__":
    main()
    