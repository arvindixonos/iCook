from Singleton import Singleton
from multiprocessing import Process, Manager, Dict, List, Value
from MoveManager import MoveManager
import time

class CookingManager(Singleton):

    currentStep = 0

    currentLoadedRecipe = None
    cookingProcess = None
    isCooking = None
    multiprocessingManager = None
    recipeQueue = None


    def CookingProcess(self, recipeQueue, isCooking):

        isCooking = False

        while True:

            if self.recipeQueue.items():

                isCooking = True

                recipeName, recipe = recipeQueue.popitem()

                recipeSteps = recipe.recipeSteps

                print ("Cooking Recipe {}".format(recipeName))

                for recipeStep in recipeSteps:
                    self.PerformRecipeStep(recipeStep)

            isCooking = False

            time.sleep(0.5)


    def __init__(self):
        self.currentStep = 0
        self.currentLoadedRecipe = None
        self.multiprocessingManager = Manager()
        self.isCooking = self.multiprocessingManager.Value('b', False)
        self.recipeQueue = self.multiprocessingManager.dict()
        self.cookingProcess = Process(target=self.CookingProcess, args=(self.recipeQueue, self.isCooking))
        self.cookingProcess.start()

    def LoadRecipe(self, recipeName):
        recipeLoaded, self.currentLoadedRecipe = self.recipeManager.LoadRecipe(recipeName)
        return recipeLoaded

    def isRecipeLoaded(self):
        return self.currentLoadedRecipe is not None

    def GetCurrentLoadedRecipe(self):
        return self.currentLoadedRecipe

    def CookRecipe(self, recipeName):

        recipeLoaded = self.LoadRecipe(recipeName)

        if recipeLoaded is True:
            recipeLoaded[recipeName] = self.currentLoadedRecipe

        else:
            print ("Recipe not loaded")


    def PerformRecipeStep(self, recipeStep):
        recipeStepType = recipeStep.recipeStepType
        stepDuration = recipeStep.duration

        if recipeStepType == eRecipeStepType.ADD_INGREDIENT:
            MoveManager.getInstance()


