
import os
def main():
    for dirsRoot, dirs, _ in os.walk("./Pictures"):
        for dir in dirs:
            images = []
            for root, _, files in os.walk(os.path.join(dirsRoot, dir)):
                for file in files:
                    if not imageInArr(os.path.join(root, file), images):
                        images.append(os.path.join(root, file))
                    else:
                        print("Deleting "+os.path.join(root, file))
                        os.remove(os.path.join(root, file))

                        



def imageInArr(img, arr):
    return True in [compareImages(img, x) for x in arr ]

def compareImages(a, b):
    return os.path.getsize(a) == os.path.getsize(b)
        


def filterFiles(file):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.webp') or file.endswith('.jpeg'):
        return True
    return False
def getAlterName(file):
     return file.split("_")[0].split(".")[0]

if __name__ == "__main__":
    main()
    