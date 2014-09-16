# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex9 - Printing, Printing, Printing
# =============================================================================

# -----------------------------------------------------------------------------
# 	- %r will ignore formatting characters such as \n since it will print 
#        the raw format for debugging
#   -  You can print multiple lines by wrapping the string in triple quotes
# -----------------------------------------------------------------------------


days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months:", months
print "Here are the months: %r" % months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""


