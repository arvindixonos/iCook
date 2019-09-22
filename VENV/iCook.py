import numpy
from RecipeManager import RecipeManager
from RecipeStep import eRecipeStepType
from CookingManager import CookingManager

class iCook:

    name = ""
    recipeManager = None
    repositoryManager = None
    cookingManager = None

    def __init__(self, name):
        self.name = name
        self.recipeManager = RecipeManager()
        self.cookingManager = CookingManager()



iCookInstance = None
def main():

    iCookInstance = iCook("Instance")
    iCookInstance.LoadRecipe("SomeName.json")

main()