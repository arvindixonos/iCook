from Globals import urdfFilePath, idlePosition
from Singleton import Singleton
from Tray import Tray
import ikpy
import time
import numpy as np
from enum import Enum

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


class MoveManager(Singleton):

    robotChain = None

    currentMoveState = eMoveState.MS_RETURNING_TO_IDLE

    minimumDistance = 0.0001

    def __init__(self):
        self.robotChain = ikpy.chain.Chain.from_urdf_file(urdfFilePath)

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