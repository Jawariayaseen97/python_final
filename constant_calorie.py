class Meal:
    def __init__(self, id, name, calories, price):
        self.id = id
        self.name = name
        self.calories = calories
        self.price = price

class Combo:
    def __init__(self, id, name, meals, price):
        self.id = id
        self.name = name
        self.meals = meals
        self.price = price

meals = [
    Meal("meal-1", "Hamburger", 600, 5),
    Meal("meal-2", "Cheese Burger", 750, 7),
    Meal("meal-3", "Veggie Burger", 400, 6),
    Meal("meal-4", "Vegan Burger", 350, 6),
    Meal("meal-5", "Sweet Potatoes", 230, 3),
    Meal("meal-6", "Salad", 15, 4),
    Meal("meal-7", "Iced Tea", 70, 2),
    Meal("meal-8", "Lemonade", 90, 2)
]

combos = [
    Combo("combo-1", "Cheesy Combo", [Meal("meal-2", "Cheese Burger", 750, 7), Meal("meal-5", "Sweet Potatoes", 230, 3), Meal("meal-8", "Lemonade", 90, 2)], 11),
    Combo("combo-2", "Veggie Combo", [Meal("meal-3", "Veggie Burger", 400, 6), Meal("meal-5", "Sweet Potatoes", 230, 3), Meal("meal-7", "Iced Tea", 70, 2)], 10),
    Combo("combo-3", "Vegan Combo", [Meal("meal-4", "Vegan Burger", 350, 6), Meal("meal-6", "Salad", 15, 4), Meal("meal-8", "Lemonade", 90, 2)], 10)
]


meal_dict_by_id = {meal.id: meal for meal in meals}
meal_dict_by_name = {meal.name.lower(): meal for meal in meals}
combo_dict_by_id = {combo.id: combo for combo in combos}
combo_dict_by_name = {combo.name.lower(): combo for combo in combos}
