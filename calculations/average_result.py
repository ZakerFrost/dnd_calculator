def calculate_average_result(collection):
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