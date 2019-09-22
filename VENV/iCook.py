import numpy
from RecipeManager import RecipeManager

class iCook:

    name = ""
    recipeManager = None

    def __init__(self, name):
        self.name = name
        self.recipeManager = RecipeManager()

    def LoadRecipe(self, recipeName):
        self.recipeManager.LoadRecipe(recipeName)

        assert False, "NO IMPLEMENTATION"




iCookInstance = None
def main():

    iCookInstance = iCook("Instance")
    iCookInstance.LoadRecipe("SomeName.json")

main()