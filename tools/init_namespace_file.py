
import os
import unicodedata
import pathlib
import json
import sys

multirangers = lambda *args: [x for y in [list(range(*z)) for z in args] for x in y]

#print(rattish_rootdir)

def init_meaningfile(meaningspace,  rattish_rootdir = os.path.dirname(__file__)):
    
    spacedir = pathlib.Path(rattish_rootdir) / "meaningspace"

    if not os.path.exists(spacedir.resolve()):
        os.mkdir(spacedir.resolve())

    standard_space = [(chr(char),hex(char), char, unicodedata.name(chr(char)), unicodedata.name(chr(char)).lower().replace(" ","_").replace("-","")) for char in multirangers((32,48),(58,65),(91,97),(123,127))]
    
    with open((spacedir / f"{meaningspace}.py").resolve(), "w+") as manifest_file:
        manifest_file.write(f"\"\"\"Rattish initialized file ;; meaning_space={meaningspace} ' \"\"\"\n")
        manifest_file.write("\n# RATTISH PROJECT - https://github.com/rattish \n\n")
        for command in standard_space:
            manifest_file.write(f"def {meaningspace}___{command[4]}(core, string):\n")
            manifest_file.write(f"\t\"\"\"Rattish command ;; {meaningspace} , {command[3]} \"\"\"\n")
            manifest_file.write("\tif string.strip():\n\t\tpass #core.blank()\n\telse:\n\t\tpass #core.blank()")
            manifest_file.write("\n")
            manifest_file.write(f"\n\t#\tCHAR=\t{command[0]}")
            manifest_file.write(f"\n\t#\tDOCS=\t{command[1]}.md ")
            manifest_file.write(f"\n\t#\tASCII=\t{str(command[2])}")
            manifest_file.write(f"\n\t#\tNAME=\t{command[3]}")
            manifest_file.write(f"\n\t#\tFUNCTION=\t{meaningspace}___{command[4]}")
            manifest_file.write("\n\n")
            manifest_file.write(f"# RATTISH PROJECT - https://github.com/rattish/rattish/docs/commands/{command[1]}.md \n\n")
        
        manifest_file.write(f"\ndef main(core):\n")
        for command in standard_space:
            manifest_file.write(f"\n\tcore[{json.dumps(command[0])}] = {meaningspace}___{command[4]}")
        
        manifest_file.write("\n\n\t# RATTISH PROJECT - https://rattish.github.io/ \n\n")


if __name__ == "__main__":
    init_meaningfile(*sys.argv[1:])