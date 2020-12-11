#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    param = dir(hidden_4)
    count = len(dir(hidden_4))

    for x in range(0, count):
        temp = param[x]
        if(temp[0] != '_'):
            print("{:s}".format(param[x]))
        else:
            continue
