from lib.recipe import *

"""
Recipe constructs with id, name, average cooking time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test recipe name", 30, 5)
    assert recipe.id == 1
    assert recipe.name == "Test recipe name"
    assert recipe.avg_cook_time == 30
    assert recipe.rating == 5