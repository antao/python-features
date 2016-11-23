import re

if __name__ == '__main__':
    sentence= "a fat cat doesn't eat oat but a rat eats bats."
    
    findall = re.findall("[force]at", sentence)
    print(findall)
    
    # search = re.search("fat.*(animal|dog|zebra|cat)", sentence)
    
    # if search:
    #     print (search.group())
    #     print (search)