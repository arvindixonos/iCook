from Globals import urdfFilePath, idlePosition
from Singleton import Singleton
from Tray import Tray
import ikpy
import time
import numpy as np
from enum import Enum



class MoveManager(Singleton):

    robotChain = None

    currentMoveState = eMoveState.MS_RETURNING_TO_IDLE
    previousStateQueue = []

    moveStatesQueue = []

    minimumDistance = 0.0001

    onStateComplete = None

    def __init__(self):
        self.robotChain = ikpy.chain.Chain.from_urdf_file(urdfFilePath)

    def ChangeState(self, newState, payload):
        self.previousStateQueue.append(newState)


    def MovetoPosition(self, targetPosition):
        target_frame = np.eye(4)
        target_frame[:3, 3] = targetPosition
        jointsAngle = robotChain.inverse_kinematics(target_frame)

        replicatedPosition = robotChain.forward_kinematics(jointsAngle)

        if self.GetDistance(targetPosition, replicatedPosition) < self.minimumDistance:
            return True

        return False

    def MovetoTray(self, tray):
        holderPosition = tray.GetHolderPosition()

        while self.MovetoPosition(holderPosition) is False:
            time.sleep(0.1)

        return True

    def GetDistance(self, vector1, vector2):
        resVector = vector2 - vector1
        return np.linalg.norm(resVector)

    def AddMoveCompleteCallback(self, callback):
        self.moveCompleteCallback += callback

    def RemoveMoveCompleteCallback(self, callback):
        self.moveCompleteCallback -= callback