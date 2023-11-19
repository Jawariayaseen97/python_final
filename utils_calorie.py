from backEnd.constants import calories, combos, combos2, meal_dist_by_id, meal_dist_by_name, combo_dist_by_id, combo_dist_by_name
from backEnd.exceptions import InvalidMealException, BigMealException

def calculate_total_calories(*args):
    total_calories = 0

    for item in args:
        try:
            # Check if item is a meal
            if item in meal_dist_by_id:
                total_calories += meal_dist_by_id[item]['calories']
            elif item in meal_dist_by_name:
                total_calories += meal_dist_by_name[item]['calories']

            # Check if item is a combo
            elif item in combo_dist_by_id:
                for meal_id in combo_dist_by_id[item]['meals']:
                    total_calories += meal_dist_by_id[meal_id]['calories']
            elif item in combo_dist_by_name:
                for meal_id in combo_dist_by_name[item]['meals']:
                    total_calories += meal_dist_by_id[meal_id]['calories']

            # Check if item is a standalone meal within a combo
            else:
                for combo_id in combos2:
                    if item in combos2[combo_id]['meals']:
                        for meal_id in combos2[combo_id]['meals']:
                            total_calories += meal_dist_by_id[meal_id]['calories']

        except KeyError:
            raise InvalidMealException(item)

    if total_calories > 2000:
        raise BigMealException(total_calories)

    return total_calories


def calculate_total_price(*list_of_items):
    sum_price = 0
    combo_price = 0

    for item in list_of_items:
        try:
            if item in meal_dist_by_id:
                sum_price += meal_dist_by_id[item]['price']
            elif item in meal_dist_by_name:
                sum_price += meal_dist_by_name[item]['price']
            elif item in combo_dist_by_id:
                combo_price += combo_dist_by_id[item]['price']

                for meal_id in combo_dist_by_id[item]['meals']:
                    sum_price += meal_dist_by_id[meal_id]['price']

            elif item in combo_dist_by_name:
                combo_price += combo_dist_by_name[item]['price']

                for meal_id in combo_dist_by_name[item]['meals']:
                    sum_price += meal_dist_by_id[meal_id]['price']

        except KeyError:
            raise InvalidMealException(item)

    if combo_price == 0:
        return sum_price
    else:
        return combo_price
