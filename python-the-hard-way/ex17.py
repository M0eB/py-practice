# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex17 - More Files			
# =============================================================================


from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata   = open( from_file ).read()  
out_file = open( to_file, 'w' ).write( indata )

print "Done."

# No need to close files when calling read/write this way.
# The file should already be closed one the line returns


