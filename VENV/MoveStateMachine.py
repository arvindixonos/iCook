from enum import Enum
from statemachine import StateMachine, State

class eMoveState(Enum):
    MS_IDLE = 0,
    MS_RETURNING_TO_REST_POSITION = 1,
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
    previousState = None
    currentState = None
    idleState = State(eMoveState.MS_IDLE.value, initial=True)
    returningToIdleState = State(eMoveState.MS_RETURNING_TO_REST_POSITION.value)
    moveToTrayHoldPositionState = State(eMoveState.MS_MOVING_TO_TRAY_HOLD_POSITION.value)
    holdingTray = State(eMoveState.MS_HOLDING_TRAY.value)

    OnIdle = None

    def on_enter_idleState(self):
        print("ENTER: IDLE STATE")
        self.currentState = self.idleState
        self.OnIdle()

    def on_exit_idleState(self):
        print("EXIT: IDLE STATE")

    def on_enter_returningToIdleState(self):
        print("ENTER: returningToIdleState")
        self.currentState = self.returningToIdleState

    def on_exit_returningToIdleState(self):
        print("EXIT: returningToIdleState")

    def on_enter_moveToTrayHoldPositionState(self):
        print("ENTER: moveToTrayHoldPositionState")
        self.currentState = self.moveToTrayHoldPositionState

        holderPosition = tray.GetHolderPosition()

        while self.MovetoPosition(holderPosition) is False:
            time.sleep(0.1)

        onComplete()

    def on_exit_moveToTrayHoldPositionState(self):
        print("EXIT: moveToTrayHoldPositionState")

    def on_enter_holdingTray(self):
        print("ENTER: holdingTray")

    def on_exit_holdingTray(self):
        print("EXIT: holdingTray")

    def ChangeState(self, newState):
        self.currentState.to(newState)

    def isIdle(self):
        return self.currentState == eMoveState.MS_IDLE

    def __init__(self):
        pass
        # self.OnIdle = onIdle
