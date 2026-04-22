from net.minecraft.client.render.entity.PlayerEntityModel import render_body_layer

class PlayerEntity:
    def __init__(self, name, name_tag_is_visible=True):
        self.x = -10
        self.y = 2
        self.z = -2
        self.yaw = 90
        self.pitch = 0
        self.thirt_person_perspective = 0
        self.name=name
        self.name_tag_is_visible=name_tag_is_visible
    def spawn(self, x, y, z, yaw=90, pitch=0):
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw
        self.pitch = pitch
    def rotate(self, yaw_change, pitch_change):
        self.yaw = (self.yaw + yaw_change)
        self.yaw = ((self.yaw + 180) % 360) - 180
        self.pitch = self.pitch - pitch_change
        self.pitch=max(-90, min(90, self.pitch))
    def get_entity_facing(self):
        return self.yaw, self.pitch
    def set_facing(self, yaw, pitch):
        self.yaw = yaw
        self.pitch = pitch
    def move(self, x,y,z):
        self.x += x
        self.y += y
        self.z += z
    def get_entity_position(self):
        return self.x, self.y, self.z
    def set_thirt_person_perspective(self):
        self.thirt_person_perspective+=1
        if self.thirt_person_perspective >= 3:
            self.thirt_person_perspective = 0
    def get_thirt_person_perspective(self):
        return self.thirt_person_perspective
    def tick(self):
        if self.thirt_person_perspective:
            render_body_layer(self.x, self.y, self.z, self.yaw, self.name_tag_is_visible, self.name)