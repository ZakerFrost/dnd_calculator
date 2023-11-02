#!/usr/bin/env python3

from calculations.utils import *
from calculations.average_result import *

def main():
    while True:
        print("\r\n")
        print("Choose a calculation:")
        print("1: Hit Chance")
        print("2: Average Damage")
        print("3: Damage Per Round [Not implemented]")
        print("4: Skill Check")
        print("5: Saving Throw")
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
            print("The average damage is: " + str(calculate_average_result(damage_collection)))
            print("----------------------")

        elif choice == '3':
            print(calculate_and_display_damage_per_round())

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

            response = calculate_and_display_skill_check(modifier, additional_bonus, dc)
            print("----------------------")
            print(response)
            print("----------------------")

        elif choice == '5':
            try:
                # Validate that the inputs
                modifier = int(input("Enter the flat modifier to add to the Saving Throw: "))
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
    
        elif choice == '0':
            print("Exiting. Have a nice day!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, 4 or 0.")
            continue

if __name__ == "__main__":
    main()
