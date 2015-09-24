names = ["jim", "sarah", "tosca", "bob"]

#print names[2]
#print names[-1]
#print names[0:2]
#print names[2:]


movies = ["big", "hackers", "say anything", ]

#print movies[1]
#print movies[-2]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
			 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
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
    return input_list

print custom_remove(names, "tosca")
i = 1
print movies[i+1]
print custom_remove(months, "Jul")
print months
month = months[:-1]
print month
