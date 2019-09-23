from enum import Enum
from Tray import Tray
from Singleton import Singleton

class eIngredientType(Enum):
    IN_CLOVE = 0,
    IN_DRY_RED_CHILLI = 1,
    IN_BLACK_PEPPER = 2,
    IN_CINNAMON_STICK = 3,
    IN_CUMIN_SEED = 4,
    IN_CORIANDER_SEED = 5,
    IN_RED_CHILLI_POWDER = 6,
    IN_TURMERIC_POWDER = 7,

class RepositoryManager(Singleton):

    trays = []
    numTrays = 0

    def __init__(self, numTrays):
        Singleton.__init__(self)
        self.numTrays = numTrays

        for i in range(self.numTrays):
            tray = Tray()
            self.trays.append(tray)

    def GetIngredientTray(self, ingredientType):

        for i in range(self.numTrays):
            trayIngredientType, trayAmounts = trays[i].GetIngredientPresent()

            if trayIngredientType != None and trayIngredientType == ingredientType:
                return trays[i]

        return None


    def GetFreeTray(self):
        for i in range(self.numTrays):

            if trays[i].isTrayFree() is True:
                return trays[i]

        return None

