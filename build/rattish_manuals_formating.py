
def newNamespaceJsonElement():
    return {
        "description":"",
        "details":"",
        "modes":[]
    }

def newCommandJsonElement():
    return {
        "namespace":"_____",
        "char":chr(0),
        "description":None,
        "details":""
    }

def unusedCommandsSection(namespaces, commands):
    out=""
    out+=f'###### *still undefined commands* \n'
    for hexId in commands:
        if not commands[hexId]["namespace"] in namespaces:
            out+='- [undefined function for that moment](./command-list/'
            out+=hexId
            out+='.md) [` '
            out+=commands[hexId]["char"].replace('`', '``')
            out+=' `]'
            out+="\n"
    out+="\n"
    return out

def namespacesCommandSection(namespaces, commands):
    out=""
    for group in namespaces:
        #print(namespacesDict)
        out+=f'##### {group.upper()} namespace\n'
        out+="> "
        out+=namespaces[group]["description"]
        out+="\n\n"
        for hexId in commands:
            if commands[hexId]["namespace"]==group:
                out+='- ['
                out+=commands[hexId]["description"]
                out+='](./command-list/'
                out+=hexId
                out+='.md) [` '
                out+=commands[hexId]["char"].replace('`', '``')
                out+=' `]'
                out+="\n"
        out+="\n"
    return out

def basicListing(inputList):
    return "\n - "+"\n - ".join(inputList)

def itemListing(inputDict):
    out=""
    for keyname in inputDict:
        out+=f' - __{keyname}__ : {inputDict[keyname]} '
        out+="\n"
    return out

def exampleListing(inputDict):
    out=""
    for keyname in inputDict:
        out+=" - ["
        out+=" ".join(keyname.split("-"))
        out+="](./examples/"
        out+=keyname
        out+="/README.md) : \n"
        for item in inputDict[keyname]:
            out+=f' - - {item} \n'
        out+="\n"
    return out

def projectsListing(inputDict):
    inputDict=inputDict.copy()
    out=""
    for keyname in inputDict:
        link=inputDict[keyname].pop()
        out+=f' - [__{keyname}__]({link})'
        if len(inputDict[keyname])!=0:
            out+=" - "
            out+=" ; ".join(inputDict[keyname])
        out+="\n"
    return out

def printNamespaces(namespaces, commands):
    raport={}
    for group in namespaces:
        raport[group]={"count":0,"all-commands":""}
    for hexKey in commands:
        if commands[hexKey]["namespace"] in raport:
            nam=commands[hexKey]["namespace"]
            raport[nam]["count"]+=1
            raport[nam]["all-commands"]+=commands[hexKey]["char"]
    print("### Namespaces Raport ###")
    for group in raport:
        print()
        print("---", group.upper(), "\tcommands count:",  raport[group]["count"])
        print()
        print("\t\t", raport[group]["all-commands"])
    print()
    return raport

def printUnused(namespaces, commands):
    raport={"count":0,"all-commands":""}
    for hexKey in commands:
        if not commands[hexKey]["namespace"] in namespaces:
            #nam=commands[hexKey]["namespace"]
            raport["count"]+=1
            raport["all-commands"]+=commands[hexKey]["char"]
    print("### Unused Raport ###")
    #for group in raport:
    print()
    print("--- <blank>\tcommands count:",  raport["count"])
    print()
    print("\t\t", raport["all-commands"])
    print()
    return raport
