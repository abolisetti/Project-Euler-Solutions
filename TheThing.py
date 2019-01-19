#The thing
from pygame import *
from math import *

screen = display.set_mode((800,600))
draw.circle(screen, (255,255,0), (400, 300), 5)
draw.circle(screen, (255,255,255), (400, 300), 50, 1)
draw.circle(screen, (255,255,255), (400, 300), 75, 1)
draw.circle(screen, (255,255,255), (400, 300), 100, 1)
draw.circle(screen, (255,255,255), (400, 300), 125, 1)
draw.circle(screen, (255,255,255), (400, 300), 150, 1)
draw.circle(screen, (255,255,255), (400, 300), 175, 1)
draw.circle(screen, (255,255,255), (400, 300), 200, 1)
draw.circle(screen, (255,255,255), (400, 300), 225, 1)
draw.circle(screen, (255,255,255), (400, 300), 250, 1)

running = True
earthDeg = 0
mercuryDeg = 0
venusDeg = 0
marsDeg = 0
jupiterDeg = 0
saturnDeg = 0
uranusDeg = 0
neptuneDeg = 0
plutoDeg = 0
speed = 2
a = screen.copy()
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
#-------------------------------
    earthDeg += 1*speed
    mercuryDeg += 4.1*speed
    venusDeg += 1.6*speed
    marsDeg += 0.52*speed
    jupiterDeg += 0.08*speed
    saturnDeg += 0.03*speed
    uranusDeg += 0.01*speed
    neptuneDeg += 0.005625*speed
    plutoDeg += (0.064/16)*speed
    screen.blit(a,(0,0))

    x1 = 400 + 50 * cos(radians(mercuryDeg))
    y1 = 300 + 50 * sin(radians(mercuryDeg))

    x3 = 400 + 75 * cos(radians(earthDeg))
    y3 = 300 + 75 * sin(radians(earthDeg))

    x2 = 400 + 100 * cos(radians(venusDeg))
    y2 = 300 + 100 * sin(radians(venusDeg))

    x4 = 400 + 125 * cos(radians(marsDeg))
    y4 = 300 + 125 * sin(radians(marsDeg))

    x5 = 400 + 150 * cos(radians(jupiterDeg))
    y5 = 300 + 150 * sin(radians(jupiterDeg))

    x6 = 400 + 175 * cos(radians(saturnDeg))
    y6 = 300 + 175 * sin(radians(saturnDeg))

    x7 = 400 + 200 * cos(radians(uranusDeg))
    y7 = 300 + 200 * sin(radians(uranusDeg))

    x8 = 400 + 225 * cos(radians(neptuneDeg))
    y8 = 300 + 225 * sin(radians(neptuneDeg))

    x9 = 400 + 250 * cos(radians(plutoDeg))
    y9 = 300 + 250 * sin(radians(plutoDeg))

##    draw.line(screen, (255,255,255), (x1, y1), (x2, y2))
##    draw.line(screen, (255,255,255), (x2, y2), (x3, y3))
##    draw.line(screen, (255,255,255), (x3, y3), (x4, y4))
##    draw.line(screen, (255,255,255), (x4, y4), (x5, y5))
##    draw.line(screen, (255,255,255), (x5, y5), (x6, y6))
##    draw.line(screen, (255,255,255), (x6, y6), (x7, y7))
##    draw.line(screen, (255,255,255), (x7, y7), (x8, y8))
##    draw.line(screen, (255,255,255), (x8, y8), (x9, y9))

    ab = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9)]
    for i in ab:
        i = (int(i[0]), int(i[1]))
        draw.circle(screen, (255,255,255), i, 5)
    
    
        
#-------------------------------
    time.wait(10)
    display.flip()
quit()
