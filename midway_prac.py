#1
print "this is a string"
#2
print 46
#2a
float(46)
#2b
str(46)
#3
print 4.5
#3a
int(4.5)
#3b
str(4.5)
#4
print True
#4a
int(True)
#4b
str(True)
#5
my_name = "aiden"
type(my_name)
#6
my_height = 65
type(my_height)
#7
print "%s is %i inches tall" % (my_name, my_height)
print my_name, "is", my_height, "inches tall"

#functions
#1
def convert_to_seconds(hours, minutes, seconds):
	minutes = minutes + hours * 60
	seconds = seconds + minutes * 60 
	return seconds
print convert_to_seconds(2, 5, 30)
#2 
def convert_to_hours(seconds):
	#print seconds
	second = seconds%60
	#print second
	minutes = int(seconds/60)
	#print minutes
	minute = minutes%60
	#print minute
	hours = int(minutes/60)
	return (hours, minute, second)
#2a
def print_time(time):
	print "Hours:", time[0], ", Minutes:", time[1], ", Seconds:", time[2]
	print "Hours:%i, Minutes:%i, Seconds:%i" % (time[0], time[1], time[2])

print convert_to_hours(7530)
this_time = convert_to_hours(7530)
print this_time
print_time(convert_to_hours(7530))

#3
def convert_to_inches(feet, inches):
	inches = inches + (feet * 12)
	return inches

print convert_to_inches(5,5)

#4
def convert_to_feet(inches):
	feet = int(inches/12)
	inch = inches%12
	return (feet, inch)

#4a
def print_feet(height):
	print "Feet: %i, Inches: %i" % (height[0], height[1])

print_feet(convert_to_feet(65))

#5 
def count_up(num):
	if (num == 10):
		print num
	else:
		print num
		count_up(num+2)
count_up(0)

#6
def crazy_count_for():
	for index in range(0,101,1):
		if (index >=10 and index%10 == 0):
			print index
		else:
			if (index< 10):
				print index
	
crazy_count_for()

#6a
def crazy_count_while():
	i = 0
	while (i <101):
		if (i >=10 and i%10 ==0):

			print i
			i = i + 10
		elif (i <10):
			print i
			i = i + 1
		else:
			i = i + 1

print "while loop"
crazy_count_while()

#6b 
def crazy_count_recursive(num):
	if (num == 100):
		print num
	elif (num < 101 and num >=10 and num%10 == 0):
		print num
		crazy_count_recursive(num + 10)
	else:
		if (num < 10):
			print num
		crazy_count_recursive(num + 1)

print "crazy_count_recursive"
crazy_count_recursive(0)

#7
def counts_uniq_letters(firstname, lastname):
	fullname = firstname + lastname
	unique_letters = []
	#print firstname, lastname
	for letter in fullname:
		if (not letter in unique_letters):
			#print letter
			unique_letters.append(letter)
		#else:
			#print letter
	#print unique_letters
	
	return len(unique_letters)

	

print counts_uniq_letters("aiden", "ward"), "letters are unique in my name"

# conditionals
#1
test_var = 49
if (test_var >50):
	print "too hight!"
else:
	print "too low"

#1a
test_var = 50
if (test_var >50):
	print "too hight!"
elif (test_var == 50):
	print "just right!"
else:
	print "too low"
#2

print type(test_var)
if (type(test_var) != str):
	test_var = str(test_var)
print type(test_var)

#list $ tuples

#1
colors = ("red", "yellow", "blue")
#1a
print colors[-1]
print colors[len(colors)-1]
#1b
secondary_colors = ("orange", "green", "purple")
print colors, secondary_colors
#1c
all_colors = colors + secondary_colors
print all_colors

#2
full_name = ("aiden", "ward")
print type(full_name)
print full_name
#2a
first_name = full_name[0]
last_name = full_name[1]
full_name = [first_name, last_name]
print type(full_name)
print full_name

#2b
temp_list = [full_name[1], full_name[0]]
full_name = temp_list
print full_name

#loops
#1
print "counts up to 99"
for index in xrange(0,100,1):
	print index

#2
print "counts up to 1000 by 100"
for index in xrange(0, 1000, 100):
	print index

#3
print "count down from 1000 by 100"
for index in xrange(1000, 0, -100):
	print index

#string parsing
#1
my_name = "aiden ward"
print type(my_name)
print my_name
my_name = list(my_name)
print type(my_name)
print my_name



#2
this_string ="1,2,3,4,5"
print this_string
print "var this_string is a", type(this_string)
this_string = this_string.split(",")
print this_string
print "var this_string is now a",type(this_string)

for index in range(len(this_string)):
	#print type(this_string[index])
	#print this_string[index]
	this_string[index] = int(this_string[index])
	#print type(this_string[index])
print type(this_string[4])
print this_string

#3
dr_suess = "one fish two fish red fish blue fish"
dr_suess = dr_suess.split(" fish ")
print dr_suess
dr_suess[len(dr_suess)-1] = dr_suess[len(dr_suess)-1].strip(" fish")
print dr_suess

#word problems
#1

def cal_groc_bill (bill):
	bill = bill.split(",")
	print bill
	#quantity = bill[1].split(":")
	#print quantity
	#quantity = float(quantity[1])
	quantity = float(bill[1].split(":")[1])
	print quantity
	#price = bill[2].split(":")
	#print price
	#price = float(price[1])
	#print price
	price = float(bill[2].split(":")[1])
	print price

	return price * quantity




str = "item:apples,quanity:4,price:1.50\n"

print cal_groc_bill(str)

#1a
items = ["item:apples,quantity:4,price:1.50\n", "items:pears,quantity:5,price:2.00\n",
	"items:cereal,quantity:1,price:4.49"]

def cal_groc_bill_list (bill):
	#print "start of list comp"
	total = 0
	price = 0
	quantity = 0

	for i in range(len(bill)):
		#print bill[i]
		item = bill[i]
		item = item.split(",")
		quantity = float(item[1].split(":")[1])
		#print quantity
		price = float(item[2].split(":")[1])
		#print price
		total = total + (price * quantity)
		#print total

	#print bill[0]
	#print bill
	return total

print "total bill cost", cal_groc_bill_list(items)


#2 create guess_number.py











#













