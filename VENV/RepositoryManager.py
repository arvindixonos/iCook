from enum import Enum

class eIngredientType(Enum):
    IN_CLOVE = 0,
    IN_DRY_RED_CHILLI = 1,
    IN_BLACK_PEPPER = 2,
    IN_CINNAMON_STICK = 3,
    IN_CUMIN_SEED = 4,
    IN_CORIANDER_SEED = 5,
    IN_RED_CHILLI_POWDER = 6,
    IN_TURMERIC_POWDER = 7,

class RepositoryManager:

    trays = []
    numTrays = 0

    def __init__(self, trays):
        self.trays = trays
        self.numTrays = len(trays)

    def GetIngredientTray(self, ingredientType):

        for tray in trays:
            trayIngredientType, trayAmounts = tray.GetIngredientPresent()

            if trayIngredientType != None and trayIngredientType == ingredientType:
                return tray

        return None

