import rattish_manuals_helpers as RMH
import rattish_manuals_formating as RMF
import os
import json

commands = RMH.loadJson("commands")
namespaces = RMH.loadJson("namespaces")
print()
RMF.printNamespaces(namespaces, commands)

RMF.printUnused(namespaces, commands)

print("### all command codes ##")
print(json.dumps(RMH.listAllCommandsCodes()))
print()
print("### repository status ##")
print()
print(os.system("git status -s"))
print()
