import json
import datetime
import os

# parse raw text to

def pathTo(*item):
    item=list(item)
    item.insert(0, os.path.dirname(__file__))
    return os.path.join(*item)

def fRead(*item):
    return open(pathTo(*item),"r")

def fWrite(*item):
    return open(pathTo(*item),"w")

def currentYear():
    return str(datetime.datetime.now().year)

def parseRaw(rawOutput):
    return list(
        filter(
            lambda line: line.strip()!='',
            rawOutput.split("\n")
        )
    )

def multiranger(*rangesList):
    result=[]
    for item in rangesList:
        result+=range(item[0],item[1]+1)

    return result

def loadTxt(file):
    out=""
    with fRead('data',file+'.txt') as filehook:
        out=parseRaw(filehook.read())
    return out

def saveTxt(file, contentlist):
    with fWrite('data',file+'.txt') as filehook:
        filehook.write("\n".join(contentlist))
        filehook.write("\n")

def loadJson(file):
    out=None
    with fRead('data',file+'.json') as filehook:
        out=json.loads(filehook.read())
    return out

def saveJson(file, content):
    with fWrite('data',file+'.json') as filehook:
        filehook.write(json.dumps(content, indent=4))

def createMdUsingTemplate(templateFile, fillingDictionary, outputFile):
    templateText=""
    with fRead('templates',templateFile+'.md') as template:
        templateText=template.read()

    for fillGap in fillingDictionary:
        templateText=templateText.replace(
            f'<<<{fillGap.upper()}>>>',
            fillingDictionary[fillGap]
        )
    with fWrite('..', outputFile) as outHook:
        outHook.write(templateText)

def listAllCommandsCodes():
    return multiranger((33,47), (58,64), (91,96), (123,126))

def listExamples():
    examples={}
    for item in os.listdir(pathTo("..","examples")):
        if os.path.isdir(pathTo("..","examples", item)):
            examples[item]=os.listdir(pathTo("..","examples",item))
    return examples
