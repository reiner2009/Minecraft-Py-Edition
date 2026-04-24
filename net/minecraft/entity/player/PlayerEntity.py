from net.minecraft.client.render.entity.PlayerEntityModel import render_body_layer, render_arms, cos, sin
import net.minecraft.world.level.Level as Level
from net.minecraft.textures.Textures import load_texture


class PlayerEntity:
    def __init__(self, name_tag_is_visible=True):
        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 90
        self.pitch = 0
        self.walk_pitch_0 = -180
        self.walk_pitch_1 = -180
        self.arm_pitch=0
        self.thirt_person_perspective = 0
        self.name="StevePy"
        self.name_tag_is_visible=name_tag_is_visible
        self.walk_pitch_direction=0
        self.movement=False
        self.left_arm_pitch=180
        self.right_arm_pitch=180
        self.right_arm_pitch_direction=0
        self.left_arm_pitch_direction=0
        self.mainhand_item=None
        self.skin = load_texture("assets/minecraft/textures/entity/player/steve.png")
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
    def setName(self, name):
        self.name = name
    def setSkin(self, path):
        self.skin = load_texture(path)
    def move(self, x,y,z):
        self.x += x
        self.y += y
        self.z += z
        if z<0 or x<0 or z>0 or x>0:
            self.movement=True
            if self.walk_pitch_direction==0:
                self.walk_pitch_0+=5
                self.walk_pitch_1-=5
            if self.walk_pitch_direction ==1:
                self.walk_pitch_0-=5
                self.walk_pitch_1+=5
        if not (z<0 or x<0 or z>0 or x>0):
            self.movement=False
    def get_entity_position(self):
        return self.x, self.y, self.z
    def set_thirt_person_perspective(self):
        self.thirt_person_perspective+=1
        if self.thirt_person_perspective >= 3:
            self.thirt_person_perspective = 0
    def get_thirt_person_perspective(self):
        return self.thirt_person_perspective
    def swing(self, arm):
        if arm=="left":
            self.left_arm_pitch_direction=1
        if arm == "right":
            self.right_arm_pitch_direction=1
    def setMainhandItem(self, item):
        self.mainhand_item=item
    def tick(self):
        if not self.movement:
            self.walk_pitch_0 = -180
            self.walk_pitch_1 = -180
        if self.thirt_person_perspective and Level.isClient:
            render_body_layer(self.x, self.y, self.z, self.yaw,self.pitch,self.left_arm_pitch,self.right_arm_pitch,self.walk_pitch_0, self.walk_pitch_1, self.name_tag_is_visible, self.name, self.mainhand_item, self.skin)
        if self.thirt_person_perspective==0 and Level.isClient:
            render_arms(self.x+cos(self.yaw+90)*0.4, self.y-0.5, self.z+sin(self.yaw+90)*0.4, self.yaw, self.left_arm_pitch-40, self.right_arm_pitch-40, self.mainhand_item, self.skin)
        if self.walk_pitch_0>30-180:
            self.walk_pitch_direction=1
        if self.walk_pitch_0<-30-180:
            self.walk_pitch_direction=0
        if self.left_arm_pitch_direction==1:
            self.left_arm_pitch-=20
            if self.left_arm_pitch<=90:
                self.left_arm_pitch_direction=0
        if self.left_arm_pitch_direction==0 and self.left_arm_pitch<=180:
            self.left_arm_pitch+=20
        if self.right_arm_pitch_direction==1:
            self.right_arm_pitch-=20
            if self.right_arm_pitch<=90:
                self.right_arm_pitch_direction=0
        if self.right_arm_pitch_direction==0 and self.right_arm_pitch<=180:
            self.right_arm_pitch+=20
        if self.right_arm_pitch_direction==0 and self.right_arm_pitch>180:
            self.right_arm_pitch=180
        if self.left_arm_pitch_direction==0 and self.left_arm_pitch>180:
            self.left_arm_pitch=180