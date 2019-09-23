from Globals import urdfFilePath, idlePosition
from Singleton import Singleton
from MoveStateMachine import MoveStateMachine, eMoveState
from Tray import Tray
import ikpy
import time
import numpy as np
from enum import Enum



class MoveManager(Singleton):

    robotChain = None

    moveStateMachine = None

    minimumDistance = 0.0001

    onIdle = None

    def __init__(self):
        Singleton.__init__(self)
        self.robotChain = ikpy.chain.Chain.from_urdf_file(urdfFilePath)
        self.moveStateMachine = MoveStateMachine()

    def MoveStateMachineOnIdle(self):
        onIdle()

    def ChangeState(self, newState, payload):
        self.moveStateMachine.ChangeState(newState, payload)

    def isFree(self):
        return self.moveStateMachine.isIdle()

    def MovetoPosition(self, targetPosition):
        target_frame = np.eye(4)
        target_frame[:3, 3] = targetPosition
        jointsAngle = robotChain.inverse_kinematics(target_frame)

        replicatedPosition = robotChain.forward_kinematics(jointsAngle)

        if self.GetDistance(targetPosition, replicatedPosition) < self.minimumDistance:
            return True

        return False

    def MovetoTray(self, tray):
        self.ChangeState(eMoveState.MS_MOVING_TO_TRAY_HOLD_POSITION, tray)
        return True

    def ChangeState(self, newState):
        self.moveStateMachine.ChangeState(newState)

    def GetDistance(self, vector1, vector2):
        resVector = vector2 - vector1
        return np.linalg.norm(resVector)

    def AddMoveCompleteCallback(self, callback):
        self.moveCompleteCallback += callback

    def RemoveMoveCompleteCallback(self, callback):
        self.moveCompleteCallback -= callback