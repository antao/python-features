# Reduce a list to a single value by combining elements via a supplied function

from functools import reduce

# "If the python interpreter is running the source file as the main program, it sets the special __name__ variable to have a value "__main__"."
# "If this file is being imported from another module, __name__ will be set to the module's name."

if __name__ == '__main__':
    
    items = [1, 2, 3, 4]

    # Reduce it is not an iterator itself. 
    # Reduce passes the current product at each step along with the next item from the list to the lambda function
   
    print(reduce((lambda x, y: x * y), items))