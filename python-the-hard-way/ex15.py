# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex15 - Reading Files
# =============================================================================


from sys import argv

script, filename = argv

print "Here's your file %r: " % filename

#Print contents of file
file = open( filename ) 
print file.read()
file.close()


