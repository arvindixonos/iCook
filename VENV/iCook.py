import numpy
from RecipeManager import RecipeManager
from RecipeStep import eRecipeStepType
from CookingManager import CookingManager
from Singleton import Singleton

class iCook(Singleton):

    name = ""
    recipeManager = None
    repositoryManager = None
    cookingManager = None

    def __init__(self, name):
        self.name = name
        self.recipeManager = RecipeManager()
        self.cookingManager = CookingManager()

    def LoadReceipe(self):
        CookingManager.getInstance().

def main():

    iCookInstance = iCook.getInstance()
    iCookInstance.LoadRecipe("SomeName.json")


main()