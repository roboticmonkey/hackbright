def bart_kiosk(number_of_ones, number_of_fives, number_of_tens, number_of_twentys):
	total = number_of_ones*1 + number_of_fives*5 +number_of_tens*10 +number_of_twentys*20	

	return total

print bart_kiosk(0,0,0,0)
print bart_kiosk(0,0,0,9)
print bart_kiosk(2,3,0,0)
print bart_kiosk(3,1,1,3)

fremont_richmond =["Fremont", "Union City", "South Hayward", "Hayward", "Bay Fair", 
	"San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "12 st", "19th st", "MacArthur", 
	"Asby", "Downtown Berkeley", "North Berkeley", "El Cerrito Plaza", "El Cerrito del Norte"]

#origin_station takes an integer of the index of the departing station in list_of_stations
#destination_station takes and integer of the index of the arrival station in list_of_stations

def calulate_fare (list_of_stations, origin_station, destination_station ):
	each_stop = 1.25
	num_stops = destination_station - origin_station
	#if num_stops becomes a negative number
	if(num_stops < 0):
		num_stops = num_stops * -1

	fare_price = each_stop * num_stops

	print "Your departing station is ", list_of_stations[origin_station]
	print "Your arrival station is ", list_of_stations[destination_station]
	print "The total cost of travel will be $%.2f"  % (fare_price)

	return fare_price

#running some tests
test_amt_1 = calulate_fare(fremont_richmond, 0,4)
#print "returned value", test_amt_1

test_amt_2 = calulate_fare(fremont_richmond, 7, 2)
#print "returned value", test_amt_2

#open file
bart_file = open("dublin_pleasanton.txt")
#save file as a list
dublin_pleasanton = bart_file.readlines()
#close file
bart_file.close()

test_amt_3 = calulate_fare(dublin_pleasanton, 0, 4)
test_amt_4 = calulate_fare(dublin_pleasanton, 7, 2)
