from net.minecraft.client.render.world.entity.PlayerEntityModel import render_body_layer, render_arms, cos, sin
from net.minecraft.client.Textures import load_texture
from net.minecraft.world.entity.LivingEntity import LivingEntity
from net.minecraft.world.phys import AABB
from net.minecraft.world.chunk.Chunk import get_block_data
from net.minecraft.util import Override
from net.minecraft.world.EntityList import entity_chunk

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
        self.HITBOX=AABB(self.x-0.3, self.y-1.5, self.z-0.3, self.x+0.3, self.y+0.3, self.z+0.3)
        self.skin, self.w, self.h = load_texture("assets/minecraft/textures/entity/player/steve.png", True)
        self.jumpDirection=0
        self.jumpHeight=0
        self.fallSpeed=0
        self.isFlying=False
        entity_chunk.remove(self)
    @Override
    def swing(self, arm):
        if arm=="left":
            self.left_arm_pitch_direction=1
        if arm == "right":
            self.right_arm_pitch_direction=1
    @Override
    def spawn(self, x, y, z, yaw=90, pitch=0):
        self.fallSpeed=0
        super().spawn(x, y, z, yaw, pitch)
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
        self.walkAnimationTick(x,y,z)
        self.move_x=True
        self.move_y=True
        self.move_z=True
        for cx in range(-2, 2):
            for cy in range(-3, 2):
                for cz in range(-2,2):
                    if AABB(self.x-0.3, self.y-1.5, self.z-0.3+z, self.x+0.3, self.y+0.3, self.z+0.3+z).intersects(get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).getCollisionShape()) and get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).hasCollision():
                        self.move_z=False
                    if AABB(self.x-0.3, self.y-1.5+y, self.z-0.3, self.x+0.3, self.y+0.3+y, self.z+0.3).intersects(get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).getCollisionShape()) and get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).hasCollision():
                        self.fallSpeed=0
                        if y<=0.0:
                            while not AABB(self.x-0.3, self.y-1.5-0.0001, self.z-0.3, self.x+0.3, self.y+0.3-0.0001, self.z+0.3).intersects(get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).getCollisionShape()) and get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).hasCollision():
                                self.y-=0.0001
                        self.move_y=False
                    if AABB(self.x-0.3+x, self.y-1.5, self.z-0.3, self.x+0.3+x, self.y+0.3, self.z+0.3).intersects(get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).getCollisionShape()) and get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).hasCollision():
                        self.move_x=False
        if self.move_x==True:
            self.x+=x
        if self.move_y==True:
            self.y+=y
        if self.move_z==True:
            self.z+=z
    def setSkin(self, path):
        self.skin, self.w, self.h = load_texture(path,True)
    @Override
    def tick(self):
        if not self.isFlying:
            if self.jumpDirection==1:
                self.move(0,0.17,0)
                self.jumpHeight+=0.17
                if self.jumpHeight>=1.1:
                    self.jumpDirection=0
                    self.jumpHeight=0
                    self.fallSpeed=0.02
            if self.jumpDirection==0:
                self.fallSpeed+=0.01
                self.move(0,-self.fallSpeed,0)
        self.HITBOX=AABB(self.x-0.3, self.y-1.5, self.z-0.3, self.x+0.3, self.y+0.3, self.z+0.3)
        if not self.movement:
            self.walk_pitch_0 = -180
            self.walk_pitch_1 = -180
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
        if self.isFlying:
            self.fallSpeed=0
    def getHitbox(self):
        return self.HITBOX
    def jumpFromGround(self):
        if self.isOnGround():
            self.jumpDirection=1
            self.jumpHeight=0
    def isOnGround(self):
        self.tisOnGround=False
        for cx in range(-2, 2):
            for cz in range(-2,2):
                cy=-2
                if AABB(self.x-0.3, self.y-1.5001, self.z-0.3, self.x+0.3, self.y+0.3, self.z+0.3).intersects(get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).getCollisionShape()) and get_block_data(cx+round(self.x),cy+round(self.y),cz+round(self.z)).hasCollision():
                    self.tisOnGround=True
        return self.tisOnGround
    def toggleFlyMode(self):
        self.isFlying=not self.isFlying
    def render(self):
        if self.thirt_person_perspective:
            render_body_layer(self.x, self.y, self.z, self.yaw,self.pitch,self.left_arm_pitch,self.right_arm_pitch,self.walk_pitch_0, self.walk_pitch_1, self.name_tag_is_visible, self.name, self.mainhand_item, self.skin, self.w, self.h)
        if self.thirt_person_perspective==0:
            render_arms(self.x+cos(self.yaw+90)*0.4, self.y-0.5, self.z+sin(self.yaw+90)*0.4, self.yaw, self.left_arm_pitch-40, self.right_arm_pitch-40, self.mainhand_item, self.skin, self.w, self.h)
    def isJumping(self):
        return self.jumpHeight>0
