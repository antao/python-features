import time
import pdb

if __name__ == '__main__':
    start = time.time()
    integer = 1
    pdb.set_trace()
    integer += 1
    print(dir(dict()))
    pdb.set_trace()
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 