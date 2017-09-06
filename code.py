# 1
# Replace if-else with try-except in the the example below:

def fourth_element_of_list(L):
    """
    Return the nth element of ``L`` if it exists, ``None`` otherwise.
    """
    
    try:
        return L[4]
    except:
        return None
    
    #if len(L) < i:
    #    return None
    #else:
    #    return L[i]

    
    
    
# 2
# Modify to use try-except to return the sum of all numbers in L,
# ignoring other data-types

def sum_of_numbers(L):
    """
    Return the sum of all the numbers in L.
    """
    s = 0
    for i in L:
        try:
            s=s+i
        except TypeError:
            pass
    return s
    
    
    #for l in L:
    #    if type(l) is int or type(l) is float:
    #        s += l
    #return s

# TEST
# sum_of_numbers([3, 1.9, 's']) == 4.9

