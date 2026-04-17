from net.minecraft.client.Client import*
from net.minecraft.world.block.Block import*
import net.minecraft.text.Text as text
import net.minecraft.util.translation.Lang as lang
import net.minecraft.world.block.Block as block

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

def add_item(texture, item, slot):
	global container_items
	container_items[slot]=(texture, item, slot)
	if slot <=8:
		selected_item[slot]=item


slot_coords=[]
for i in range(54):
	slot_coords.append((0, 0, i, "air"))

add_item("stone_bricks", "stone_bricks", 0)
add_item("cobblestone", "cobblestone", 1)
add_item("stone", "stone", 2)
add_item("deepslate", "deepslate", 3)
add_item("bedrock", "bedrock", 4)
add_item("dirt", "dirt", 5)
add_item("grass_block_side", "grass_block", 6)
add_item("oak_planks", "oak_planks", 7)
add_item("oak_log", "oak_log", 8)
add_item("stone_bricks", "stone_bricks", 53)
add_item("cobblestone", "cobblestone", 52)
add_item("stone", "stone", 51)
add_item("deepslate", "deepslate", 50)
add_item("bedrock", "bedrock", 49)
add_item("dirt", "dirt", 48)
add_item("grass_block_side", "grass_block", 47)
add_item("oak_planks", "oak_planks", 46)
add_item("oak_log", "oak_log", 45)
add_item("white_wool", "white_wool", 44)
add_item("light_blue_wool", "light_blue_wool", 43)
add_item("green_wool", "green_wool", 42)
add_item("black_wool", "black_wool", 41)
add_item("blue_wool", "blue_wool", 40)
add_item("brown_wool", "brown_wool", 39)
add_item("cyan_wool", "cyan_wool", 38)
add_item("gray_wool", "gray_wool", 37)
add_item("light_gray_wool", "light_gray_wool", 36)
add_item("lime_wool", "lime_wool", 35)
add_item("magenta_wool", "magenta_wool", 34)
add_item("orange_wool", "orange_wool", 33)
add_item("pink_wool", "pink_wool", 32)
add_item("purple_wool", "purple_wool", 31)
add_item("red_wool", "red_wool", 30)
add_item("yellow_wool", "yellow_wool", 29)
add_item("oak_leaves", "oak_leaves", 28)
add_item("glass_block", "glass_block", 27)
add_item("smooth_stone", "smooth_stone", 26)
add_item("gold_block", "gold_block", 25)
add_item("diamond_block", "diamond_block", 24),
add_item("lapis_block", "lapis_block", 23),
add_item("iron_block", "iron_block", 22),
add_item("bricks", "bricks", 21)


ITEM_TEXTUE_MAP={
	"bedrock":"bedrock",
	"cobblestone":"cobblestone",
	"grass_block":"grass_block_side",
	"oak_planks":"oak_planks",
	"oak_log":"oak_log",
	"dirt":"dirt",
	"stone":"stone",
	"stone_bricks":"stone_bricks",
	"deepslate":"deepslate",
	"white_wool":"white_wool",
	"light_blue_wool":"light_blue_wool",
	"green_wool":"green_wool",
	"black_wool":"black_wool",
	"blue_wool":"blue_wool",
	"brown_wool":"brown_wool",
	"cyan_wool":"cyan_wool",
	"gray_wool":"gray_wool",
	"light_gray_wool":"light_gray_wool",
	"lime_wool":"lime_wool",
	"magenta_wool":"magenta_wool",
	"orange_wool":"orange_wool",
	"pink_wool":"pink_wool",
	"purple_wool":"purple_wool",
	"red_wool":"red_wool",
	"yellow_wool":"yellow_wool",
	"oak_leaves":"oak_leaves",
	"glass_block":"glass_block",
	"gold_block":"gold_block",
	"smooth_stone":"smooth_stone",
	"diamond_block":"diamond_block",
	"lapis_block":"lapis_block",
	"iron_block":"iron_block",
	"bricks":"bricks"
}

def render_items_for_hotbar():
	global selected_item
	for i in range(9):
		tex_name, name, slot=container_items[i]
		if block.TEXTURE_MAP[tex_name] in block.green_textures:
			glColor4f(158 / 255, 219 / 255, 75 / 255, 255)
		else:
			glColor4f(1,1,1,1)
		scale = 0.6
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glBindTexture(GL_TEXTURE_2D, block.TEXTURE_MAP[tex_name])
		uv=[(0,1),(1,1),(1,0),(0,0)]
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
		glTexCoord2fv(uv[0])
		glVertex2f(x, y)
		glTexCoord2fv(uv[1])
		glVertex2f(x + quad_w, y)
		glTexCoord2fv(uv[2])
		glVertex2f(x + quad_w, y + quad_h)
		glTexCoord2fv(uv[3])
		glVertex2f(x, y + quad_h)
		glEnd()

def render_items_for_container():
	global container_items, events, slot_coords, selected_item
	for texture, name, slot in container_items:
		try:
			scale=0.5
			slots_per_row=9
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
			glDisable(GL_DEPTH_TEST)
			glEnable(GL_TEXTURE_2D)
			if block.TEXTURE_MAP[texture] in block.green_textures:
				glColor4f(158 / 255, 219 / 255, 75 / 255, 255)
			else:
				glColor4f(1, 1, 1, 1)
			glBindTexture(GL_TEXTURE_2D, block.TEXTURE_MAP[str(texture)])
			uv = [(0, 1), (1, 1), (1, 0), (0, 0)]
			orig_w = 62
			orig_h = 58
			orig_spacing = 44.6
			quad_w = orig_w * scale
			quad_h = orig_h * scale
			base_x = width / 2 - 372 / 2
			base_y = height / 960 * 315
			col = slot % slots_per_row
			row = slot // slots_per_row
			old_left = base_x + orig_spacing * col
			old_right = old_left + orig_w
			center_x = (old_left + old_right) / 2
			x = center_x - (quad_w - 20) / 2
			old_top = base_y + orig_h
			center_y = (base_y + old_top) / 2
			extra_spacing = 5 * (height / 900)
			if row == 0:
				y = center_y - quad_h / 2
			elif row == 1:
				y = center_y - quad_h / 2 + orig_spacing + extra_spacing
			else:
				y = center_y - quad_h / 2 + orig_spacing + extra_spacing + (row - 1) * orig_spacing
			glBegin(GL_QUADS)
			glTexCoord2fv(uv[0])
			glVertex2f(x, y)
			glTexCoord2fv(uv[1])
			glVertex2f(x + quad_w, y)
			glTexCoord2fv(uv[2])
			glVertex2f(x + quad_w, y + quad_h)
			glTexCoord2fv(uv[3])
			glVertex2f(x, y + quad_h)
			glEnd()
			slot_coords[slot] = (x,y, slot, name)
		except:
			continue
	mx, my=pygame.mouse.get_pos()
	my=height-my
	for x, y, slot_, name_ in slot_coords:
		if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
			text.render_item_name(lang.get_lang_key(name_), mx, my)
	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			for x, y , slot_, name_ in slot_coords:
				if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
					add_item(ITEM_TEXTUE_MAP[name_],name_ , hotbar_slot_selected-1)