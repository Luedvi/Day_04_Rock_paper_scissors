print("pathy initialize")

" These absolute and relative imports won't work if we run this file as a script, thats why we have to export it to the 'cool.py'"
# absolute imports: you can use them to refer to submodules of siblings packages For example, if the module new_package.human.mix needs to use the mix module in the new_package.inmortal package, it can use from sound.effects import echo.
from new_package.inmortal.mix import white_wizard
print(white_wizard)
# relative imports: These imports use leading dots to indicate the current and parent packages involved in the relative import. Note that relative imports are based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.
from . import elf2
print(elf2.war_elf2)

from .elf1 import grey_wizard
print(grey_wizard)

from .. import humans
print(humans.mix.gollum)

from .. inmortal import elf1
print(elf1.brown_wizard)
