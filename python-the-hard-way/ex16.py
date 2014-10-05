# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex15 - Reading and Writing Files
# =============================================================================


# File methods ----------------------------------------------------------------
#
#           read() - Read the contents of the file and return a string.
#       readline() - Reads one line of the text file.
#  write( "text" ) - Writes text to the file.
#       truncate() - Empties the fule. 
#          close() - Close the file.
#              ...
# -----------------------------------------------------------------------------


from sys import argv


script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN"

raw_input( "?" )

print "Opening the file..."
target = open( filename, 'w' )


# Note that truncate has an optional size argument and 
# the file is trucated to at most that size
# The size defaults to the current position

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going t ask you for three lines."

line1 = raw_input( "line 1 : " )
line2 = raw_input( "line 2 : " )
line3 = raw_input( "line 3 : " )

print "I'm going to write these to the file."

target.write( line1 + "\n" + line2 + "\n" + line3 + "\n" )s

print "And finally, we close it."
target.close()


