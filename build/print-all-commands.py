import json
import datetime
import os

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


#class RattishDocPrepTool():

allCommandsAsciiInts = []
commandsDict = {}
namespaces = []
namespacesDict={}

def loadNamespacesTxt(nmspFile="namespaces.txt"):
    global namespaces
    with open(nmspFile,"r") as namespacesTxt:
        namespaces=parseRaw(namespacesTxt.read())
    print(f'namespaces loaded from "{nmspFile}"')
    print("[ \033[96m","\033[0m ; \033[96m".join(namespaces), "\033[0m ]")

def printCommandsInLine():
    global allCommandsAsciiInts
    print()
    print('     \033[01m\033[92m'+' '.join(list(map(lambda x: chr(x), allCommandsAsciiInts)))+'\033[0m ')
    print()

def writeAllCommandsTxt(separator='', outFile="all-commands.txt"):
    global allCommandsAsciiInts
    with open(outFile,"w") as allCommandsTxt:
        for i in allCommandsAsciiInts:
            allCommandsTxt.write(chr(i))
            allCommandsTxt.write(separator)



def readOldReadmeMd():
    global commandsDict
    readedlines=[]
    with open("../README.md","r") as oldreadme:
        readedlines=oldreadme.readlines()
    currentNamespace = "blank"
    for i in readedlines:
        if i.strip().startswith("###### ") and i.strip().endswith(" namespace"):
            currentNamespace = i.strip().lstrip("###### ").rstrip(" namespace")
        elif i.strip().startswith("- [") and "](./command-list/" in i:
            commandInfo=i.strip().split('](')
            hexKey=str(hex(ord(commandInfo[1].split(") [ `")[1][0])))
            description=commandInfo[0].lstrip("- [")
            commandsDict[hexKey]["description"]=description
            commandsDict[hexKey]["namespace"]=currentNamespace.lower()

commandExample={
    "namespace":"_____",
    "char":chr(0),
    "description":None,
    "details":""
}

def mapCommands(loadSource=None):
    global allCommandsAsciiInts, commandsDict, namespaces
    print("### mapping rattish commands ###")
    print()
    allCommandsAsciiInts = multiranger((33,47), (58,64), (91,96), (123,126))
    print("total command count: \033[94m", len(allCommandsAsciiInts), '\033[0m')
    printCommandsInLine()
    commandsDict = {}
    loadNamespacesTxt()
    print()
    for i in allCommandsAsciiInts:
        print('--- command \033[01m\033[31m', chr(i), hex(i), i, '\033[0m]')
        commandsDict[str(hex(i))]=commandExample.copy()
        if loadSource=="user":
            while not commandsDict[str(hex(i))]["namespace"] in namespaces:
                commandsDict[str(hex(i))]["namespace"] = input(f'what namespace is this? [ {" ; ".join(namespaces)} ] :>')
            commandsDict[str(hex(i))]["description"]=input(f'description :>')
        commandsDict[str(hex(i))]["char"]=chr(i)
    if loadSource=="old-readme":
        readOldReadmeMd()
    with open("commands.json","w") as commandsJsonIndex:
        commandsJsonIndex.write(json.dumps(commandsDict, indent=4))

#mapCommands("old-readme")

def writeCommandFromTemplate(hexKey, contentFill):
    templateText=""
    with open("command-details-template.md","r") as template:
        templateText=template.read()
    templateText=templateText.replace("<<<YEAR>>>", str(datetime.datetime.now().year))
    templateText=templateText.replace("<<<ASCIIHEX>>>", hexKey)
    templateText=templateText.replace("<<<ASCIIDEC>>>", str(ord(contentFill["char"])))
    templateText=templateText.replace("<<<ASCIICHAR>>>", contentFill["char"])
    templateText=templateText.replace("<<<DESCRIPTION>>>", contentFill["description"])
    templateText=templateText.replace("<<<NAMESPACE>>>", contentFill["namespace"].upper())
    with open(f'../command-list/{hexKey}.md',"w") as commandInfo:
        commandInfo.write(templateText)

def loadCommandsJson():
    global commandsDict
    with open("commands.json","r") as commandsJsonIndex:
        commandsDict=json.loads(commandsJsonIndex.read())

def createCommandLibrary():
    global commandsDict, namespaces
    for mdFile in os.listdir("../command-list"):
        os.remove("../command-list/"+mdFile)
    loadCommandsJson()
    loadNamespacesTxt()
    for hexKey in commandsDict:
        if commandsDict[hexKey]["namespace"] in namespaces:
            writeCommandFromTemplate(hexKey,commandsDict[hexKey])

namespaceDictTemplate={
    "description":"",
    "details":"",
    "commands":None
}

def loadNamespacesJson():
    global namespacesDict
    with open("namespaces.json","r") as namespacesJsonIndex:
        namespacesDict=json.loads(namespacesJsonIndex.read())

def namespacesToJson():
    global namespacesDict, namespaces
    loadNamespacesTxt()
    for group in namespaces:
        print("namespace "+group.upper())
        namespacesDict[group]=namespaceDictTemplate.copy()
        namespacesDict[group]["description"]=input("description :>")
    with open("namespaces.json","w") as namespacesJsonIndex:
        namespacesJsonIndex.write(json.dumps(namespacesDict, indent=4))

#namespacesToJson()

def writeMainReadme():
    global namespacesDict, namespaces, commandsDict
    templateText=""
    templateFiller=None
    loadNamespacesJson()
    loadCommandsJson()
    with open('readme-template.md',"r") as readmeFile:
        templateText=readmeFile.read()
    with open('readme-filler.json',"r") as readmeData:
        templateFiller=json.loads(readmeData.read())
    templateText=templateText.replace("<<<TEXTFIELD1>>>", templateFiller["textfield1"])
    templateText=templateText.replace("<<<TEXTFIELD2>>>", templateFiller["textfield2"])
    templateText=templateText.replace("<<<LANGASSUMPTIONS>>>", "\n- "+"\n- ".join(templateFiller["langassumptions"]))
    commandBlock=""
    for namespace in namespacesDict:
        #print(namespacesDict)
        commandBlock+=f'###### {namespace.upper()} namespace\n'
        commandBlock+="> "
        commandBlock+=namespacesDict[namespace]["description"]
        commandBlock+="\n\n"
        for command in commandsDict:
            if commandsDict[command]["namespace"]==namespace:
                commandBlock+=f'- [{commandsDict[command]["description"]}](./command-list/{command}.md) [` {commandsDict[command]["char"]} `]'
                commandBlock+="\n"
        commandBlock+="\n"
    templateText=templateText.replace("<<<COMMANDSLISTWITHNAMESPACES>>>", commandBlock)

    with open('../README.md',"w") as readmeFile:
        readmeFile.write(templateText)

writeMainReadme()

#createCommandLibrary()

#writeAllCommandsTxt("")


#def createCommandsJson():
#    global allCommandsAsciiInts, commands


#    with open("commands.json","w") as printAll:
