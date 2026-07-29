from net.minecraft.client.render.world.entity.PlayerEntityModel import render_body_layer, render_arms, cos, sin
from net.minecraft.client.Textures import load_texture
from net.minecraft.world.entity.LivingEntity import LivingEntity
from net.minecraft.world.phys import AABB
from net.minecraft.world.chunk.Chunk import get_block
from net.minecraft.util import Override

class PlayerEntity(LivingEntity):
    def __init__(self, name_tag_is_visible=True):
        super().__init__(name_tag_is_visible)
        self.walk_pitch_0 = -180
        self.walk_pitch_1 = -180
        self.arm_pitch=0
        self.left_arm_pitch=180
        self.right_arm_pitch=180
        self.right_arm_pitch_direction=0
        self.left_arm_pitch_direction=0
        self.skin, self.w, self.h = load_texture("assets/minecraft/textures/entity/player/steve.png", True)
    @Override
    def swing(self, arm):
        if arm=="left":
            self.left_arm_pitch_direction=1
        if arm == "right":
            self.right_arm_pitch_direction=1
    def walkAnimationTick(self, x,y,z):
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
    @Override
    def move(self,x,y,z):
        radius=5
        size=radius*2+1
        for i in range(size**3):
            cx=i%size-radius
            cy=(i//size)%size-radius
            cz=i//(size*size)-radius
            if (not AABB(self.x-0.3+x, self.y-1.5, self.z-0.3, self.x+0.3+x, self.y+0.3, self.z+0.3).intersects(AABB(cx-0.5+round(self.x), cy-0.5+round(self.y), cz-0.5+round(self.z), cx+0.5+round(self.x), cy+0.5+round(self.y), cz+0.5+round(self.z)))) or get_block(cx+round(self.x),cy+round(self.y),cz+round(self.z))=="air":
                self.x+=x
                self.walkAnimationTick(x,y,z)
                return
            if (not AABB(self.x-0.3, self.y-1.5+y, self.z-0.3, self.x+0.3, self.y+0.3+y, self.z+0.3).intersects(AABB(cx-0.5+round(self.x), cy-0.5+round(self.y), cz-0.5+round(self.z), cx+0.5+round(self.x), cy+0.5+round(self.y), cz+0.5+round(self.z)))) or get_block(cx+round(self.x),cy+round(self.y),cz+round(self.z))=="air":
                self.y+=y
                self.walkAnimationTick(x,y,z)
                return
            if (not AABB(self.x-0.3, self.y-1.5, self.z-0.3+z, self.x+0.3, self.y+0.3, self.z+0.3+z).intersects(AABB(cx-0.5+round(self.x), cy-0.5+round(self.y), cz-0.5+round(self.z), cx+0.5+round(self.x), cy+0.5+round(self.y), cz+0.5+round(self.z)))) or get_block(cx+round(self.x),cy+round(self.y),cz+round(self.z))=="air":
                self.z+=z
                self.walkAnimationTick(x,y,z)
                return           
    def setSkin(self, path):
        self.skin, self.w, self.h = load_texture(path,True)
    @Override
    def tick(self):
        if not self.movement:
            self.walk_pitch_0 = -180
            self.walk_pitch_1 = -180
        if self.thirt_person_perspective:
            render_body_layer(self.x, self.y, self.z, self.yaw,self.pitch,self.left_arm_pitch,self.right_arm_pitch,self.walk_pitch_0, self.walk_pitch_1, self.name_tag_is_visible, self.name, self.mainhand_item, self.skin, self.w, self.h)
        if self.thirt_person_perspective==0:
            render_arms(self.x+cos(self.yaw+90)*0.4, self.y-0.5, self.z+sin(self.yaw+90)*0.4, self.yaw, self.left_arm_pitch-40, self.right_arm_pitch-40, self.mainhand_item, self.skin, self.w, self.h)
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
