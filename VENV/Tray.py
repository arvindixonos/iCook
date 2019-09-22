from RepositoryManager import eIngredientType
from enum import Enum


class eAmountUnitType(Enum):
    UNIT_GRAMS = 0,
    UNIT_COUNT = 1
    UNIT_LITRES = 2

class Tray:
    isIngredientPresent = False
    ingredientType = None
    amounts = {}

    def __init__(self, ingredientType):
        self.isIngredientPresent = True
        self.ingredientType = ingredientType
        self.amounts = {}

    def isTrayFree(self):
        return self.isIngredientPresent is False

    def GetIngredientPresent(self):
        if self.isIngredientPresent == True:
            return self.ingredientType, self.amounts

        return None, None

    def SetIngredient(self, ingredientType, amountType, amount):
        self.ingredientType = ingredientType
        amount[amountType] = amount
