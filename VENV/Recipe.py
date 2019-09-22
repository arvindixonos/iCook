

class Recipe:
    recipeID = ""
    recipeName = ""

    recipeSteps = []

    def __init__(self, recipeID, recipeName):
        self.recipeID = recipeID
        self.recipeName = recipeName
        self.recipeSteps = []


    def AppendRecipeStep(self, recipeStep):
        self.recipeSteps.append(recipeStep)

    @staticmethod
    def FromJSON(jsonString):



        assert False, "FROM JSON IMPLEMENTATION PENDING"
