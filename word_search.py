import os

def isItemInSearched(item):
    with open(item, "r") as f:
        cont = f.read()
        print(cont)
        if "nirav" in cont.lower():
            return True
        else:
            return False
    
if __name__ == "__main__":
    
    dir_content = os.listdir()
    count = 0
    for item in dir_content:
        if item.endswith('txt'):
            # print(item)
            print(f"Detecting the Nirav in {item}\n")
            
            flag = isItemInSearched(item)
            # print(flag)
            # print(cont)
            if(flag):
                print(f"Nirav is found in the {item}")
                count = count + 1
            else:
                print(f"Nirav is not found in the {item}")
            print(count)