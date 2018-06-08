# The built-in function dir() is used to find out which names a module defines.
# This is the one function in python which you should never forget. The good news is this also list the methods available for user defined objects.

# dir(object)

import time

if __name__ == '__main__':
    print(dir(dict()))