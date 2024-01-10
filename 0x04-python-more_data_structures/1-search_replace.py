#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_l =[]
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_l.append(replace)
        else:
            new_l.append(my_list[i])
    return new_l
