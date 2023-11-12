from calculations.average_result import calculate_average_result

def calculate_success_rate(modifier, proficiency, additional_bonus, ac, advantage=0):
	"""Calculate and return the hit chance based on various parameters."""
	modifier = 0 if modifier == "" else int(modifier)
	proficiency = 0 if proficiency == "" else int(proficiency)
	bonus = 0 if additional_bonus == "" else calculate_average_result(additional_bonus)
	positive_mods = modifier + proficiency + bonus
	# Nat 1s and Nat 20s need to be accounted for
	minimum_roll = max(1, min(19, ac - positive_mods - 1))
	# Calculate hit chance based on DnD 5E rules
	percentage = (1 - (minimum_roll / 20)**(advantage + 1)) * 100
	return percentage

# def probability_one_die_meets(dice, target):
# 	num_dice, value_dice = map(int, dice.split('d'))
# 	percentage = ((value_dice - target + 1) / value_dice)**(num_dice) * 100
# 	return percentage

def probability_repeated_success(dice, target):
	num_dice, value_dice = map(int, dice.split('d'))
	percentages = []
	for i in range(1, num_dice + 1):
		percentage = ((value_dice - target + 1) / value_dice)**(i) * 100
		percentages.append(percentage)

	return percentages