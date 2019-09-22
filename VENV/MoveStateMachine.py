from enum import Enum
from statemachine import StateMachine, state

class eMoveState(Enum):
    MS_IDLE = 0,
    MS_RETURNING_TO_IDLE = 1,
    MS_MOVING_TO_TRAY_HOLD_POSITION = 2,
    MS_HOLDING_TRAY = 3,
    MS_RETRIEVE_TRAY_TO_DROP_POSITION = 4,
    MS_DROPPING_TO_PAN = 5,
    MS_RETURNING_TRAY_TO_DOCK = 6,
    MS_MOVING_TO_STIRRER_HOLD_POSITION = 7,
    MS_HOLDING_STIRRER = 8,
    MS_STIRRING = 9,
    MS_RETURNING_STIRRER_TO_DOCK = 10,


class MoveStateMachine(StateMachine):
    
