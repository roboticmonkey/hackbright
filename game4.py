import math

zero_string = "44-44"
print "%s = %i" % (zero_string, eval(zero_string))

one_string = "44/44"
print "%s = %i" % (one_string, eval(one_string))
 
two_string = " 4/4 + 4/4"
print "%s = %i" % (two_string, eval(two_string))

three_string = ""

four_string = ""

five_string = "(44 - 4!)/4"
print "%s = %i" % (five_string, (44- math.factorial(4))/4 )

six_string = ""

seven_string = "(4+4) - 4/4"
print "%s = %i" % (seven_string, eval(seven_string))

eight_string = "(4*4) - (4+4)"
print "%s = %i" % (eight_string, eval(eight_string))

nine_string = "(4+4) + 4/4"
print "%s = %i" % (nine_string, eval(nine_string))

ten_string = "(44-4)/4"
print "%s = %i" % (ten_string, eval(ten_string))

print math.factorial(4) - 4 
print 4**2
