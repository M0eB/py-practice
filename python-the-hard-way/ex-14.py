# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex14 - Prompting and Passing
# =============================================================================


from sys import argv

script, user_name = argv   # User must pass name as argument
prompt = '>'               # Character the user sees during input

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s ?" % user_name
likes = raw_input( prompt )

print "Where do you live %s?" % user_name
lives = raw_input( prompt )

print "What kind of computer do you have ?"
computer = raw_input( prompt )

print """
Alright, so you said %r about liking me.
You live in %r. and you have a %r computer.
""" % ( likes, lives, computer )

