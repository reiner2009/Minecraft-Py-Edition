t = 7
light=1
sunriseblend=0
sunsetblend=0
light_start_fade_in=5*60
light_end_fade_in=7*60
light_start_fade_out=17*60
light_end_fade_out=19*60

def set_tick(t_, s1=None, s2=None):
    global t, sunriseblend, sunsetblend, light
    t=t_
    if s1!=None and s2!=None:
        sunriseblend=s1
        sunsetblend=s2
    else:
        if light_start_fade_in <= t_ <= light_end_fade_in:
            sunriseblend = fade_calculate(5 * 60, 5.5 * 60, 6.5 * 60, 7 * 60, 1, t_, sunriseblend)
            sunsetblend = 0
        elif light_start_fade_out <= t_ <= light_end_fade_out:
            sunsetblend = fade_calculate(17 * 60, 17.5 * 60, 18.5 * 60, 19 * 60, 1, t_, sunsetblend)
            sunriseblend = 0

def get_time():
    return round(t/60, 1)

def fade_calculate(start_fade_in,end_fade_in,start_fade_out,end_fade_out, gw, w, w_, ad=0):
    if start_fade_in <= w <= end_fade_in:
        return (w-start_fade_in)/(end_fade_in-start_fade_in)/1*gw+ad
    if start_fade_out <= w <= end_fade_out:
        return gw-((w-start_fade_out)/(end_fade_out-start_fade_out)/1*gw)+ad
    else:
        return w_


def tick(speed=0.01):
    global t, light, sunriseblend, sunsetblend
    t=t+speed
    if t==24*60:
        t=0
    if t>=light_end_fade_out or (t>=0 and t<=light_end_fade_in):
        light=0.1
    elif t>=light_end_fade_in:
        light=1
    light=fade_calculate(light_start_fade_in, light_end_fade_in, light_start_fade_out, light_end_fade_out, 0.9, t, light, 0.1)
    if light_start_fade_in <= t <= light_end_fade_in:
        sunriseblend = fade_calculate(5 * 60, 5.5 * 60, 6.5 * 60, 7 * 60, 1, t, sunriseblend)
        sunsetblend=0
    elif light_start_fade_out <= t <= light_end_fade_out:
        sunsetblend = fade_calculate(17 * 60, 17.5 * 60, 18.5 * 60, 19 * 60, 1, t, sunsetblend)
        sunriseblend=0
    else:
        sunriseblend=0
        sunsetblend=0

def get_light():
    global light
    return light

def get_sunriseblend():
    global sunriseblend
    return sunriseblend

def get_sunsetblend():
    global sunsetblend
    return sunsetblend