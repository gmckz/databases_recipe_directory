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

"""
We can format recipes to strings nicely 
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test recipe name", 30, 5)
    assert str(recipe) == "1 - Test recipe name - 30 - 5"

"""
We can compare two identical recipes
and have them be equal
"""
def test_identical_recipes_are_equal():
    recipe1 = Recipe(1, "Test recipe name", 30, 5)
    recipe2 = Recipe(1, "Test recipe name", 30, 5)
    assert recipe1 == recipe2