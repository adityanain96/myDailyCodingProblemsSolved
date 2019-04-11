'''
This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. 
If at most two people can fit in a rescue boat, and the maximum 
weight limit for a given boat is k, determine how many boats will 
be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and 
a boat limit of 200, the smallest number of boats required will be three.
'''


def boats(wgt_lst, wgt_limit):
    wgt_lst.sort()
    if wgt_lst[-1] > wgt_limit:
        return -1
    
    num_boats = 0
    first , last = 0, len(wgt_lst)-1

    while first <= last:
        if wgt_lst[first] + wgt_lst[last] <= wgt_limit:
            num_boats += 1
            first += 1
            last -= 1
        else:
            last -= 1
            num_boats += 1
    return num_boats

print(boats([100,200,150,80],200))

'''
Hint
'''