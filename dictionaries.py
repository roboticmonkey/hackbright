# my_stats = {"name": "Katie", "age": 32, "height": "5'3"}
# print "%s is %i years old with the height of %s" % (my_stats["name"], my_stats["age"], my_stats["height"])

# vocabulary_words = {"list": "an ordered group of values", "tuple": "unchangable like list dude",
#  "dictionary": "list of keys and values", "function": "reusable chunk of code"}


# full_name = "moon booger"
# def count_letters(name):
# 	number_letters = {}
# 	for letters in name:
# 		if (letters in number_letters):
# 			number_letters[letters] = number_letters[letters] +1
# 		else:
# 			number_letters[letters] = 1
# 	del number_letters[" "]
# 	return number_letters
# print count_letters(full_name)

def count_letters(txt_list):
 	number_letters = {}
 	for line in txt_list:
 		#print line
 		for letter in line:
 			#print letter
 			if (letter in number_letters):
				number_letters[letter] = number_letters[letter] +1
			else:
				number_letters[letter] = 1
	#del number_letters[" "]
	return number_letters

txt_file = open("one_fish.txt")
txt_list = txt_file.readlines()
txt_file.close()
#print count_letters(txt_list)
# print type(txt_list)
# print count_letters(txt_list)

#
# for item in txt_list:
# 	print item
# 	item.strip("\n")
# 	print item
#print "\n", txt_list

def count_words(txt_list):
 	number_words = {}
 	for line in txt_list:
 		print line
 		line_list = line.split(" ")
 		print line_list
 		for word in line_list:
 			print word
 			word = word.lower()
 			word =word.strip("\n")
 			word = word.strip(".")
 			word = word.strip("!")
 			word = word.strip(",")
 			word = word.strip("?")
 			print word
 			if (word not in number_words):
				number_words[word] = 1
			else:
				number_words[word] += 1
	#del number_letters[" "]
	return number_words

#print count_words(txt_list)


item_prices = {"apples": 50, "ranier cherries": 6, "ramen noodles": 1, "pizza": 100}

def compare_prices(price_list):
	highest_price = {}
	temp_key = " "
	#returns False if empty
	#print bool(highest_price)

	for key, value in price_list.items():
		print key, value
		if (not bool(highest_price)):
			#print highest_price
			highest_price[key] = value
			#print highest_price
			temp_key = key
			#print key
		else:
			if (price_list[key] > highest_price[temp_key]):
				#print key, value
				#print highest_price
				highest_price[key] = value
				#print highest_price
				del highest_price[temp_key]
				temp_key = key
				#print highest_price
				#print temp_key


	return highest_price

		
print compare_prices(item_prices)
