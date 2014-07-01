# ex36 lpthw - cicerone map game

from sys import exit
import sys

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

	if vicar_answer == "Yes":
		die()
	elif vicar_answer == "No":
		# points += 1
		# print points
		print "Nice, you get to move on.\n"
		dmv()
	elif vicar_answer == "Hell No":
		print "Hell yeah! Move on...\n"
		dmv()
	else:
		print "Try again..."
		vicar_office()

def dmv():
	print "You made it to the DMV. Sorry."
	print "The lazy ass at the counter asks a question."
	print "'How do brewers express the bitterness level of their beer?'"

	dmv_answer = raw_input("Hint: It is a three letter acronym... ")

	if dmv_answer == "IBU":
		print "You are correct!"
		print "Now what does it stand for??"

		ibu_acronym = raw_input("> ")

		if ibu_acronym == "International Bitterness Units":
			# put this if/else in a function? "shouldn't go 2 deep..."
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

	if srm == "Color":
		print "You got it!"
	else:
		print "This time, it doesn't matter you are stupid."

	farmers_market()

def post_office():
	print "Welcome to the post office."
	print "Before you can send a package, the clerk has a query."
	print "Name the tax brewers are forced to pay for every gallon brewed."

	excise = raw_input("> ")

	if excise == "Federal Excise Tax":
		print "Great one! Move on to the mall."
		mall()
	else:
		print "Try again.\n"
		post_office()

def farmers_market():
	print "Welcome to the farmers market."
	print "Those peaches look great."
	print "But first, the salesman has a question."
	print "Name at least one member of the 3 Tier Distribution System."

	tiers = raw_input("> ")

	if tiers == "Distributor":
		print "You are so smart.\n"
		beer_store()
	elif tiers == "Brewer":
		print "That is correct.\n"
		beer_store()
	elif tiers == "Retailer":
		print "Yeppers.\n"
		beer_store()
	else:
		print "You couldn't get one? Even with the internet?"
		die()

def mall():
	print "You made it to the mall."
	print "For some reason, they are selling cars in there."
	print "The guy at Brookstone won't sell you that massage chair"
	print "until you answer correctly."

	freshness = raw_input("What keeps bottled beer freshest?\n")

	if freshness == "Cold":
		print "Yes."
		grocery()
	elif freshness == "Dark":
		print "Alright."
		grocery()
	else:
		die()

def beer_store():
	print "Welcome to the beer store."
	print "Now things are going to get difficult."
	print "I'm going to give you a IBU value..."
	print "You have to give me a corresponding beer style."

	questions = [
	  {
	  'question': '12 IBU',
	  'answer': 2,
	  'options': ['Munich Dunkel', 'Standard American Lager', 'Oktoberfest']},
	  {
	  'question': '28 IBU',
	  'answer': 1,
	  'options': ['Schwarzbier', 'Cream Ale', 'ESB']},
	  {
	  'question': '45 IBU',
	  'answer': 2,
	  'options': ['Oatmeal Stout', 'Dry Stout', 'Sweet Stout']},
	  {
	  'question': '80 IBU',
	  'answer': 3,
	  'options': ['English IPA', 'Belgian Tripel', 'American Barleywine']},
	  ]

	for ask in questions:
	    print ask['question'] + '?'
	    n = 1
	    for options in ask['options']:
	        print "%d. %s" % (n, options)
	        n = n + 1
	    response = sys.stdin.readline().strip()
	    if int(response) == ask['answer']:
	        print "YES!\n"
	    else:
	        print "NO!\n"

def grocery():
	print "Welcome to the grocery store."

# def nirvana():

# def dump():

def die():
	print "Too bad..."
	exit(0)

start()
