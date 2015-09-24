def bart_kiosk(number_of_ones, number_of_fives, number_of_tens, number_of_twentys):
	total = number_of_ones*1 + number_of_fives*5 +number_of_tens*10 +number_of_twentys*20	

	return total

print bart_kiosk(0,0,0,0)
print bart_kiosk(0,0,0,9)
print bart_kiosk(2,3,0,0)
print bart_kiosk(3,1,1,3)