def generate_grocery_list(planned_meals):
    ingredients = []
    for plan in planned_meals:
        # split by comma, strip spaces
        ing = [i.strip() for i in plan.meal.ingredients.split(',')]
        ingredients.extend(ing)
    # remove duplicates and sort
    unique = sorted(set(ingredients))
    return unique
