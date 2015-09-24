new_list=[0, 1, 2,3,4,5,6,7,8]

def head(input_list):
    #"""
        #Return the first element of the input list.
        #[ A, B, C, D, E, F ] --> A
    #"""
   # pass
   return input_list[0]

print head(new_list)

def tail(input_list):
    #"""
        #Return the first element of the input list.
        #[ A, B, C, D, E, F ] --> A
    #"""
   # pass
   return input_list[1:]

print tail(new_list)

def last(input_list):
    #"""
        #Return the first element of the input list.
        #[ A, B, C, D, E, F ] --> A
    #"""
   # pass
   return input_list[-1]

print last(new_list)

def init(input_list):
   # """
    #    Return all elements of the input list except the last.
      #  [ A, B, C, D ] --> [ A, B, C ]
    #"""

    return input_list[:-1]

print init(new_list)

def first_three(input_list):
    #"""
     #   Return the first three elements of the input list.
      #  [ A, B, C, D, E, F ] --> [ A, B, C ]
    #"""

    return input_list[:3]

print first_three(new_list)

def last_five(input_list):
    #"""
     #   Return the last five elements of the input list.
      #  [ A, B, C, D, E, F ] --> [ B, C, D, E, F ]
    #"""

    return input_list[-5:]
print last_five(new_list)

def middle(input_list):
    #"""
     #   Return all elements of the input list except the first two and the last two.
      #  [ A, B, C, D, E, F ] --> [ C, D ]
    #"""
    #pass
    return input_list[2:-2]
print middle(new_list)

def inner_four(input_list):
#    """
 #       Return the third, fourth, fifth, and sixth elements of the input list.
  #      [ A, B, C, D, E, F, G ] --> [ C, D, E, F ]
   # """
	return input_list[2:6]
print inner_four(new_list)

def inner_four_end(input_list):
    """
        Return the sixth, fifth, fourth, and third elements from the end of the 
        list, in that order.
        [ A, B, C, D, E, F, G, H, I, J, K, L] --> [ G, H, I, J ]
    """
    return input_list[-6:-2]
print inner_four_end(new_list)

def replace_head(input_list):
    """
        Replace the head of the input list with the value 42.
        [ A, B, C, D ] --> [ 42, B, C, D]
    """
    input_list[0]=42
    return input_list
    
replace_head(new_list)
print new_list

def replace_third_and_last(input_list):
    """
        Replace the third and last elements of the input list with the value 37.
        [ A, B, C, D, E, F ] --> [ A, B, 37, D, E, 37 ]
    """
    input_list[2]=37
    input_list[-1]=37
    return input_list

replace_third_and_last(new_list)
print new_list

new_list=[0, 1, 2,3,4,5,6,7,8]
def replace_middle(input_list):
    """
        Replace all elements of the input list with the the values 42 and 37, in
        that order, except for the first two and last two elements.
        [ A, B, C, D, E, F, G, H, I ] --> [ A, B, 42, 37, H, I ] 
    """
    input_list[2:-2]=[42,37]

replace_middle(new_list)
print new_list

new_list=[0, 1, 2,3,4,5,6,7,8]

def delete_third_and_seventh(input_list):
    """
        Remove the third and seventh elements of the input list.
        [ A, B, C, D, E, F, G, H ] --> [ A, B, D, E, F, H ]
        """
    del input_list[2]
    del input_list[5]
    return input_list


delete_third_and_seventh(new_list)
print new_list