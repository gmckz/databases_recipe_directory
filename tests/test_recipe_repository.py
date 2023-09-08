from lib.recipe_repository import *
from lib.recipe import *

"""
When we call #all on RecipeRepository
it returns the list of recipes
"""
def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    
    result = repository.all()

    assert result == [
        Recipe(1, 'Fajitas', 30, 5),
        Recipe(2, 'Chilli con carne', 50, 4),
        Recipe(3, 'Soup', 5, 2),
        Recipe(4, 'Chicken pie', 60, 3),
    ]

"""
When we call #find on RecipeRepository
given the recipe id
it returns the recipe
"""
def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    assert repository.find(2) == Recipe(2, 'Chilli con carne', 50, 4)

