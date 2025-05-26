

class LibsMaster:

    def __init__(self):
        self.LIB=dict()

    def pypi_load(self, pypi_name, import_name):
        import pip
        pip.main(["install", pypi_name])
        self.LIB[import_name] = __import__(import_name)

    def load_single(self, pypi_name, import_name=None):
        if import_name is None:
            import_name=pypi_name

        try:
            self.LIB[import_name]=__import__(import_name)

        except ModuleNotFoundError:
            self.pypi_load(pypi_name, import_name)

        finally:
            if not import_name == pypi_name:
                self.LIB[pypi_name] = self.LIB[import_name]

    def load_iter(self, list_import):
        for name in list_import:
            self.load_single(name)

    def load_renamed(self, dict_import):
        for name, rename in dict_import.items():
            self.load_single(name, rename)

    def __getitem__(self, libname):
        if libname in self.LIB:
            self.LOAD(libname)
        self.LIB[libname]

    def LOAD(self, *args):
        if len(args)>1:
            self.load_iter(args)

        elif len(args)==1:
            if type(args[0]) is str:
                self.load_single(args[0])

            elif type(args[0]) is list:
                self.load_iter(args[0])

            elif type(args[0]) is dict:
                self.load_renamed(args[0])

        else:
            raise Exception("No args for LOAD")
        
def __init__():
    return LibsMaster()