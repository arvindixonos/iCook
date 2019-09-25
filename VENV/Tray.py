from Enums import eIngredientType
from enum import Enum
import numpy as np

class eAmountUnitType(Enum):
    UNIT_GRAMS = 0,
    UNIT_COUNT = 1
    UNIT_LITRES = 2

class Tray:

    holderPosition = None

    isIngredientPresent = False
    ingredientType = None
    amounts = {}

    def __init__(self, holderPosition):
        self.holderPosition = holderPosition
        self.isIngredientPresent = False
        self.ingredientType = None
        self.amounts = {}

    def isTrayFree(self):
        return self.isIngredientPresent is False

    def GetIngredientPresent(self):
        if self.isIngredientPresent == True:
            return self.ingredientType, self.amounts

        return None, None

    def GetHolderPosition(self):
        return self.holderPosition

    def SetIngredient(self, ingredientType, amountType, amount):
        self.ingredientType = ingredientType
        amount[amountType] = amount
