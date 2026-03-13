
import os
def main():
    walk_directory(".")

def walk_directory(root_dir):
    names = []
    for _, _, files in os.walk(root_dir):
        for file in files:
            if filterFiles(file):
                name = getAlterName(file)
                if name not in names:
                    names.append(name)
                    os.mkdir(name)
                os.rename(file, os.path.join(name, file))
                         

        


def filterFiles(file):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.webp') or file.endswith('.jpeg'):
        return True
    return False
def getAlterName(file):
     return file.split("_")[0].split(".")[0]

if __name__ == "__main__":
    main()
    