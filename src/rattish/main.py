
# meaningspace = "default"

# definitions = f"""
# class {meaningspace.capitalize()}RattishMeanings(RattishMeanings):
#     core = None
#     charmap = None
# """

# assignings = """
#     def assign_meanings(self):
        
# """


#definitions=""


import unicodedata
import pathlib
import hashlib
import zlib
import json
import inspect
import ast
import time
import os






# def init_meaningspace(meaningspace, rattish_rootdir = os.path.dirname(__file__)):
    
#     spacedir = pathlib.Path(rattish_rootdir) / "meaningspace"

#     if not os.path.exists(spacedir.resolve()):
#         os.mkdir(spacedir.resolve())

#     standard_space = [(chr(char),hex(char), char, unicodedata.name(chr(char)), unicodedata.name(chr(char)).lower().replace(" ","_")) for char in multirangers((32,48),(58,65),(91,97),(123,127))]

#     for command in standard_space:
#         #py_file= spacedir / f"{zlib.adler32(f"{meaningspace}___{x[4]}")}.py"
#         py_file = spacedir / f"{meaningspace}___{command[4]}.py"
#         with open(py_file.resolve(), "w") as codefile:
#             codefile.write(f"\"\"\"Rattish initialized file ;; meaning_space={meaningspace} , command_char='{command[3]}' \"\"\"\n")
#             codefile.write("\n# RATTISH PROJECT - https://github.com/rattish \n\n")
#             codefile.write("def __init__(core, string):\n")
#             codefile.write(standard_command)
#         #definitions+=
#         #definitions+=f"{x[4]}(core, string)"

#         #definitions+=":\n"
#         #definitions+=standard_command


#     #print((spacedir / f"{meaningspace}.json").resolve())

#     with open((spacedir / f"{meaningspace}.json").resolve(), "w+") as manifest_file:
#         manifest_file.write(
#             json.dumps({
#                 x[4]:{
#                     "asciicode":x[2],
#                     "docs":str((pathlib.Path(rattish_rootdir) / "docs" / "commands" / meaningspace / f"{x[1]}.md").resolve()),
#                     #"meanings_file":f"./meaningspace/{meaningspace}.py",
#                     "meanings_file":str((spacedir / f"{meaningspace}___{x[4]}.py").resolve()),
#                     #"def":f"{x[4]}(core, string)",
#                     "def":"__init__(core, string)",
#                     "label":x[3],
#                     "call_char":x[0]
#                 } for x in standard_space
#             }, indent=4)
#         )


# class RattishMeaning:
    
        
#     def __getitem__(self, key=None):
#         if key is None or key not in self.charmap:
#             raise KeyError(self, key)
#         return self.charmap[key]


# class RattishMemory:
#     def __init__(self):
#         pass



class RattishProcessor:

    #standard_namespace = [(chr(char),hex(char), char) for char in multirangers((33,47),(58,64),(91,96),(123,126))]

    #rattish_rootdir = os.path.dirname(__file__)
    mode = None
    meaning_modes = dict()
    memory = None
    context = None
    charmap = None

    # def __mul__(self, meaningspace):

    #     meaning_dict = None

    #     with open((pathlib.Path(self.rattish_rootdir)/"meaningspace"/f"{meaningspace}.json").resolve()) as manifest:
    #         meaning_dict = json.loads(manifest.read())

    #     for item in meaning_dict:
    #         to_import = str((pathlib.Path(self.rattish_rootdir)/"meaningspace"/meaning_dict[item]["meanings_file"]).resolve())
    #         self[meaning_dict[item]["call_char"]] = __import__(to_import)

    #def __truediv__(self, meaningspace):
    #    pass
    
    def memsafe_acc(self):
        self.standart_checkup()
        if "ACC" not in self.memory:
            self.memory["ACC"] = 0

    def memsafe_context(self):
        self.standart_checkup()
        if self.context not in self.memory:
            self.memory[self.context] = 0
            
    def __init__(self, shared_inherits=None):
        # if shared_inherits is not None:
        #     if "memory" in shared_inherits:

        #     if "charmap" in shared_inherits:

        #     if "context" in shared_inherits:
        #         self.

        self.standart_checkup()
        #print("namespace")
        #self[">"] = lambda core, input_args: core.output_handler(input_args) 
        #self["<"] = lambda core, input_args: core.input_handler(input_args)
        #self["$"] = lambda core, input_args: core.point_to_context(input_args)
        #self["="] = lambda core, input_args: core.assign_context_value(input_args)
        #self["@"] = lambda core, input_args: core.load_import(input_args)
        
    def standart_checkup(self):
        if self.memory is None or not len(self.memory):
            self.memory = {"UNIXUSAT": int(time.time()*1000)}
        if self.context is None or not self.context.strip():
            self.context = next(iter(self.memory))
        if self.charmap is None or not len(self.charmap):
            self.charmap = {}
            from rattish.meaningspace import default
            default.main(self)
            self.mode = "default"
            self.meaning_modes["default"] = default

        #if not name is None:
            
        #return (self.context, name, self.context in self.memory)


    def __getitem__(self, key=None):
        if key is None or key not in self.charmap:
            raise KeyError(self, key)
        return self.charmap[key]
    
    def __setitem__(self, key=None, instruction=None):
        if key is None or instruction is None:
            raise IsADirectoryError(self, key, instruction, "key and data must BE")

        self.charmap[key] = instruction

    def __str__(self):
        return json.dumps({
            x: "->".join([
                str(inspect.signature(self.charmap[x])),
                str(zlib.adler32(str.encode(ast.dump(ast.parse(inspect.getsource(self.charmap[x]))))))
            ]) for x in self.charmap
        }, indent=4)

    def __repr__(self):
        return json.dumps([
            {
                "command": x,
                "signature": str(inspect.signature(self.charmap[x])),
                "adler32":zlib.adler32(str.encode(ast.dump(ast.parse(inspect.getsource(self.charmap[x]))))),
                "ASDL": ast.dump(ast.parse(inspect.getsource(self.charmap[x])), indent=4).split("\n")
            } for x in self.charmap
        ], indent=4)
    
    def __add__(self, added=None):
        #print(json.dumps(added))
        for line in added.split("\n"):
            if line.strip():
                if line[0] in self.charmap:
                    self.standart_checkup()
                    self.charmap[line[0]](self, line[1:])
        
        #return repr(self)


