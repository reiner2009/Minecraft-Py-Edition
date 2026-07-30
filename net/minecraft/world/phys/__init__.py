class AABB:
    def __init__(self, minX,minY,minZ,maxX,maxY,maxZ,x_offset=0, y_offset=0, z_offset=0):
        self.minX,self.minY,self.minZ,self.maxX,self.maxY,self.maxZ=minX+x_offset,minY+y_offset,minZ+z_offset,maxX+x_offset,maxY+y_offset,maxZ+z_offset
    def intersects(self, other):
        return (
            self.minX < other.maxX and
            self.maxX > other.minX and
            self.minY < other.maxY and
            self.maxY > other.minY and
            self.minZ < other.maxZ and
            self.maxZ > other.minZ
        )