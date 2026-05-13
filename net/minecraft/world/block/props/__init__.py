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