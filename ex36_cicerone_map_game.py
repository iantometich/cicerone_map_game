# ex36 lpthw - cicerone map game - use all elements of python i know

from sys import exit

player = raw_input("First, what is your name: \n")
points = 0

def start():
	print "Now %s, welcome to the Cicerone training game." % player
	print "You will work your way through town answering a series of beery questions."
	print "If you answer correctly, you gain points."
	print "If you answer incorrectly, you lose points."
	print "If you succeed, you will enter Nirvana."
	print "If you fail, it's damnation for you...\n"

	vicar_office()

def vicar_office():
	print "You are in the office of your local vicar."
	print "He asks you to abdicate free thought and join his flock."

	vicar_answer = raw_input("'Yes' or 'No'? ")

	if vicar_answer == 'Yes':
		die()
	elif vicar_answer == 'No':
		# points += 1
		# print points
		print "Nice, you get to move on.\n"
		dmv()
	elif vicar_answer == 'Fuck No':
		# points += 10
		# print "Points: %d" % points
		print "Fuck yeah! Move on...\n"
		dmv()
	else:
		print "Try again..."
		vicar_office()

def dmv():
	print "You made it to the DMV. Sorry."
	print "The lazy ass at the counter asks a question."
	print "'How do brewers express the bitterness level of their beer?'"

	dmv_answer = raw_input("Hint: It is a three letter acronym... ")

	if dmv_answer == 'IBU':
		print "You are correct!"
		print "Now what does it stand for??"

		ibu_acronym = raw_input("> ")

		if ibu_acronym == 'International Bitterness Units':
			print "Right again!!\n"
			ups_store()
		else:
			print "Not quite. You live another day...\n"
			post_office()
	else:
		print "Nope. You dead."
		die()

def ups_store():
	print "You are a pro. Welcome to the UPS Store."
	print "You need to ship a package but the worker has a question for you."
	print "'What beer trait does degrees SRM indicate in beer?'"

	srm = raw_input("> ")

	if srm == 'Color':
		print "You got it!"
	else:
		print "This time, it doesn't matter you are stupid."

	# farmers_market()

def post_office():
	print "You ain't from around here don't ya?"
	print "Welcome to the goddamn post office."

# def farmers_market():

# def mall():

# def beer_store():

# def gocery():

# def nirvana():

# def dump():

def die():
	print "Too bad..."
	exit(0)

start()
