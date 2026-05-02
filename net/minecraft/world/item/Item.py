import net.minecraft.text.Text as text
import net.minecraft.util.translation.Lang as lang
from net.minecraft.client.Client import *
from net.minecraft.textures.Textures import load_texture

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
	if item != "air":
		container_items[slot]=(texture, item, slot)
		if slot <=8:
			selected_item[slot]=item
	else:
		pass


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
add_item("deepslate_bricks", "deepslate_bricks", 20),
add_item("polished_deepslate", "polished_deepslate", 19),

TEXTURE_MAP = {
    "stone_bricks": load_texture("assets/minecraft/textures/block/stone_bricks.png"),
    "dirt": load_texture("assets/minecraft/textures/block/dirt.png"),
    "grass_block_side": load_texture("assets/minecraft/textures/block/grass_block_side.png"),
    "grass_block_top": load_texture("assets/minecraft/textures/block/grass_block_top.png"),
    "stone": load_texture("assets/minecraft/textures/block/stone.png"),
    "bedrock": load_texture("assets/minecraft/textures/block/bedrock.png"),
    "deepslate": load_texture("assets/minecraft/textures/block/deepslate.png"),
    "deepslate_top": load_texture("assets/minecraft/textures/block/deepslate_top.png"),
    "cobblestone":load_texture("assets/minecraft/textures/block/cobblestone.png"),
    "oak_planks":load_texture("assets/minecraft/textures/block/oak_planks.png"),
    "oak_log":load_texture("assets/minecraft/textures/block/oak_log.png"),
    "oak_log_top":load_texture("assets/minecraft/textures/block/oak_log_top.png"),
    "white_wool":load_texture("assets/minecraft/textures/block/white_wool.png"),
    "light_blue_wool":load_texture("assets/minecraft/textures/block/light_blue_wool.png"),
    "green_wool":load_texture("assets/minecraft/textures/block/green_wool.png"),
    "black_wool":load_texture("assets/minecraft/textures/block/black_wool.png"),
    "blue_wool":load_texture("assets/minecraft/textures/block/blue_wool.png"),
    "brown_wool":load_texture("assets/minecraft/textures/block/brown_wool.png"),
    "cyan_wool":load_texture("assets/minecraft/textures/block/cyan_wool.png"),
    "gray_wool":load_texture("assets/minecraft/textures/block/gray_wool.png"),
    "light_gray_wool":load_texture("assets/minecraft/textures/block/light_gray_wool.png"),
    "lime_wool":load_texture("assets/minecraft/textures/block/lime_wool.png"),
    "magenta_wool":load_texture("assets/minecraft/textures/block/magenta_wool.png"),
    "orange_wool":load_texture("assets/minecraft/textures/block/orange_wool.png"),
    "pink_wool":load_texture("assets/minecraft/textures/block/pink_wool.png"),
    "purple_wool":load_texture("assets/minecraft/textures/block/purple_wool.png"),
    "red_wool":load_texture("assets/minecraft/textures/block/red_wool.png"),
    "yellow_wool":load_texture("assets/minecraft/textures/block/yellow_wool.png"),
    "oak_leaves":load_texture("assets/minecraft/textures/block/oak_leaves.png"),
    "glass_block":load_texture("assets/minecraft/textures/block/glass.png"),
    "smooth_stone":load_texture("assets/minecraft/textures/block/smooth_stone.png"),
    "gold_block":load_texture("assets/minecraft/textures/block/gold_block.png"),
    "diamond_block":load_texture("assets/minecraft/textures/block/diamond_block.png"),
    "lapis_block":load_texture("assets/minecraft/textures/block/lapis_block.png"),
    "iron_block":load_texture("assets/minecraft/textures/block/iron_block.png"),
    "bricks":load_texture("assets/minecraft/textures/block/bricks.png"),
    "deepslate_bricks":load_texture("assets/minecraft/textures/block/deepslate_bricks.png"),
    "polished_deepslate":load_texture("assets/minecraft/textures/block/polished_deepslate.png")
}

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
	"bricks":"bricks",
	"deepslate_bricks":"deepslate_bricks",
	"polished_deepslate":"polished_deepslate"
}

def render_items_for_hotbar():
	global selected_item
	for i in range(9):
		tex_name, name, slot=container_items[i]
		scale = 0.6
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glBindTexture(GL_TEXTURE_2D, TEXTURE_MAP[tex_name])
		glColor3f(1,1,1)
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
			glBindTexture(GL_TEXTURE_2D, TEXTURE_MAP[str(texture)])
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
			if name_!="air":
				text.render_item_name(lang.get_lang_key(name_), mx, my)
	for event in events:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			for x, y , slot_, name_ in slot_coords:
				if mx >= x and mx <= x + quad_w and my >= y and my <= y + quad_h:
					if name_!="air":
						add_item(ITEM_TEXTUE_MAP[name_],name_ , hotbar_slot_selected-1)