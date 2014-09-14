# =============================================================================
#          By : Mohamed T. Ismail
#        Book : Learn Python The Hard Way 
#      Author : Zed Shaw
#  Decription : Ex4 - Variables and Names
# =============================================================================


# -----------------------------------------------------------------------------
# 	- You can print numerics wihtout converting to strings
#   - Append be separating with commas (instead of +)
#   - A space is put beterrn the inputs automatically 
# -----------------------------------------------------------------------------


cars = 100
space_in_a_car = 4.0  #float
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


