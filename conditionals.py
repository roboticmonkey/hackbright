import time
import calendar
import datetime


#answer to 1
if ("aiden" > "joel"):
	print "my name is greater!"
elif ("aiden" < "joel"):
	print "their namer is greater."
else: print "our names are equal."



#now = time.strftime("%c")
now2 = datetime.datetime.now()
#print now2.year
#print now2.month

print "current date " + time.strftime("%x")
#print time.strftime("%d")
#print calendar.monthrange(now2.year, now2.month)
#print "current date " + time.strftime("%A")

month = calendar.monthrange(now2.year, now2.month)
#print "this is the month range " ,month
print "this is the max days" , month[1]

#answer to 2
if (time.strftime("%d") >= month[1]):
	print "oh, we're halfway there!"
else: print "the month is still young"

# answer to 3
if (time.strftime("%A") == "Monday"):
	print "yay class day!"
elif (time.strftime("%A") == "Tuesday"):
	print "sigh, it's only Tuesday"
elif (time.strftime("%A") == "Wednesday"):
	print "humpday!"
elif (time.strftime("%A") == "Thursday"):
	print "#tbt"
elif (time.strftime("%A") == "Friday"):
	print "TGIF"
else: print "yeah, it's the weekend!"



