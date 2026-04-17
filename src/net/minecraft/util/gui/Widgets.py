import net.minecraft.text.Text as Text
from net.minecraft.textures.Textures import*

button_texture=load_texture("assets/minecraft/textures/gui/sprites/widget/button.png")
button_highlighted_texture=load_texture("assets/minecraft/textures/gui/sprites/widget/button_highlighted.png")
slider_texture=load_texture("assets/minecraft/textures/gui/sprites/widget/slider.png")
slider_handle_texture=load_texture("assets/minecraft/textures/gui/sprites/widget/slider_handle.png")
slider_handle_highlighted_texture=load_texture("assets/minecraft/textures/gui/sprites/widget/slider_handle_highlighted.png")

def button(x1, y1, x2, y2, button_text, highlighted):
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)
	glColor4f(1,1,1,1)
	if highlighted==True:
		glBindTexture(GL_TEXTURE_2D, button_highlighted_texture)
	else:
		glBindTexture(GL_TEXTURE_2D, button_texture)
	uv=[(0,1),(1,1),(1,0),(0,0)]
	glBegin(GL_QUADS)
	glTexCoord2fv(uv[0])
	glVertex2f(x1,y1)
	glTexCoord2fv(uv[1])
	glVertex2f(x2,y1)
	glTexCoord2fv(uv[2])
	glVertex2f(x2, y2)
	glTexCoord2fv(uv[3])
	glVertex2f(x1, y2)
	glEnd()
	button_width=((x2-x1)/len(button_text))
	button_height=(y2-y1)
	text_width=button_width*40/100
	text_height=button_height*40/100
	button_x=(button_width-text_width)/2+x1
	button_y=(button_height-text_height)/2+y1
	Text.render_text(button_text, button_x + 5, button_y, text_height, text_height, [255, 255, 255, 255])

def slider(x1, y1, x2, y2, highlighted, handle_x, button_text):
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)
	glColor4f(1,1,1,1)
	glBindTexture(GL_TEXTURE_2D, slider_texture)
	uv=[(0,1),(1,1),(1,0),(0,0)]
	glBegin(GL_QUADS)
	glTexCoord2fv(uv[0])
	glVertex2f(x1,y1)
	glTexCoord2fv(uv[1])
	glVertex2f(x2,y1)
	glTexCoord2fv(uv[2])
	glVertex2f(x2,y2)
	glTexCoord2fv(uv[3])
	glVertex2f(x1,y2)
	glEnd()
	if highlighted==True:
		glBindTexture(GL_TEXTURE_2D, slider_handle_highlighted_texture)
	else:
		glBindTexture(GL_TEXTURE_2D, slider_handle_texture)
	glBegin(GL_QUADS)
	glTexCoord2fv(uv[0])
	glVertex2f(x1+handle_x,y1)
	glTexCoord2fv(uv[1])
	glVertex2f(x1+handle_x+((x2-x1)/25),y1)
	glTexCoord2fv(uv[2])
	glVertex2f(x1+handle_x+((x2-x1)/25),y2)
	glTexCoord2fv(uv[3])
	glVertex2f(x1+handle_x,y2)
	glEnd()
	button_width=((x2-x1)/len(button_text))
	button_height=(y2-y1)
	text_width=button_width*40/100
	text_height=button_height*40/100
	button_x=(button_width-text_width)/2+x1
	button_y=(button_height-text_height)/2+y1
	Text.render_text(button_text, button_x + 5, button_y, text_height, text_height, [255, 255, 255, 255])
