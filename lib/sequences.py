#!/usr/bin/env python3

def print_fibonacci(length):
    new_list = []
    if length == 0:
        print(new_list)
        return
    elif length == 1:
        new_list.append(0)
        print(new_list)
        return
    elif length == 2:
        new_list = [0,1]
        print(new_list)
        return
    else:
        new_list = [0,1]
        start1 = new_list[-2]
        start2 = new_list[-1]
        i = length - 2
        while i > 0:
            new_num = start1 + start2
            new_list.append(new_num)
            start1 = start2
            start2 = new_num
            i = i - 1
        print(new_list)
        return
print_fibonacci(100)
        
            
