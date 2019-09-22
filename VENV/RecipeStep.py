from enum import Enum

class eRecipeStepType(Enum):
    IDLE = 0,
    HEAT = 1,
    ADD_INGREDIENT = 2,
    FRY_IDLE = 3,
    FRY_STIR = 4,
    SAUTE = 5,
    POUR = 6,
    SPRINKLE = 7,
    COVER_COOK = 8,
    PLACE = 9

class RecipeStep:
    recipeStepType = eRecipeStepType.IDLE
    duration = 0.0
    payload = None

    def __init__(self, recipeStepType, duration, payload):
        self.recipeStepType = recipeStepType
        self.duration = duration
        self.payload = payload

