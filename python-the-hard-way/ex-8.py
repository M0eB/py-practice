# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex8 - Printing, Printing
# =============================================================================

# -----------------------------------------------------------------------------
# 	- Use %s for printing and only use %r for getting debugging information
#	- %r gives you the "raw programmer's" version of variable,
#        also known as the "representation"
#	- %r will sometimes use '' and sometimes use "" because python will
#	     print  the strings in the most efficient way it can, not replicate
#		 exactly the way you wrote them (ok since it is for debugging)
# -----------------------------------------------------------------------------


formatter = "%r %r %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)


