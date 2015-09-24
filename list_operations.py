
"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the above
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.

DO NOT USE ANY OF THE BUILT IN LIST METHODS, OR len(input_list)
"""

def head(input_list):
    """
        Return the first element of the input list.
        [ A, B, C, D, E, F ] --> A
    """
    return input_list[0]
    pass

def tail(input_list):
    """
        Return all elements of the input list except the first.
        [ A, B, C, D ] --> [ B, C, D ]
    """
    return input_list[1:]
    pass

def last(input_list):
    """
        Return the last element of the input list.
        [ A, B, C, D ] --> D
    """
    return input_list[-1]
    pass

def init(input_list):
    """
        Return all elements of the input list except the last.
        [ A, B, C, D ] --> [ A, B, C ]
    """
    return input_list[:-1]
    pass

"""
Do yourself a favor and get a short code review here.
You can also get reviewed by a neighbor who has been reviewed.
"""

def first_three(input_list):
    """
        Return the first three elements of the input list.
        [ A, B, C, D, E, F ] --> [ A, B, C ]
    """
    return input_list[:3]
    pass

def last_five(input_list):
    """
        Return the last five elements of the input list.
        [ A, B, C, D, E, F ] --> [ B, C, D, E, F ]
    """
    return input_list[-5:]
    pass

def middle(input_list):
    """
        Return all elements of the input list except the first two and the last two.
        [ A, B, C, D, E, F ] --> [ C, D ]
    """
    return input_list[2:-2]
    pass

def inner_four(input_list):
    """
        Return the third, fourth, fifth, and sixth elements of the input list.
        [ A, B, C, D, E, F, G ] --> [ C, D, E, F ]
    """
    return input_list[2:6]

    pass

def inner_four_end(input_list):
    """
        Return the sixth, fifth, fourth, and third elements from the end of the 
        list, in that order.
        [ A, B, C, D, E, F, G, H, I, J, K, L] --> [ G, H, I, J ]
    """
    return input_list[-6:-2]
    pass

def replace_head(input_list):
    """
        Replace the head of the input list with the value 42.
        [ A, B, C, D ] --> [ 42, B, C, D]
    """
    input_list[0]=42
    return input_list
    pass

def replace_third_and_last(input_list):
    """
        Replace the third and last elements of the input list with the value 37.
        [ A, B, C, D, E, F ] --> [ A, B, 37, D, E, 37 ]
    """
    input_list[2]=37
    input_list[-1]=37
    return input_list
    pass

def replace_middle(input_list):
    """
        Replace all elements of the input list with the the values 42 and 37, in
        that order, except for the first two and last two elements.
        [ A, B, C, D, E, F, G, H, I ] --> [ A, B, 42, 37, H, I ] 
    """
    input_list[2:-2]=[42,37]
    return input_list
    pass

def delete_third_and_seventh(input_list):
    """
        Remove the third and seventh elements of the input list.
        [ A, B, C, D, E, F, G, H ] --> [ A, B, D, E, F, H ]
    """
    del input_list[2]
    del input_list[5]
    return input_list
    pass


def delete_middle(input_list):
    """
        Remove all elements from the input list except for the first two and the
        last two.
         [ A, B, C, D, E, F, G, H ] --> [ A, B, G, H ]
    """
    del input_list[2:-2]
    return input_list
    pass
#print new_list
#print delete_middle(new_list)

"""
Part 1 is finished! Ask for a code review before proceeding to Part 2.
"""

"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 and 2 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""
#new_list=[0, 1, 2,3,4,5,6,7]
#new_list2=[0, 1, 2,3,4,5,6,7,8]
def custom_len(input_list):
    """
        like len(input_list), should return the number of items in the list
    """
    i = 0
    for item in input_list:
        i = i + 1
    return i

    pass
#print custom_len(new_list)

# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """
        like input_list.append(value), should add the value to the end of the list
        and return nothing
    """
    input_list[:] = input_list + [value]
    print "custum append ", input_list
    
    pass
#print custom_append(new_list, 9)

def custom_extend(input_list, second_list):
    """
        like input_list.extend(second_list), should append every item in the second 
        list to the end of the first list and return nothing
    """
    input_list[:] = input_list + second_list
    print "custom_extend ", input_list
    #return input_list
    pass
#print custom_extend(new_list, new_list2 )

def custom_insert(input_list, index, value):
    """
        like input_list.insert(index, value), should insert (not replace) the value
        at the specified index of the input list and return nothing
    """
    temp_list = input_list[index:]
    input_list[index:] = input_list
    input_list[:] = input_list + [value] + temp_list
    print "custom insert ", input_list
    #return input_list
    pass
#print custom_insert(new_list, 3, "ball")

#notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
def custom_remove(input_list, value):
    """
        like input_list.remove(value), should remove the first item of the 
        value specified and return nothing
    """
    i = 0
    for item in input_list:
        
        #print i, item, "value ", value
        if (item == value):
            #print "if ", i, item, value, 
            input_list = input_list[:i] + input_list[i+1:]
            #input_list[i] = 
        
        i +=1
    print "custom remove ", input_list    
    #return input_list
    pass
#print notes
#print custom_remove(notes, "Do")

def custom_pop(input_list):
    """
        like input_list.pop(), should remove the last item in the list and 
        return it
    """
    value = input_list[-1]
    input_list = input_list[:-1]
    print "custom pop ", value
    return value
    pass
#print notes
#print custom_pop(notes)

def custom_index(input_list, value):
    """
        like input_list.index(value), should return the index of the first item 
        which matches the specified value
    """
    i = 0
    for item in input_list:
        if (item == value):
            return i
        else:
            i += 1
    pass
#print notes
#print custom_index(notes, "Mi")

def custom_count(input_list, value):
    """
        like input_list.count(value), should return the number of times the specified
        value appears in the list.
    """
    count = 0
    for item in input_list:
        if (item == value):
            count +=1
    return count
    pass
#print notes
#print custom_count(notes, "Do")
#print custom_count(notes, "La")


def custom_reverse(input_list):
    """
        like input_list.reverse(), should reverse the elements of the original list
        and return nothing (we call this reversing "in place")
    """
    temp_list = []
    
    for item in input_list:
        # must concate list to list so taking a one element slice acts
        # like a one item list
        temp_list = temp_list + input_list[-1:]
        input_list= input_list[:-1]
    input_list= temp_list
    print "custom_reverse list ", input_list
    #return input_list
    pass
#print notes
#print custom_reverse(notes)
#print notes


def custom_contains(input_list, value):
    """
        like (value in input_list), should return True if the list contains the
        specified value and False if it does not 
    """
    for item in input_list:
        if(item == value):
            return True
    return False
    pass
#print notes
#print custom_contains(notes, "Fa")
#print custom_contains(notes, "bug")

def custom_equality(some_list, another_list):
    """
        like (some_list == another_list), should return True if both lists contain
        the same values in the same indexes
    """
    index1 = 0
    index2 = 0
    #find length of list
    for item in some_list:
        index1 += 1
        
    for item in another_list:
        index2 += 1
        
    #print "another_list num ", index2
    #print "some_list num ", index1

    # if lists are same size compare lists else return false
    if (index1 == index2):
        # compare list values
        for i in range(index1):
            # increment through each item of the lists. if it matchs
            # compare the next. if it gets to one that doesnt match False
            if (some_list[i] == another_list[i]):
                i+= 1
            else:
                return False
        #after comparing all items
        return True

    else:
        return False
    
    pass
#print notes
#print new_list
#notes2= notes
#notes3 = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Ti']
#print custom_equality(notes, notes2)
#print custom_equality(notes, new_list)
#print custom_equality(notes, notes3)

"""
Part 2 is finished! Required: Ask for a code review. Optional: High-Five
"""
#months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
#notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#custom_append(months, "hex")
#custom_extend(months, ["bin", "tri", "hex" ])
#custom_insert(months, 8, "hex")
#custom_remove(months, "Jul")
#print months
#custom_pop(months)
#custom_reverse(months)

