class PlayerEntity:
    def __init__(this):
        this.x = -10
        this.y = 2
        this.z = -2
        this.yaw = 90
        this.pitch = 0
    def spawn(this, x, y, z, yaw=90, pitch=0):
        this.x = x
        this.y = y
        this.z = z
        this.yaw = yaw
        this.pitch = pitch
    def rotate(this, yaw_change, pitch_change):
        this.yaw = (this.yaw + yaw_change)
        this.yaw = ((this.yaw + 180) % 360) - 180
        this.pitch = this.pitch - pitch_change
        this.pitch=max(-90, min(90, this.pitch))
    def get_entity_facing(this):
        return this.yaw, this.pitch
    def set_facing(this, yaw, pitch):
        this.yaw = yaw
        this.pitch = pitch
    def move(this, x,y,z):
        this.x += x
        this.y += y
        this.z += z
    def get_entity_position(this):
        return this.x, this.y, this.z
    def hitbox(this):
        return(0.6,1.8,0.6)
