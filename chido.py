tejuino=1234567890

# entry point: is where the first instructions of a program are executed, and where the program has access to command line arguments. To start a program's execution, the loader or operating system passes control to its entry point.

# The simplest thing that you can do is treat your Python file as a self-contained script, that is running that file specifically, like when we run "main.py" or running this file (chido.py) from the shell by typing "python chido.py"

# additionaly we can import the code from one python file to another, the problem is that functionality is executed at import time
import cool
import ocean

# to prevent this we can use functions so the code only runs when we call it and not by importing it
def function_from_chido():
    print("here is a function from chido.py")

# __name__: is a special variable that python uses to know how the code is used. '__main__' is the name of the scope in which top-level code executes. A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive promp
if __name__ == "__main__":
    print(f"chido is running as a script with the __name__ variable set as {__name__}")
    
    print("here we write anythig that we want to execute when we run this python file as a script")
    import party
    import sauce
    function_from_chido()
else:
    print(f"chido is being imported by another file with the __name__ variable set as {__name__}")
    
    print("outside the 'if __name__ == __main__' we put anything we want to execute when the file is imported")

# https://dev.to/demianbrecht/entry-points-in-python-34i3
