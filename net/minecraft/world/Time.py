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



def tick(speed=0.1):
    global t, light, sunriseblend, sunsetblend
    t += speed
    if t >= 360:
        t = 0
    if (t > 350 or t < 30) and light < 1:
        light += speed / 25
    if 170 < t < 210 and light > 0.1:
        light -= speed / 25
    if 170 <= t < 190 and sunsetblend < 1:
        sunsetblend += speed
    elif 190 <= t < 210 and sunsetblend > 0:
        sunsetblend -= speed
    if t >= 350 or t < 10 and sunriseblend < 1:
        sunriseblend += speed
    elif 10 <= t < 30 and sunriseblend > 0:
        sunriseblend -= speed
    light = max(0.1, min(1, light))
    sunsetblend = max(0, min(1, sunsetblend))
    sunriseblend = max(0, min(1, sunriseblend))


def get_light():
    global light
    return light

