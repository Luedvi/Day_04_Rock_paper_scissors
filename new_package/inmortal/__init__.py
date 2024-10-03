# __all__ variable: it is taken to be the list of module names that should be imported when "from package import *" is encountered
__all__ = ["elf1", "elf2", "elf3"]

# Be aware that submodules might become shadowed by locally defined names, for example, if you added an "elf3" variable to the new_package/inmortal/__init__.py file, the "from new_package.inmortal import *" would only import the two submodules elf1 and elf2, but not the elf3 submodule, because it is shadowed by the locally defined elf3 variable
elf3 = "wrong"
