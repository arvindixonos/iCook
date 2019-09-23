import time
from Singleton import Singleton
from multiprocessing import Process, Manager, Dict, List, Value
from MoveManager import MoveManager
from RepositoryManager import RepositoryManager, eIngredientType
from RecipeStep import eRecipeStepType

class CookingManager(Singleton):

    currentStep = 0

    currentLoadedRecipe = None
    cookingProcess = None
    isCooking = None
    multiprocessingManager = None
    recipeQueue = None
    waitcondition = None


    def CookingProcess(self, recipe, isCooking):

        isCooking = True

        while True:

            if self.recipeQueue.items():

                isCooking = True

                recipeName, recipe = recipeQueue.popitem()

                recipeSteps = recipe.recipeSteps

                print("Cooking Recipe {}".format(recipeName))

                for recipeStep in recipeSteps:
                    self.PerformRecipeStep(recipeStep)

        isCooking = False

    def __init__(self):
        Singleton.__init__(self)
        self.currentStep = 0
        self.currentLoadedRecipe = None
        self.multiprocessingManager = Manager()
        self.isCooking = self.multiprocessingManager.Value('b', False)
        self.recipeQueue = self.multiprocessingManager.dict()
        self.waitcondition = self.multiprocessingManager.Condition()
        self.cookingProcess = None
        MoveManager.getInstance().onIdle += self.OnMachineIdle

    def OnMachineIdle(self):
        self.waitcondition.notifyAll()

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
            self.cookingProcess = Process(target=self.CookingProcess, args=(self.isCooking,))
            self.cookingProcess.start()
        else:
            print ("Recipe not loaded")

    def PerformRecipeStep(self, recipeStep):
        recipeStepType = recipeStep.recipeStepType

        if recipeStepType == eRecipeStepType.ADD_INGREDIENT:
            ingredientType = eIngredientType[recipeStep.payload]
            ingredientTray = RepositoryManager.getInstance().GetIngredientTray(ingredientType)

            if ingredientTray is not None:
                MoveManager.getInstance().MovetoTray(ingredientTray)
                self.waitcondition.wait()

                MoveManager.getInstance().HoldTray()
                self.waitcondition.wait()

                MoveManager.getInstance().TraytoDropPosition()
                self.waitcondition.wait()

                MoveManager.getInstance().DroptoPan()
                self.waitcondition.wait()

                MoveManager.getInstance().ReturnTrayToDock()
                self.waitcondition.wait()

        elif recipeStepType == eRecipeStepType.HEAT:
            stepDuration = recipeStep.duration
            targetTemperature = int(recipeStep.payload)

            MoveManager.getInstance().HeatPan(stepDuration, targetTemperature)
            self.waitcondition.wait()

        elif recipeStepType == eRecipeStepType.STIR:
            stirHeight = int(recipeStep.payload)
            stirStyle = int(recipeStep.payload)
            stepDuration = recipeStep.duration
            MoveManager.getInstance().Stir(stepDuration, stirHeight, stirStyle)
            self.waitcondition.wait()

        