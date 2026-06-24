import net.minecraft.text.Text as text
import net.minecraft.util.translation.Lang as lang
from net.minecraft.client.Client import *
from net.minecraft.client.render.world.block.BlockRenderer import block_atlas, UV_MAP, block_atlas_data
from net.minecraft.resources.DataLocation import get_resource_path
import json

container_items=[]
for i in range(54):
	container_items.append(("air", "air",i))

selected_item=[]
for i in range(9):
	selected_item.append(None)
events=None

hotbar_slot_selected=0

def set_vars(event_, hotbar_slot_selected_):
	global events, hotbar_slot_selected
	events=event_
	hotbar_slot_selected=hotbar_slot_selected_

def add_item(item, slot):
	global container_items
	if item != "air":
		try:
			container_items[slot]=(texture_map[item], item, slot)
		except:
			container_items[slot] = (item, item, slot)
		if slot <=8:
			selected_item[slot]=item
	else:
		pass

ItemGroup=json.load(open(get_resource_path("data/minecraft/item/ItemGroup.json")))
for item, slot in ItemGroup.items():
	add_item(str(item), slot)

for i in range(9):
	add_item(list(ItemGroup.keys())[i], i)

slot_coords=[]
for i in range(54):
	slot_coords.append((0, 0, i, "air"))


texture_map = json.load(open(get_resource_path("assets/minecraft/item/TextureMap.json")))

def render_items_for_hotbar():
	global selected_item
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
	for i in range(9):
		tex_name, name, slot=container_items[i]
		scale = 0.6
		glColor3f(1,1,1)
		try:
			uv = UV_MAP[tex_name]
		except:
			try:
				uv = UV_MAP[texture_map[tex_name]]
			except:
				uv=UV_MAP["missing"]
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
	glBindTexture(GL_TEXTURE_2D, block_atlas)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
	for texture, name, slot in container_items:
		scale=0.5
		slots_per_row=9
		try:
			uv=UV_MAP[texture]
		except:
			try:
				uv=UV_MAP[texture_map[texture]]
			except KeyError:
				uv=UV_MAP["missing"]
		w, h = block_atlas_data["width"], block_atlas_data["height"]
		uv_map = [((uv[0]) / w, (uv[1]) / h), ((uv[0] + 1) / w, (uv[1]) / h),
				  ((uv[0] + 1) / w, (uv[1] + 1) / h), ((uv[0]) / w, (uv[1] + 1) / h)]
		orig_w = 62
		orig_h = 58
		orig_spacing = 44.5
		quad_w = orig_w * scale
		quad_h = orig_h * scale
		base_x = width / 2 - 372 / 2
		base_y = height / 1000 * 314
		col = slot % slots_per_row
		row = slot // slots_per_row
		old_left = base_x + orig_spacing * col
		old_right = old_left + orig_w
		center_x = (old_left + old_right) / 2
		x = center_x - (quad_w - 20) / 2
		old_top = base_y + orig_h
		center_y = (base_y + old_top) / 2
		extra_spacing = 11
		if row == 0:
			y = center_y - quad_h / 2
		elif row == 1:
			y = center_y - quad_h / 2 + orig_spacing + extra_spacing
		else:
			y = center_y - quad_h / 2 + orig_spacing + extra_spacing + (row - 1) * orig_spacing
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
	for x, y, slot_, name_ in slot_coords:
		if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
			if name_!="air":
				text.render_item_name(lang.get_lang_key(name_), mx, my)
	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			for x, y , slot_, name_ in slot_coords:
				if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
					if name_!="air":
						add_item(name_ , hotbar_slot_selected-1)
