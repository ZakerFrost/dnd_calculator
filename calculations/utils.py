from calculations.success_rate import calculate_success_rate
from calculations.damage_per_round import damage_per_round

def calculate_and_display_hit_chance(modifier, proficiency, additional_bonus, ac):
    """Calculate the hit chance and return the message to display to the user."""
    normal_percentage = calculate_success_rate(modifier, proficiency, additional_bonus, ac)
    advantage_percentage = calculate_success_rate(modifier, proficiency, additional_bonus, ac, 1)
    bonus_text = f", bonus of {additional_bonus}" if additional_bonus != "" else ""
    response = (f"The hit chance, given a modifier of {modifier}, proficiency of {proficiency}"
                f"{bonus_text}, and an AC of {ac} is: "
                f"\r\nNormal roll = {normal_percentage}% \tAdvantage roll = {advantage_percentage}%")
    return response

def calculate_and_display_skill_check(modifier, additional_bonus, dc):
    """Calculate the chance of succeeding on a skill check and return the message to display to the user."""
    normal_percentage = calculate_success_rate(modifier, 0, additional_bonus, dc)
    advantage_percentage = calculate_success_rate(modifier, 0, additional_bonus, dc, 1)
    bonus_text = f", bonus of {additional_bonus}" if additional_bonus != "" else ""
    response = (f"The chance to pass the skill check, given a flat modifier of {modifier}"
                f"{bonus_text}, and an DC of {dc} is: "
                f"\r\nNormal roll = {normal_percentage}% \tAdvantage roll = {advantage_percentage}%")
    return response

def calculate_and_display_saving_throw(modifier, additional_bonus, dc):
    """Calculate the chance of succeeding on a saving throw and return the message to display to the user."""
    normal_percentage = calculate_success_rate(modifier, 0, additional_bonus, dc)
    advantage_percentage = calculate_success_rate(modifier, 0, additional_bonus, dc, 1)
    bonus_text = f", bonus of {additional_bonus}" if additional_bonus != "" else ""
    response = (f"The chance to pass the saving throw, given a flat modifier of {modifier}"
                f"{bonus_text}, and an DC of {dc} is: "
                f"\r\nNormal roll = {normal_percentage}% \tAdvantage roll = {advantage_percentage}%")
    return response

def calculate_and_display_damage_per_round():
    return damage_per_round()