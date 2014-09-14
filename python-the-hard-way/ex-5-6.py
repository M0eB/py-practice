# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex5-6 - More Variables and Printing
# =============================================================================


# String Formatting -----------------------------------------------------------
#
# 	- You can format strings similary to C
#   - Separate the strings from the input vars with %
#   - Group multiple input vars in brackets - % (var1, var2, var3)
#
#	- Conversion types : 
# 		%d / %i = Signed Integer decimal
#		     %u = Unsigned decimal
#		%s / %r = String (convert python object using str() / repr())	
#	              Use %r to print the 'raw' data fi the variable 	
#		     %c = Single character (accepts integer or single char string)
#		%x / %X = Unsigned hex (lowercase/uppercase)
#		     %o = Unsigned octal
#		%f / %F = Floating point decimal
#		%e / %E = Floating point exponential format (lowercase/uppercase)
#		%g / 5G = Floating point format. Uses exponential format if exponent
#				  is greated than -4 or less than precision
#				  Uses decimal format otherwise
#
# -----------------------------------------------------------------------------


## Strings, Chars, Booleans ---------------------------------------------------

my_char = 'M'
my_bool = 2 < 1
my_string = "Hello, World!"
str_hello = "Hello"
str_world = "World"
my_new_string = str_hello + ', ' + str_world + '!'   # concatenate

print "Printing a character : %c" % my_char
print "Printing a boolean : %r" % my_bool
print "Printing a string : %s" % my_string
print "Printing a string : %s" % my_new_string
print "printing multiple items : %s, %s !" % (str_hello, str_world)


## Floating Point Values ------------------------------------------------------

my_num = 1234
my_float = 123.456

print "Printing an int : %d" % my_num         # 1234
print "Printing a float: %f " % my_float      # 123.456
print "Printing a float: %3.0f " % my_float   # 123
print "Printing a float: %.2f " % my_float    # 123.46  <- rounds


## Hex Values  ----------------------------------------------------------------

my_hex_val = 0x0000FFFF

print "Printing a hex as decimal : %d" % my_hex_val                    # 65535
print "Printing a hex as hex (lower) : %x" % my_hex_val                # ffff
print "Printing a hex as hex (upper) : %X" % my_hex_val                # FFFF
print "Using the formatting func. to print 255 :", format(255, '02x')  # ff
print "Using the hex func. to print 255 :", hex(255)                   # 0xff


## Exponential values ---------------------------------------------------------

my_pos_exp = 1.1234e+05
my_neg_exp = 1.1234e-5
my_sml_exp = 1.1234e2

print "Printing a single char : %c" % my_char
print "Printing +ve exponential (lower) : %e" % my_pos_exp   # 1.123400e+05
print "Printing -ve exponential (upper) : %E" % my_neg_exp   # 1.123400E-05
print "Printing +ve exponential (lower) : %g" % my_sml_exp   # 112.34
print "Printing +ve exponential (lower) : %G" % my_neg_exp   # 1.1234E-05


