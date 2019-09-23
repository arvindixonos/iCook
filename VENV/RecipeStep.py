from enum import Enum

class eRecipeStepType(Enum):
    IDLE = 0,
    HEAT = 1,
    ADD_INGREDIENT = 2,
    STIR = 3,
    POUR = 4,
    SPRINKLE = 5,
    COVER_COOK = 6,
    PLACE = 7

class RecipeStep:
    recipeStepType = eRecipeStepType.IDLE
    duration = 0.0
    payload = None

    def __init__(self, recipeStepType, duration, payload):
        self.recipeStepType = recipeStepType
        self.duration = duration
        self.payload = payload

