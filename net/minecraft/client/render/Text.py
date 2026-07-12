from net.minecraft.client.Textures import*
import time

ascii_texture=load_texture("assets/minecraft/textures/font/ascii.png")

def get_letter(char):
	ascii_code=ord(char)
	col=ascii_code%16
	row=ascii_code//16
	char_size=8
	atlas_size=128
	u0=col*char_size/atlas_size	
	v0=row*char_size/atlas_size
	u1=(col+1)*char_size/atlas_size
	v1=(row+1)*char_size/atlas_size
	return[(u0,v1),(u1,v1),(u1,v0),(u0,v0)]

font_width=[
	("a", 5),("b", 5),("c", 5),
	("d", 5),("e", 5),("f", 4),
	("g", 5),("h", 5),("i", 1),
	("j", 5),("k", 4),("l", 2),
	("m", 5),("n", 5),("o", 5),
	("p", 5),("q", 5),("r", 5),
	("s", 5),("t", 3),("u", 5),
	("v", 5),("w", 5),("x", 5),
	("y", 5),("z", 5),("A", 5),
	("B", 5),("C", 5),("D", 5),
	("E", 5),("F", 5),("G", 5),
	("H", 5),("I", 3),("J", 5),
	("K", 5),("L", 5),("M", 5),
	("N", 5),("O", 5),("P", 5),
	("Q", 5),("R", 5),("S", 5),
	("T", 5),("U", 5),("V", 5),
	("W", 5),("X", 5),("Y", 5),
	("Z", 5),("0", 5),("1", 5),
	("2", 5),("3", 5),("4", 5),
	("5", 5),("6", 5),("7", 5),
	("8", 5),("9", 5),(" ", 5),
	(".", 1),(":", 1),(",", 1),
	(">", 4),("<", 4),('"', 3),
	("!", 1),("@", 4),("/", 5),
	("'", 1),("?", 4),("-", 5),
	("[", 3),("]",3)
]

def pulse():
	t=time.time() % 1.0
	return t >=0.5

def render_item_name(name,x,y):
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)
	glDisable(GL_TEXTURE_2D)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glColor4f(0, 0, 0, 0.7)
	if x+len(name)*20 <=width:
		glBegin(GL_QUADS)
		glVertex2f(x, y-5)
		glVertex2f(x+len(name)*20, y-5)
		glVertex2f(x+len(name)*20, y + 25)
		glVertex2f(x, y + 25)
		glEnd()
		render_text(name, x+10, y, 20, 20)
	else:
		glBegin(GL_QUADS)
		glVertex2f(x, y-5)
		glVertex2f(x-len(name)*20, y-5)
		glVertex2f(x-len(name)*20, y + 25)
		glVertex2f(x, y + 25)
		glEnd()
		render_text(name, x+10-len(name)*20, y, 20, 20)

def render_text(text,x,y,width,height, color=[255,255,255,255], blink_cursor=False):
	if blink_cursor==True and pulse()==True:
		text=text+"|"
	text=text+" "
	r=color[0]
	g=color[1]
	b=color[2]
	a=color[3]
	for i in range(len(text)):
		for c, n in font_width:
			if c==text[i-1]:
				x=x-(8-n-1)*(width/8)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor4f(r/255,g/255,b/255, a/255)
		glBindTexture(GL_TEXTURE_2D, ascii_texture)
		uv=get_letter(text[i])
		glBegin(GL_QUADS)
		glTexCoord2fv(uv[0])
		glVertex2f(x+width*i, y)
		glTexCoord2fv(uv[1])
		glVertex2f(x+width*(i+1), y)
		glTexCoord2fv(uv[2])
		glVertex2f(x+width*(i+1), y+height)
		glTexCoord2fv(uv[3])
		glVertex2f(x+width*i, y+height)
		glEnd()

def render_text_billboard(text, x, y, z, width, height, color=[255,255,255,255]):
    glPushMatrix()
    glTranslatef(x, y, z)
    m = glGetFloatv(GL_MODELVIEW_MATRIX)
    for i in range(3):
        for j in range(3):
            m[i][j] = 1.0 if i == j else 0.0
    glLoadMatrixf(m)
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    r,g,b,a = [c/255 for c in color]
    glColor4f(r,g,b,a)
    glBindTexture(GL_TEXTURE_2D, ascii_texture)
    offset = 0
    for i, ch in enumerate(text):
        uv = get_letter(ch)
        for c, n in font_width:
            if c == ch:
                char_width = (n / 8) * width
                break
        else:
            char_width = width
        glBegin(GL_QUADS)
        glTexCoord2fv(uv[0]); glVertex3f(offset, 0, 0)
        glTexCoord2fv(uv[1]); glVertex3f(offset + char_width, 0, 0)
        glTexCoord2fv(uv[2]); glVertex3f(offset + char_width, height, 0)
        glTexCoord2fv(uv[3]); glVertex3f(offset, height, 0)
        glEnd()
        offset += char_width
    glEnable(GL_DEPTH_TEST)
    glPopMatrix()
