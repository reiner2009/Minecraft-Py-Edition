class AxisProperty:
    def __init__(self, AXIS="y"):
        self.AXIS_KEYS=["x","y","z"]
        if AXIS in self.AXIS_KEYS:
            self.AXIS = AXIS
        else:
            self.AXIS = "y"
    def setAxis(self, AXIS):
        if AXIS in self.AXIS_KEYS:
            self.AXIS = AXIS
        else:
            self.AXIS = "y"
    def getAxis(self):
        return self.AXIS
    def getAxisKeys(self):
        return self.AXIS_KEYS

class FacingProperty:
    def __init__(self, FACING="south"):
        self.FACING_KEYS=["north","east","south","west"]
        if FACING in self.FACING_KEYS:
            self.FACING = FACING
        else:
            self.FACING = "south"
    def setFacing(self, FACING):
        if FACING in self.FACING_KEYS:
            self.FACING = FACING
        else:
            self.FACING = "south"
    def getFacing(self):
        return self.FACING
    def getFacingKeys(self):
        return self.FACING_KEYS

class TwoDirectionsProperty:
    def __init__(self, DIRECTION="x"):
        self.DIRECTION_KEYS=["x","z"]
        if DIRECTION in self.DIRECTION_KEYS:
            self.DIRECTION = DIRECTION
        else:
            self.DIRECTION = "x"
    def setDirection(self, DIRECTION):
        if DIRECTION in self.DIRECTION_KEYS:
            self.DIRECTION = DIRECTION
        else:
            self.DIRECTION = "x"
    def getDirection(self):
        return self.DIRECTION
    def getDirectionKeys(self):
        return self.DIRECTION_KEYS

class StairSetProperty:
    def __init__(self, STAIR_SET="south0"):
        self.STAIR_SET_KEYS=["north0","east0","south0","west0","north1","east1","south1","west1"]
        if STAIR_SET in self.STAIR_SET_KEYS:
            self.STAIR_SET = STAIR_SET
        else:
            self.STAIR_SET = "south0"
    def setStairSet(self, STAIR_SET):
        if STAIR_SET in self.STAIR_SET_KEYS:
            self.STAIR_SET = STAIR_SET
        else:
            self.STAIR_SET = "south0"
    def getStairSet(self):
        return self.STAIR_SET
    def getStairSetKeys(self):
        return self.STAIR_SET_KEYS

class DoorSetProperty:
    def __init__(self, DIRECTION="south0"):
        self.DIRECTION_KEYS=["north0","east0","south0","west0","north1","east1","south1","west1"]
        if DIRECTION in self.DIRECTION_KEYS:
            self.DIRECTION=DIRECTION
        else:
            self.DIRECTION = "south0"
    def setDirection(self, DIRECTION):
        if DIRECTION in self.DIRECTION_KEYS:
            self.DIRECTION = DIRECTION
        else:
            self.DIRECTION = "south0"
    def getDirection(self):
        return self.DIRECTION
    def getDirectionKeys(self):
        return self.DIRECTION_KEYS