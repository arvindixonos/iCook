from enum import Enum
from Tray import Tray
from Singleton import Singleton
from Enums import eIngredientType


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

