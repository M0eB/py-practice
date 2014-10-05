# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex10 - Escape Sequences
# =============================================================================

# ESCAPE SEQUENCES ------------------------------------------------------------
#
#       \\	     Backslash ()
#       \'	     Single-quote (')
#       \"	     Double-quote (")
#       \a	     ASCII bell (BEL)
#       \b	     ASCII backspace (BS)
#       \f	     ASCII formfeed (FF)
#       \n	     ASCII    linefeed (LF)
#    \N{name}	 Character named name in the Unicode database (Unicode only)
#       \r       ASCII	Carriage Return (CR)
#       \t       ASCII	Horizontal Tab (TAB)
#     \uxxxx	 Character with 16-bit hex value xxxx (Unicode only)
#    \Uxxxxxxxx	 Character with 32-bit hex value xxxxxxxx (Unicode only)
#       \v	     ASCII vertical tab (VT)
#      \ooo	     Character with octal value ooo
#      \xhh	     Character with hex value hh
#
# -----------------------------------------------------------------------------


print "- Backslash : \\"
print "- Single Quote : \'"
print "- Double Quote : \""
print "- ASCII bell \a"
print "- ASCII backspace : \b"
print "- ASCII formfeed : \f"
print "- ASCII line\nfeed."
print "- ASCII Carriage Reterun : \r."
print "- ASCII Horizontal \t Tab."
print "- Character with 16-bit hex value \u1234"
print "- Character with 32-bit hex value \U12345678"  
print "- ASCII vertical tab \v"
print "- Character with octal value \041."   # 41 Octal = !
print "- Character with hex value \x21"      # 21 Hex   = !


