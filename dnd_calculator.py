#!/usr/bin/env python3

# Function Definitions

def hit_chance(modifier, proficiency, additional_bonus, ac, advantage=0):
	"""Calculate and return the hit chance based on various parameters."""
	bonus = 0 if additional_bonus == "" else average_result(additional_bonus)
	positive_mods = modifier + proficiency + bonus
	# Nat 1s and Nat 20s need to be accounted for
	minimum_roll = max(1, min(19, ac - positive_mods - 1))
	# Calculate hit chance based on DnD 5E rules
	percentage = (1 - (minimum_roll / 20)**(advantage + 1)) * 100
	return percentage

def calculate_and_display_hit_chance(modifier, proficiency, additional_bonus, ac):
	"""Calculate the hit chance and return the message to display to the user."""
	normal_percentage = hit_chance(modifier, proficiency, additional_bonus, ac)
	advantage_percentage = hit_chance(modifier, proficiency, additional_bonus, ac, 1)
	bonus_text = f", bonus of {additional_bonus}" if additional_bonus != "" else ""
	response = (f"The hit chance, given a modifier of {modifier}, proficiency of {proficiency}"
				f"{bonus_text}, and an AC of {ac} is: "
				f"\r\nNormal roll = {normal_percentage}% \tAdvantage roll = {advantage_percentage}%")
	return response

def average_result(collection):
	"""Calculate and return the average damage from a set of values."""
	instances = collection.split('+')
	average = 0

	for instance in instances:
		instance = instance.strip()

		if 'd' in instance:
			try:
				num_dice, dice_value = map(int, instance.split('d'))
				average_value = (dice_value + 1)/2 * num_dice
			except ValueError:
				print(f"Invalid expression: {instance}")
				return None
		else:
			try:
				average_value = int(instance)
			except ValueError:
				print(f"Invalid expression: {instance}")
				return None

		average += average_value
	return average

def damage_per_round():
	# Placeholder for damage per round calculation
	return "Damage per round function not implemented yet."

#def saving_throws():

def skill_check(modifier, proficiency, additional_bonus, dc):
	"""Calculate the chance of succeeding in a skill check and return the message to display to the user."""
	normal_percentage = hit_chance(modifier, 0, additional_bonus, dc)
	advantage_percentage = hit_chance(modifier, 0, additional_bonus, dc, 1)
	bonus_text = f", bonus of {additional_bonus}" if additional_bonus != "" else ""
	response = (f"The chance to pass the skill check, given a flat modifier of {modifier}"
				f"{bonus_text}, and an DC of {dc} is: "
				f"\r\nNormal roll = {normal_percentage}% \tAdvantage roll = {advantage_percentage}%")
	return response

def main():
	while True:
		print("\r\n")
		print("Choose a calculation:")
		print("1: Hit Chance")
		print("2: Average Damage")
		print("3: Damage Per Round [Not implemented]")
		print("4: Skill Check")
		print("0: Exit")

		choice = input("Enter your choice: ")
		print("\r\n")
		# Get the user to input all of the necessary data depending on the requested calculus
		if choice == '1':
			try:
				# Validate that the inputs
				modifier = int(input("Enter the modifier for the attack: "))
				proficiency = int(input("Enter the proficiency bonus: "))
				additional_bonus = str(input("Enter any additional bonus (like +1 to rolls on a weapon or the Bardic Inspiration dice) or press Enter for none: "))
				#additional_bonus = 0 if additional_bonus_str == "" else int(additional_bonus_str)
				ac = int(input("Enter the Armor Class (AC): "))
				if ac <= 0:
					print("Armor Class cannot be negative or 0")
					continue
			except ValueError:
				print("Please enter valid integer values for the attribute.")
				continue

			response = calculate_and_display_hit_chance(modifier, proficiency, additional_bonus, ac)
			print("----------------------")
			print(response)
			print("----------------------")

		elif choice == '2':
			damage_collection = input("Enter all the instances of damage to account for: ")
			print("----------------------")
			print("The average damage is: " + str(average_result(damage_collection)))
			print("----------------------")

		elif choice == '3':
			print(damage_per_round())

		elif choice == '4':
			try:
				# Validate that the inputs
				modifier = int(input("Enter the flat modifier of the skill including proficiency or expertise: "))
				additional_bonus = str(input("Enter any additional bonus (either flat modifiers or dice) or press Enter for none: "))
				dc = int(input("Enter the Difficulty Class (DC): "))
				if dc <= 0:
					print("DC cannot be negative or 0")
					continue
			except ValueError:
				print("Please enter valid integer values for the attribute.")
				continue

			response = skill_check(modifier, 0, additional_bonus, dc)
			print("----------------------")
			print(response)
			print("----------------------")
		
		elif choice == '0':
			print("Exiting. Have a nice day!")
			break

		else:
			print("Invalid choice. Enter 1, 2, 3 or 0.")
			continue

if __name__ == "__main__":
	main()
