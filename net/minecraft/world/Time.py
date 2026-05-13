from net.minecraft.chat.Chat import show_text
t = 45
light=1
sunriseblend=0
sunsetblend=0

def set_tick(t_, s1, s2, l):
    global t, light, sunriseblend, sunsetblend
    t=t_
    light=l
    sunriseblend=s1
    sunsetblend=s2

def get_time():
    return t

def get_sun__blend():
    global sunriseblend, sunsetblend
    if t>=150 and t<=170:
        sunsetblend=(t-150)/20
    elif t>=190 and t<=210:
        sunsetblend=1-((t-190)/20)
    elif t>=330 and t<=350:
        sunriseblend=(t-330)/20
    elif t>=10 and t<=30:
        sunriseblend=1-((t-10)/20)

def tick(speed=0.01):
    global t, light, sunriseblend, sunsetblend
    t += speed
    if t >= 360:
        t = 0
    if (t > 350 or t < 30) and light < 1:
        light += speed / 25
    if 170 < t < 210 and light > 0.1:
        light -= speed / 25
    light = max(0.1, min(1, light))
    get_sun__blend()


def get_light():
    global light
    return light

