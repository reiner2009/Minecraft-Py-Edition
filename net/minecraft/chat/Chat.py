from net.minecraft.client import *
import net.minecraft.client.render.gui.Hud as hud
import net.minecraft.client.render.Text as text

temporary_texts=[]
texts=[]
LINE_HIGHT=24
CHAT_BASE_Y=100

def split_text(text, max_len=53):
    words = text.split()
    parts = []
    current = ""
    for word in words:
        if len(word) > max_len:
            if current:
                parts.append(current)
                current = ""
            for i in range(0, len(word), max_len):
                parts.append(word[i:i+max_len])
            continue
        if len(current) + len(word) + (1 if current else 0) <= max_len:
            if current:
                current += " "
            current += word
        else:
            parts.append(current)
            current = word
    if current:
        parts.append(current)
    return parts

def show_text(msg, color, lifetime=10000):
	msg=str(msg)
	msgs=split_text(msg)
	for i in msgs:
		temporary_texts.insert(0,{
			"text":i,
			"spawn_time":pygame.time.get_ticks(),
			"life_time":lifetime,
			"color":color
		})
		texts.insert(0, {
			"text":i,
			"color":color
		})
	if len(temporary_texts)>10:
		temporary_texts.pop()

def render_temporary_texts():
	current_time=pygame.time.get_ticks()
	hud.render_chat_background(98,len(temporary_texts)*24)
	for i, t in enumerate(temporary_texts[:]):
		if current_time-t["spawn_time"]>t["life_time"]:
			temporary_texts.remove(t)
			continue
		y=CHAT_BASE_Y+i*LINE_HIGHT
		text.render_text(t["text"], 15, y, 20,20,t["color"])

def render_texts():
	hud.render_chat_background(98,len(texts)*24)
	for i, t in enumerate(texts[:]):
		y=CHAT_BASE_Y+i*LINE_HIGHT
		text.render_text(t["text"], 15, y, 20,20,t["color"])
