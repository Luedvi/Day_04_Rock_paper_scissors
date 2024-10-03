tuba="deliciosa"
balnearios=["chimulco","agua caliente","tobolandia"]

print("cool.py is running")

# package: is a folder that contains one or more modules. the abbreviation for package is "pkg"

#importing one module from a package
import another_package.my_module3
print(another_package.my_module3.func5())
print(another_package.my_module3.func6())

# importing one module with "from" keyword
from awesome_package import my_module1
print(my_module1.func1())
print(my_module1.func2())

#importing one module with alias
from awesome_package import my_module1 as godzilla
print(godzilla.func1())
print(godzilla.func2())

#importing individual items from one module
from awesome_package.my_module2 import func3
print(func3())
# this would be a NameError because func4 hasn't been imported yet
"print(func4())"

# import old_package containing __init__.py
from old_package.old_module1 import old_func1
print(old_func1())
# the __init__.py only initialize one time regardless of how many times it's called, this is the same behavior for python 3.3 or newer versions that don't need to have the __init__.py file
from old_package.old_module1 import old_func2
print(old_func2())

# we can call the variables inside the __init__.py of the package directly because they have been initialized
import old_package
print(old_package.hot_dog)

# import package module
import old_package.old_module3
print(old_package.old_module3.old_func5())

# import package module with an alias
import old_package.old_module3 as godzuki
print(godzuki.old_func6())

# we can access this namespace only because it is previously imported in the __init__.py of the "old_package"
print(old_package.old_module2.old_func3())
print(old_package.old_module4.old_func7())

# Now what happens when the user writes from packagename.packagename import *? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported. The only solution is for the package author to provide an explicit index of the package with the "__all__" variable

# this works thanks to the "__all__" variable in the __init__ of the "inmortal" package
from new_package.inmortal import *
print(elf1.war_elf1)
print(elf2.war_elf2)
# the module elf3 is being shadowed by a locally defined name in the __init__ file of the "inmortal" package thus raising an error
"print(elf3.war_elf3)"

# there is nothing wrong with using "from package import specific_submodule" In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.
from new_package.humans import mix
from new_package.inmortal import mix
# this raises an error because humans.mix has been replaced with inmortal.mix
"print(mix.character_mix1)"
print(mix.character_mix2)
# the solution is using a different syntax
from new_package import humans
print(humans.mix.character_mix1)

import new_package.humans.mix
print(new_package.humans.mix.character_mix1)

# we can use absolute and relative imports(go to new_package/inmortal/pathy for details)
import new_package.inmortal.pathy
