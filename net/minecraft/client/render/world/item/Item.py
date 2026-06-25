import net.minecraft.text.Text as text
import net.minecraft.util.translation.Lang as lang
from net.minecraft.client.Client import *
from net.minecraft.client.render.world.block.BlockRenderer import block_atlas, UV_MAP, block_atlas_data
from net.minecraft.resources.DataLocation import get_resource_path
import json
import traceback

container_items_=json.load(open(get_resource_path("data/minecraft/item/ItemGroup.json")))
texture_map = json.load(open(get_resource_path("assets/minecraft/item/TextureMap.json")))
hotbar_items_=json.load(open(get_resource_path("data/minecraft/item/Hotbar.json")))
hotbar_items={}
container_items={}

for i in range(len(hotbar_items_)):
	hotbar_items[i]=hotbar_items_[i]

for i in range(len(container_items_)):
	container_items[i]=container_items_[i]

events=None
hotbar_slot_selected=0
slot_coords={}
selected_item=list(hotbar_items.values())

def set_vars(event_, hotbar_slot_selected_):
	global events, hotbar_slot_selected
	events=event_
	hotbar_slot_selected=hotbar_slot_selected_

def add_item(item, slot):
	global hotbar_items
	hotbar_items[slot]=item

def render_items_for_hotbar():
	global selected_item, hotbar_items
	selected_item=list(hotbar_items.values())
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
	scale = 0.6
	for slot in list(hotbar_items.keys()):
		name=hotbar_items[slot]
		glColor3f(1,1,1)
		try:
			uv = UV_MAP[name]
		except:
			try:
				uv = UV_MAP[texture_map[name]]
			except:
				uv=UV_MAP["translucent"]
		w, h = block_atlas_data["width"], block_atlas_data["height"]
		uv_map = [((uv[0]) / w, (uv[1]) / h), ((uv[0] + 1) / w, (uv[1]) / h),
				  ((uv[0] + 1) / w, (uv[1] + 1) / h), ((uv[0]) / w, (uv[1] + 1) / h)]
		glBegin(GL_QUADS)
		orig_w = 62
		orig_h = 59
		orig_spacing = 56
		quad_w = orig_w * scale
		quad_h = orig_h * scale
		base_x = width/2 - 510/2
		base_y = height/480 * 23
		old_left = base_x + orig_spacing * slot
		old_right = old_left + orig_w
		center_x = (old_left + old_right) / 2
		old_top = base_y + orig_h
		center_y = (base_y + old_top) / 2
		x = center_x - quad_w/2
		y = center_y - quad_h/2
		glTexCoord2fv(uv_map[3])
		glVertex2f(x, y)
		glTexCoord2fv(uv_map[2])
		glVertex2f(x + quad_w, y)
		glTexCoord2fv(uv_map[1])
		glVertex2f(x + quad_w, y + quad_h)
		glTexCoord2fv(uv_map[0])
		glVertex2f(x, y + quad_h)
		glEnd()

def render_items_for_container():
	global container_items, events, slot_coords, selected_item
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)
	glEnable(GL_BLEND)
	glColor4f(1,1,1,1)
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
	for slot in list(container_items.keys()):
		name=container_items[slot]
		glColor3f(1,1,1)
		try:
			uv = UV_MAP[name]
		except:
			try:
				uv = UV_MAP[texture_map[name]]
			except:
				uv=UV_MAP["translucent"]
		scale=0.5
		w, h = block_atlas_data["width"], block_atlas_data["height"]
		uv_map = [((uv[0]) / w, (uv[1]) / h), ((uv[0] + 1) / w, (uv[1]) / h),
				  ((uv[0] + 1) / w, (uv[1] + 1) / h), ((uv[0]) / w, (uv[1] + 1) / h)]
		orig_w = 62
		orig_h = 58
		orig_spacing = 44.5
		quad_w = orig_w * scale
		quad_h = orig_h * scale
		base_x = orig_spacing
		base_y = orig_spacing
		slots_per_row=round(width/quad_w*0.6)
		col = slot % slots_per_row
		row = slot // slots_per_row
		old_left = base_x + orig_spacing * col
		old_right = old_left + orig_w
		center_x = (old_left + old_right) / 2
		x = center_x - (quad_w - 20) / 2
		old_top = base_y + orig_h
		center_y = (base_y + old_top) / 2
		y = center_y - quad_h / 2 + orig_spacing  + (row - 1) * orig_spacing + 30
		glBegin(GL_QUADS)
		glTexCoord2fv(uv_map[3])
		glVertex2f(x, y)
		glTexCoord2fv(uv_map[2])
		glVertex2f(x + quad_w, y)
		glTexCoord2fv(uv_map[1])
		glVertex2f(x + quad_w, y + quad_h)
		glTexCoord2fv(uv_map[0])
		glVertex2f(x, y + quad_h)
		glEnd()
		slot_coords[slot] = (x,y, slot, name)
	mx, my=pygame.mouse.get_pos()
	my=height-my
	for slot_coord in slot_coords:
		(x, y, slot_, name_) = slot_coords[slot_coord]
		if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
			if name_!="air":
				text.render_item_name(lang.get_lang_key(name_), mx, my)
	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			for slot_coord in slot_coords:
				(x, y, slot_, name_) = slot_coords[slot_coord]
				if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
					if name_!="air":
						add_item(name_ , hotbar_slot_selected-1)
