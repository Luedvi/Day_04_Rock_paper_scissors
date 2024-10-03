# if we're using a python version older than 3.3 we have to create an __init__.py file inside the package. the file can be empty if we only want to have compatibility with older versions of python. The __init__.py files are required to make Python treat directories containing the file as packages (unless using a namespace package, a relatively advanced feature)

# if we use a python 3.3 version or newer the __init__.py file can also be used to initialize variables or imports to the package when it's called by an import in another file
print("the package has initialized")

hot_dog = "with ketchup and mayo"

# we need to import modules in the __init__.py so that they can be used with the proper namespace (packagename.modulename.item) in another file when the package is imported
import old_package.old_module2, old_package.old_module4
