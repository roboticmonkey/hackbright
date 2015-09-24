def list_even (list):
	if len(list)%2 == 0:
		return True
	else: 
		return False


even_list = [1,2,3,4,5,6]
odd_list = [1,2,3]

print "even_list is even:", list_even(even_list)
print "odd_list is even:", list_even(odd_list)

def list_even_short(list):
	return len(list)%2 ==0


my_info = {"age": 35}
my_info["height"] = 78
my_info["age"] = my_info["age"] +1
print my_info
for key in my_info:
	print key
for key in my_info:
	print my_info[key]
for key, value in my_info.items():
	print key
for key, value in my_info.items():
	print value
for key in my_info.keys():
	print key




