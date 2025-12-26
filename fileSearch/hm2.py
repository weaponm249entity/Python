#Using recursive make a program that lists all the files inside a directory.
import os

def browseFile(PATH):
    files = []
    fileList = os.listdir(PATH)
    for fileName in fileList:
        fullPath = os.path.join(PATH,fileName)
        if os.path.isdir(fullPath) == True:
            print(fileName,"is a directory:",{fullPath})
            print(f"Opening directory: {fullPath}")
            print("-"*50)
            browseFile(fullPath)
        if os.path.isfile(fullPath) == True:
            print(fileName,"is a file")
            print("-"*50)
            files.append(fileName)
        else:
            with os.scandir(fullPath) as it:
                if not any(it):
                    print("Directory is empty")
                    print("-"*50)
    return files


print(browseFile("/home/revenant/Github/"))

## HM
# Save data to a JSON file
# Make a structured data
# Filter all .py files