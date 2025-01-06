#!/usr/bin/env python3

from calculations.utils import *
from calculations.average_result import *

def main():
    while True:
        print("\r\n")
        print("Choose a calculation:")
        print("1: Hit Chance")
        print("2: Average Damage")
        print("3: Damage Per Round")
        print("4: Skill Check")
        print("5: Saving Throw")
        print("6: Probability of multiple dice rolling equal or above")
        print("7: Probability at least one success in multiple rolls")
        print("0: Exit")

        choice = input("Enter your choice: ")
        print("\r\n")
        # Get the user to input all of the necessary data depending on the requested calculus
        if choice == '1':
            try:
                # Validate the inputs
                modifier = str(input("Enter the modifier for the attack: "))
                proficiency = str(input("Enter the proficiency bonus: "))
                additional_bonus = str(input("Enter any additional bonus (like +1 to rolls on a weapon or the Bardic Inspiration dice) or press Enter for none: "))
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
            print("The average damage is: " + str(calculate_average_result(damage_collection)))
            print("----------------------")

        elif choice == '3':
            try:
                # Get all necessary inputs
                modifier = input("Enter the attack modifier: ")
                proficiency = input("Enter the proficiency bonus: ")
                additional_bonus = input("Enter any additional bonus to hit: ")
                ac = int(input("Enter the target's Armor Class (AC): "))
                damage_formula = input("Enter the damage formula (e.g., 2d6+4): ")
                attacks_per_turn = int(input("Enter the number of attacks per turn: "))
                advantage = input("Does the attack have advantage? (yes/no): ").strip().lower()
                advantage = 1 if advantage in ["yes", "y"] else 0

                # Inputs for bonus attacks
                bonus_attacks = int(input("Enter the number of bonus attacks (e.g., off-hand attacks or extraordinary actions): "))
                bonus_attacks_data = []

                for i in range(bonus_attacks):
                    print(f"Enter details for bonus attack {i + 1}:")
                    bonus_damage_formula = input(f"  Damage formula for bonus attack {i + 1} (e.g., 1d6+1): ")
                    bonus_hit_modifier = input(f"  Hit modifier for bonus attack {i + 1} (if different, or press Enter for none): ")
                    bonus_advantage = input(f"  Does bonus attack {i + 1} have advantage? (yes/no): ").strip().lower()
                    bonus_advantage = 1 if bonus_advantage in ["yes", "y"] else 0
                    bonus_attacks_data.append({
                        "damage_formula": bonus_damage_formula,
                        "hit_modifier": bonus_hit_modifier.strip() or "0",
                        "advantage": bonus_advantage
                    })
            except ValueError:
                print("Invalid input. Please ensure all numeric values are correct.")
                continue

            # Call the utility function and print the result
            response = calculate_and_display_damage_per_round(
                modifier, proficiency, additional_bonus, ac, damage_formula, attacks_per_turn, advantage, bonus_attacks_data
            )
            print("----------------------")
            print(response)
            print("----------------------")

        elif choice == '4':
            try:
                # Validate the inputs
                modifier = str(input("Enter the flat modifier of the skill including proficiency or expertise or press Enter for none: "))
                additional_bonus = str(input("Enter any additional bonus (either flat modifiers or dice) or press Enter for none: "))
                dc = int(input("Enter the Difficulty Class (DC): "))
                if dc <= 0:
                    print("DC cannot be negative or 0")
                    continue
            except ValueError:
                print("Please enter valid integer values for the attribute.")
                continue

            response = calculate_and_display_skill_check(modifier, additional_bonus, dc)
            print("----------------------")
            print(response)
            print("----------------------")

        elif choice == '5':
            try:
                # Validate the inputs
                modifier = str(input("Enter the flat modifier to add to the Saving Throw or press Enter for none: "))
                additional_bonus = str(input("Enter any additional bonus (either flat modifiers or dice) or press Enter for none: "))
                dc = int(input("Enter the Difficulty Class (DC): "))
                if dc <= 0:
                    print("DC cannot be negative or 0")
                    continue
            except ValueError:
                print("Please enter valid integer values for the attribute.")
                continue

            response = calculate_and_display_saving_throw(modifier, additional_bonus, dc)
            print("----------------------")
            print(response)
            print("----------------------")

        elif choice == '6':
            try:
                # Validate the inputs
                value_dice_input = input("Enter the size of the dice to roll (Default is a d20): ")
                # Check if the input is empty or an integer
                if value_dice_input.strip() == "":
                    value_dice = 20
                else:
                    value_dice = int(value_dice_input)
                
                num_dice = int(input("Enter the amount of dice to roll: "))
                target = int(input("Enter the target number to meet: "))
            except ValueError:
                print("Please enter valid values.")
                continue
            
            dice = str(num_dice) + 'd' + str(value_dice)
            response = calculate_and_display_probability_repeated_success(dice, target)
            print("----------------------")
            print(response)
            print("----------------------")

        elif choice == '7':
            try:
                # Validate the inputs
                value_dice_input = input("Enter the size of the dice to roll (Default is a d20): ")
                # Check if the input is empty or an integer
                if value_dice_input.strip() == "":
                    value_dice = 20
                else:
                    value_dice = int(value_dice_input)
                
                num_dice = int(input("Enter the amount of dice to roll: "))
                target = int(input("Enter the target number to meet: "))
            except ValueError:
                print("Please enter valid values.")
                continue
            
            dice = str(num_dice) + 'd' + str(value_dice)
            response = calculate_and_display_probability_one_dice_meets(dice, target)
            print("----------------------")
            print(response)
            print("----------------------")
    
        elif choice == '0':
            print("Exiting. Have a nice day!")
            break

        else:
            print("Invalid choice. Enter a number from [1-7] or 0 to exit.")
            continue

if __name__ == "__main__":
    main()
