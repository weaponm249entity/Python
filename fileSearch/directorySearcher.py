import os
import json

def browseFile(PATH):
    dirName = os.path.basename(PATH)
    fileData = {
        "directoryName" : dirName,
        "rootPath" : PATH,
        "files" : [],
        "subDirectories" : [],
        "pythonFiles" : [] 
    }
    fileList = os.listdir(PATH)
    for fileName in fileList:
        fullPath = os.path.join(PATH,fileName)
        if os.path.isdir(fullPath) == True:
            fileData["subDirectories"].append(browseFile(fullPath))
        if os.path.isfile(fullPath) == True:
            if fileName.endswith(".py") == True:
                fileData["pythonFiles"].append(fileName)
            else:
                fileData["files"].append(fileName)
    return fileData

targetDir = "/home/revenant/Github/Python/" #aranacak dizin
jsonFileName = "directory.json" #json ismi

fileData = browseFile(targetDir)

with open(jsonFileName, "w", encoding='utf-8') as jsonFile: #json a kayit etme
    json.dump(fileData, jsonFile, indent=4, ensure_ascii=False)