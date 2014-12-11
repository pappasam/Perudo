import re
import random
import collections # This one might not be necessary

class Die:
	'''
	Defines the attributes of the type of die in play
	Note:  Only fair dice are allowed in play
	'''
	def __init__(self, sides=6):
		self.sides = sides
		self.value = 1

	def roll(self):
		'''roll one die'''
		self.value = int(random.uniform(1,self.sides + 1))

class Cup:
	'''
	Defines the attributes of a cup of dice
	'''
	def __init__(self, max_dice=5, sides=6):
		'''Initialize the number of dice'''
		self.max_dice = max_dice
		self.sides = sides
		self.dice = [Die(sides=sides) for i in range(max_dice)]

	def roll_dice(self):
		[die.roll() for die in self.dice]

	def dice_values(self):
		return [die.value for die in self.dice]

	def number_dice(self):
		return len(self.dice)

	def add_die(self):
		if self.number_dice() < self.max_dice: # only add if below max
			self.dice.append(Die(sides=self.sides))

	def remove_die(self):
		if self.number_dice() > 0: # only remove die if above zero
			self.dice.pop()
 
class Player:
	'''
	Defines attributes unique to a player in addition to
	the dice in his cup.  These attributes are specific to the player
	only, and have nothing to do with the player's relative position
	with other players (this is handled in another class)
	'''
	def __init__(self, username, start_dice=5, sides=6):
		self.username = username	# username
		self.cup = Cup(max_dice=start_dice, sides=sides)
		self.attained_palifico = False

	def done_palifico(self):
		'''This indicates that the player has finished leading a 
		palifico round'''
		self.attained_palifico = True

class Roster:
	'''Creates an object of player objects'''
	def __init__(self, start_dice=5, sides=6):
		self.start_dice = start_dice
		self.sides = sides
		self.roster = []

	def _input_name(self):
		'''request user input for name and check for errors'''
		REQUIREMENT = "username must be of length > 1 and contain only alphanumeric characters"
		input_string = "Enter username (%s): " % REQUIREMENT
		pattern_alphanumeric = re.compile('\w+', re.IGNORECASE)
		while True:
			name = input(input_string)
			if re.match(pattern_alphanumeric, name):
				return name
			else:
				print(REQUIREMENT + ". Maybe omit spaces?  Please try again...")

	def set_roster(self, number_players):
		'''Initialize roster of players'''
		if self.roster == []:
			for i in range(number_players):
				name = self._input_name()
				self.roster.append(Player(username=name,
											start_dice=self.start_dice,
											sides=self.sides))
		else:
			print("Roster already set")

	def player_names(self):
		'''return list of player names'''
		return [player.username for player in self.roster]

	def eliminate_zero_dice(self):
		'''Eliminate players with zero dice'''
		self.roster = [player for player in self.roster if player.cup.number_dice() > 0]
			
if __name__ == '__main__':
	print("---Testing class: Players")
	p = Roster(start_dice=1)
	p.set_roster(3)
	print(p.roster[2].username)

	p.roster[2].cup.remove_die()

	print(p.player_names())
	p.eliminate_zero_dice()
	print(p.player_names())

	# for player in p.roster:
	# 	print(player.username)
	# 	print(player.cup.dice_values())
	# 	player.cup.roll_dice()
	# 	print(player.cup.dice_values())
	# 	player[2]





	# print("---Testing class: Die")
	# d = Die()
	# for i in range(20):
	# 	d.roll()
	# 	print(d.value)

	# print("---Testing class: Cup")
	# c = Cup()
	# print(c.dice_values())
	# c.roll_dice()
	# print(c.dice_values())
	# c.remove_die()
	# print(c.dice_values())
	# c.remove_die()
	# print(c.dice_values())
	# c.roll_dice()
	# print(c.dice_values())
	# c.add_die()
	# print(c.dice_values())

	# print ("---Testing class: Player")
	# p = Player()
	# p.cup.roll_dice()
	# print(p.cup.dice_values())
	# print(p.attained_palifico)
	# p.done_palifico()
	# print(p.attained_palifico)



# class Player:
# 	'''
# 	Defines a player and tracks their roll and dice count
# 	'''
	
# 	def __init__(self, player_name, start_dice=5, sides_per_die=6):
# 		self.name = player_name
# 		self.number_dice = start_dice
# 		self.sides_per_die = sides_per_die
# 		self.current_roll = [] # initialize current role to zero

# 	def roll_dice(self):
# 		'''roll player's dice'''
# 		self.current_roll = [int(random.uniform(1,self.sides_per_die + 1)) \
# 								for i in range(self.number_dice)]

# 	def current_roll(self):
# 		return self.current_roll

# 	def remove_die(self):
# 		self.number_dice -= 1

# 	def add_die(self):
# 		self.number_dice += 1
		
# 	def number_dice(self):
# 		return int(self.dice_per_cup)

# class Round:
# 	'''Defines a round'''

# 	def __init__(self, active_players, starter):
# 		self.active_players = active_players
# 		try:
# 			self.caller = active_players.next_key(starter)
# 		except:
# 			self.caller = active_players.first_key()

# 	def _get_responder(self):
# 		'''get name of the responder'''
# 		try:
# 			return self.active_players.next_key(self.caller)
# 		else:
# 			return self.active_players.first_key()
	
# 	def _players_roll(self):
# 		'''Make all active players roll dice'''
# 		for player in active_players:
# 			player.roll_dice()

# 	def _possible_calls(self, previous_call, num_dice, first_round=False, palifico=False):
# 		'''Get user input and evaluate its validity
# 		Rules (assuming the call represents valid integers):
# 			1) If first_round is True
# 				- If palifico is True, begin with anything
# 				- Else can't begin with 1
# 			2) Else If palifico = True
# 				- If num_dice > 1, must call either more dice of same number or dudo
# 				- Else If num_dice == 1, can change the number of the die 
# 			3) Else If previous die value == 1
# 				- Increase number of ones
# 				- Increase number of dice to at least 2*num_ones + 1
# 			4) Else
# 				- Increase the value of the die without decreasing the number of dice 
# 				- Increase the number of dice
# 				- Take half the number called, rounded up, and call ones'''		
# 		p_dicenum, p_diceval = previous_call
		
# 		if first_round == True:
# 			if palifico == True:
# 				return ()


# 		while True:
# 			try:
# 				current_call = int(input("Number of Dice"))
# 			if first_round == True:

# 	def _make_call(self, call_past):
# 		'''determine calls
# 		BEGIN LOGIC WORK HERE: THIS IS QUITE THE CHALLENGE'''
# 		past_num = call_past[0]
# 		past_val = call_past[1]
# 		while True:
# 			try:
# 				x = int(input('Number of Dice --> '))
# 				y = int(input('Value of Dice  --> '))

# 				if call_past == (0,0) and y == 1:
# 					print(
# 				if x <= 0 or y <= 0:
# 					print('Only positive, non-zero values')
# 				elif x >
# 			except:
# 				print("Ensure you only enter integer values")
			
# 	def play_round(self):
# 		'''Main logic for round'''
# 		self._players_roll()
# 		call_past = ''
# 		flag_dudo = False
# 		while flag_dudo == False:
# 			call_present = _make_call
# 		call_present = 
# 		flag_dudo = False
# 		call_past = (0,0)
# 		call_present = (0,0)
# 		while flag_dudo == False:
# 			call_past, call_present = call_present, (0,0)
