def getVoxelShapeVertices(x,y,z, box):
    new_box=[]
    for b in box:
        for (X,Y,Z) in box:
            new_box.append([X+x*2,Y+y*2,Z+z*2])
    return new_box