
class CookingManager:

    currentStep = 0
    currentLoadedRecipe = None

    def __init__(self, numTrays):
        self.currentStep = 0
        self.currentLoadedRecipe = None

    def LoadRecipe(self, recipeName):
        recipeLoaded, self.currentLoadedRecipe = self.recipeManager.LoadRecipe(recipeName)

        return  recipeLoaded

    def isRecipeLoaded(self):
        return self.currentLoadedRecipe is not None

    def GetCurrentLoadedRecipe(self):
        return self.currentLoadedRecipe

    def CookRecipe(self, recipe):
        recipeSteps = recipe.recipeSteps

        for recipeStep in recipeSteps:
            PerformRecipeStep(recipeStep)

    def PerformRecipeStep(self, recipeStep):
        recipeStepType = recipeStep.recipeStepType
        stepDuration = recipeStep.duration

        if recipeStepType == eRecipeStepType.ADD_INGREDIENT:


