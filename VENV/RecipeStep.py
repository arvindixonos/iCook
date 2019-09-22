from enum import Enum

class eRecipeStepType(Enum):
    IDLE,
    HEAT,
    ADD_INGREDIENT,
    FRY_IDLE,
    FRY_STIR,
    SAUTE,
    POUR,
    SPRINKLE,
    COVER_COOK,
    PLACE

class RecipeStep:
    recipeStepType = eRecipeStepType.IDLE
    duration = 0.0

    def __init__(self, recipeStepType, duration):
        self.recipeStepType = recipeStepType
        self.duration = duration

