class AABB:
    def __init__(self, minX,minY,minZ,maxX,maxY,maxZ):
        self.minX,self.minY,self.minZ,self.maxX,self.maxY,self.maxZ=minX,minY,minZ,maxX,maxY,maxZ
    def intersects(self, other):
        return (
            self.minX < other.maxX and
            self.maxX > other.minX and
            self.minY < other.maxY and
            self.maxY > other.minY and
            self.minZ < other.maxZ and
            self.maxZ > other.minZ
        )