# ex36 lpthw - cicerone map game

from sys import exit
import sys
import random

player = raw_input("First, what is your name:  ")

def start():
	print "Now %s, welcome to the Cicerone training game." % player
	print "You will work your way through town answering a series of beery questions."
	print "Make sure to capitalize your answers."
	print "If you answer correctly, you win."
	print "If you answer incorrectly, you lose."
	print "That's life.\n"

	vicar_office()

def vicar_office():
	print "You are in the office of your local vicar."
	print "He asks, 'Name one of the two types of barley used in brewing.'"

	vicar_answer = raw_input()

	if vicar_answer == "Two Row":
		print "Good job.\n"
		dmv()
	elif vicar_answer == "Six Row":
		print "Nice, you get to move on.\n"
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
			print "Right again!!\n"
			ups_store()
		else:
			print "Not quite.\n"
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
		print "You got it!\n"
	else:
		print "This time, it doesn't matter you are wrong.\n"

	farmers_market()

def post_office():
	print "Welcome to the post office."
	print "Before you can send a package, the clerk has a query."
	print "Name the tax brewers are forced to pay for every gallon brewed."

	excise = raw_input("> ")

	if excise == "Federal Excise Tax":
		print "Great one! Move on to the mall.\n"
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
		print "Yes.\n"
		grocery()
	elif freshness == "Dark":
		print "Alright.\n"
		grocery()
	else:
		die()

def beer_store():
	print "Welcome to the beer store."
	print "Now things are going to get difficult."
	print "I'm going to give you a IBU value..."
	print "You have to select the corresponding beer style."

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

	print "That was tough!"
	nirvana()

def grocery():
	print "Welcome to the grocery store."
	print "The clerk will give you a brewing temperature."
	print "You have to decide if he is brewing an Ale or a Lager."

	for n in range(8):
		query = random.randint(45, 78)
		print "Clerk: %d degrees Fahrenheit..." % query
		temp_ans = raw_input('Ale or Lager?\n')

		if temp_ans == "Lager" and 45 <= query <= 56:
			print "Way to go!\n"
		elif temp_ans == "Ale" and 56 <= query <= 78:
		  	print "Correct!\n"
		else:
			print "You failed!\n"
			purgatory()
	print "You were fantastic."
	nirvana()

def nirvana():
	print "Great Work! You reached nirvana..............."

def purgatory():
	print "Not so smart? Infinite limbo.............\n"

	while True:
		print "Noooooooooo! "

def die():
	print "Too bad..."
	exit(0)

start()
