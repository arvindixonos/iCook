import numpy
from RecipeManager import RecipeManager
from RecipeStep import eRecipeStepType

class iCook:

    name = ""
    recipeManager = None
    ingredientsTrayMap = {}

    def __init__(self, name):
        self.name = name
        self.recipeManager = RecipeManager()

    def LoadRecipe(self, recipeName):
        recipeLoaded, recipe = self.recipeManager.LoadRecipe(recipeName)

        if recipeLoaded == True:
            CookRecipe(recipe)

        assert False, "NO IMPLEMENTATION"

    def CookRecipe(self, recipe):
        recipeSteps = recipe.recipeSteps

        for recipeStep in recipeSteps:
            PerformRecipeStep(recipeStep)

    def PerformRecipeStep(self, recipeStep):
        recipeStepType = recipeStep.recipeStepType
        stepDuration = recipeStep.duration

        if recipeStepType == eRecipeStepType.ADD_INGREDIENT:




iCookInstance = None
def main():

    iCookInstance = iCook("Instance")
    iCookInstance.LoadRecipe("SomeName.json")

main()