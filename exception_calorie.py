class InvalidMealException(Exception):
    def __init__(self, item):
        super().__init__(f"Meal {item} is invalid!")

class BigMealException(Exception):
    def __init__(self, calories):
        super().__init__(f"Meal has {calories} calories, which is too much!")
