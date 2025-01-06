from calculations.success_rate import calculate_success_rate
from calculations.average_result import calculate_average_result

def calculate_critical_damage(damage_formula):
    """Calculate the average critical damage based on the provided formula."""
    instances = damage_formula.split('+')
    critical_damage = 0

    for instance in instances:
        instance = instance.strip()

        if 'd' in instance:
            try:
                num_dice, dice_value = map(int, instance.split('d'))
                critical_average = (dice_value + 1) / 2 * (num_dice * 2)  # Double the dice rolls
            except ValueError:
                print(f"Invalid expression in damage formula: {instance}")
                return None
        else:
            try:
                critical_average = int(instance)  # Flat values are not doubled
            except ValueError:
                print(f"Invalid expression in damage formula: {instance}")
                return None

        critical_damage += critical_average
    return critical_damage

def damage_per_round(modifier, proficiency, additional_bonus, ac, damage_formula, attacks_per_turn, advantage, bonus_attacks, bonus_damage_formula):
    """Calculate the Damage Per Round (DPR) with critical hits included."""
    # Calculate hit chance
    hit_chance = calculate_success_rate(modifier, proficiency, additional_bonus, ac, advantage)

    # Calculate critical chance
    critical_chance = 0.05 if advantage == 0 else 1 - ((19 / 20) ** 2)

    # Calculate average damage
    average_damage = calculate_average_result(damage_formula)

    # Calculate average critical damage
    average_critical_damage = calculate_critical_damage(damage_formula)

    # Calculate normal attack damage contribution
    normal_damage = (hit_chance - (critical_chance * 100)) / 100 * average_damage
    critical_damage_contribution = critical_chance * average_critical_damage

    # Total damage for regular attacks
    regular_attack_dpr = attacks_per_turn * (normal_damage + critical_damage_contribution)

     # Calculate bonus attack damage
    if bonus_attacks > 0:
        bonus_average_damage = calculate_average_result(bonus_damage_formula)
        bonus_critical_damage = calculate_critical_damage(bonus_damage_formula)

        bonus_normal_damage = (hit_chance - (critical_chance * 100)) / 100 * bonus_average_damage
        bonus_critical_damage_contribution = critical_chance * bonus_critical_damage

        # Total damage for bonus attacks
        bonus_attack_dpr = bonus_attacks * (bonus_normal_damage + bonus_critical_damage_contribution)
    else:
        bonus_attack_dpr = 0

    # Combine regular and bonus attack DPR
    dpr = regular_attack_dpr + bonus_attack_dpr

    return hit_chance, critical_chance, average_damage, average_critical_damage, bonus_attack_dpr, dpr
