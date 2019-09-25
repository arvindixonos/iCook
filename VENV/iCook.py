import numpy as np
from RecipeManager import RecipeManager
from RecipeStep import eRecipeStepType
from CookingManager import CookingManager
from MoveManager import MoveManager
from Singleton import Singleton

class iCook(metaclass=Singleton):

    name = ""
    recipeManager = None
    repositoryManager = None
    cookingManager = None

    moveManager = None

    def __init__(self, name):
        self.name = name
        # self.recipeManager = RecipeManager()
        # self.cookingManager = CookingManager()
        self.moveManager = MoveManager()
        self.moveManager.MovetoPosition([1, 0, 0])

        # targetPosition = [61, 22, 53]
        # target_frame = np.eye(4)
        # target_frame[:3, 3] = targetPosition
        # i = 0


    # def LoadReceipe(self):
    #     CookingManager.getInstance().

def main():
    iCookInstance = iCook("Lionel Tech - iCook")

    pass


main()