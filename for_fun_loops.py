for i in range(1,21):
	if(i == 13):
		print "hello"
	else: print i

for i in range (0,101,10):
	print i

for i in range (11):
	if (i%2 !=0):
		print i

for i in range (10, -1, -1):
	if i ==0:
		print "Blastoff"
	else:
		print i		

list = ["apples", "oranges", "bananas"]
for item in list:
	print item

for i in range(len(list)):
	print list[i]


def sum_num(num):
	num_tot = 0
	for i in range(num+1):
		#print "i=" , i

		num_tot = num_tot + i
		#print "num_tot=", num_tot
	return num_tot

print sum_num(3)
print sum_num(4) 

def sum_num2(num):
	num_tot = 0
	if (num <0):
		for i in range(num,0,1):
			print "i=" , i

			num_tot = num_tot + i
			print "num_tot=", num_tot
	else:
		for i in range(num+1):
		#print "i=" , i

			num_tot = num_tot + i
		#print "num_tot=", num_tot
	return num_tot
	
print sum_num2(-3)

def fizz_buzz():
	for i in range(1,101,1):
		if (i%3 == 0 and i%5 ==0):
			print "FizzBuzz"
		elif (i%3 == 0):
			print "Fizz"
		elif (i%5 == 0):
			print "Buzz"
		else:
			print i

fizz_buzz()

		