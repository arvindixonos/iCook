import json
import Globals
from enum import Enum
from Globals import recipeFolderPath

class RecipeManager:




    def LoadRecipe(self, recipeName):
        recipePath = recipeFolderPath + recipeName
        file = open(recipePath, "r")
        recipeJSONString = file.read()
        file.close()

        assert False, "JSON OBJECT DECODING PENDING"

    def __init__(self):
        print("Recipe Manager")
