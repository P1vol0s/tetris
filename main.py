import pygame, time
import sys
from random import randint
W = 800
H = 900
FPS = 240
shet = 0
e = -1
fig = randint(1,7)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
gamemod = 0
element = 0
padpos = 0
changepos = 0
crut = 1
timestart = time.time()
timestart = int(timestart)
timeshet = 0
x = []
y = []
pos = []
def paden():
    global BLACK,e
    sc.fill(BLACK)
    dop()
    pad(e)
    pygame.display.update()
    time.sleep(0.1)
def dop():
    global shet,WHITE,timeshet
    shet = str(shet)
    timeshet = str(timeshet)
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('счёт = ', True, (180, 0, 0))
    text2 = f1.render(shet, True, (180, 0, 0))
    tend1 = f1.render('время: ', True, (180, 0, 0))
    tend2 = f1.render(timeshet, True, (180, 0, 0))
    sc.blit(text1, (610, 10))
    sc.blit(text2, (690, 10))
    sc.blit(tend1, (610, 30))
    sc.blit(tend2, (690, 30))
    pygame.draw.rect(sc, WHITE, (0, 20, 50, 900))
    pygame.draw.rect(sc, WHITE, (550, 20, 50, 900))
    pygame.draw.rect(sc, WHITE, (1, 850, 550, 50))
def pad(e):
    global RED,pos
    for i in range(0, e + 1):
        cub1 = pygame.Surface((50, 50))
        cub1.fill(RED)
        sc.blit(cub1, (pos[i]))

def putfig():
    global fig,x,y,pos,e
    if fig == 1:
        e += 1
        x.append(200)
        y.append(50)
        pos.append((x[e], y[e]))
        e += 1
        x.append(300)
        y.append(100)
        pos.append((x[e], y[e]))
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
    if fig == 2:
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(150)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(200)
        x.append(250)
        pos.append((x[e], y[e]))
    if fig == 3:
        e += 1
        y.append(50)
        x.append(200)
        pos.append((x[e], y[e]))
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(200)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
    if fig == 4:
        e += 1
        x.append(300)
        y.append(50)
        pos.append((x[e], y[e]))
        e += 1
        x.append(200)
        y.append(100)
        pos.append((x[e], y[e]))
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
    if fig == 5:
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(150)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(150)
        x.append(300)
        pos.append((x[e], y[e]))
    if fig == 6:
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(150)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(150)
        x.append(200)
        pos.append((x[e], y[e]))
    if fig == 7:
        e += 1
        y.append(50)
        x.append(200)
        pos.append((x[e], y[e]))
        e += 1
        y.append(50)
        x.append(250)
        pos.append((x[e], y[e]))
        e += 1
        y.append(50)
        x.append(300)
        pos.append((x[e], y[e]))
        e += 1
        y.append(100)
        x.append(250)
        pos.append((x[e], y[e]))
putfig()
pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W,H))
cub1 = pygame.Surface((50, 50))
f2 = pygame.font.Font(None, 100)
while True:
    sc.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_F1:
                pygame.quit()
                sys.exit()
                break
            elif i.key == pygame.K_LEFT:
                gamemod = 1
            elif i.key == pygame.K_RIGHT:
                gamemod = 2
            elif i.key == pygame.K_SPACE:
                gamemod = 3
            elif i.key == pygame.K_UP:
                gamemod = 4
    dop()
    if (gamemod == 1):
        for i in range(0,4):
            if x[e-i]-50 != 0:
                changepos = 1
            else:
                changepos = 2
                break
        if changepos == 1:
            for i in range(0,4):
                x[e - i] -= 50
        gamemod = 0
    if (gamemod == 2):
        for i in range(0, 4):
            if x[e - i] + 50 != 550:
                changepos = 1
            else:
                changepos = 2
                break
        if changepos == 1:
            for i in range(0, 4):
                x[e - i] += 50
        gamemod = 0
    for i in range(0,4):
        pos[e - i] = (x[e - i], y[e - i])
    if gamemod == 4:
        if fig == 1:
            if crut == 2:
                if x[e] == 50:
                    for i in range(0, 4):
                        x[e - i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                y[e - 2] += 50
                pos[e - 2] = ((x[e - 2], y[e - 2]))
                x[e - 3] -= 100
                y[e - 3] += 50
                pos[e - 3] = ((x[e - 3], y[e - 3]))
                crut = 1
            elif crut == 1:
                y[e - 2] -= 50
                pos[e - 2] = ((x[e - 2], y[e - 2]))
                x[e - 3] += 100
                y[e - 3] -= 50
                pos[e - 3] = ((x[e - 3], y[e - 3]))
                crut = 2
        if fig == 2:
            if crut == 2:
                for j in range(3, -1,-1):
                    y[e - j] -= 50 * j
                    x[e - j] -= 50 * j
                    pos[e - j] = ((x[e - j], y[e - j]))
                crut = 1
            elif crut == 1:
                if x[e] < 400:
                    for i in range(0,4):
                        y[e-i] += 50 * i
                        x[e-i] += 50 * i
                        pos[e-i] = ((x[e-i],y[e-i]))
                    crut = 2
                elif x[e] >= 400:
                    while x[e] != 350:
                        for i in range(0,4):
                            x[e-i] -= 50
                            pos[e - i] = ((x[e - i], y[e - i]))
                    for i in range(0,4):
                        y[e-i] += 50 * i
                        x[e-i] += 50 * i
                        pos[e-i] = ((x[e-i],y[e-i]))
                    crut = 2
        if fig == 4:
            if crut == 2:
                if x[e] == 500:
                   for i in range(0,4):
                       x[e-i] -= 50
                       pos[e - i] = ((x[e - i], y[e - i]))
                y[e - 2] += 50
                pos[e - 2] = ((x[e - 2], y[e - 2]))
                x[e - 3] += 100
                y[e - 3] += 50
                pos[e - 3] = ((x[e - 3], y[e - 3]))
                crut = 1

            elif crut == 1:
                y[e - 2] -= 50
                pos[e - 2] = ((x[e - 2], y[e - 2]))
                x[e - 3] -= 100
                y[e - 3] -= 50
                pos[e - 3] = ((x[e - 3], y[e - 3]))
                crut = 2
        if fig == 5:
            if crut == 4:
                if x[e] == 50:
                    for i in range(0,4):
                        x[e-i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                x[e-1] -= 150
                y[e-1] += 50
                x[e-2] -= 50
                y[e-3] -= 50
                x[e-3] -= 100
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 1
            elif crut == 3:
                if x[e] == 500:
                    for i in range(0,4):
                        x[e-i] -= 100
                        pos[e - i] = ((x[e - i], y[e - i]))
                for i in range(1,4,2):
                    x[e-i] += 100
                    y[e-i] += 50
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 4
            elif crut == 2:
                for i in range(1,4,2):
                    x[e-i] += 50
                    y[e-i] -= 100
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 3
            elif crut == 1:
                if x[e-3] == 50:
                    for i in range(0,4):
                        x[e-i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                x[e-2] += 50
                x[e-3] -= 50
                y[e-3] += 100
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 2
        if fig == 6:
            if crut == 4:
                if x[e-1] == 50:
                    for i in range(0,4):
                        x[e-i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                x[e] -= 100
                x[e-3] -= 100
                y[e-3] -= 100
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 1
            elif crut == 3:
                if x[e-3] == 500:
                    for i in range(0,4):
                        x[e-i] -= 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                for i in range(0,4,3):
                    x[e-i] += 50
                    y[e-i] += 100
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 4
            elif crut == 2:
                if x[e-1] == 500:
                    for i in range(0,4):
                        x[e-i] -= 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                for i in range(0,4,3):
                    x[e-i] += 100
                    y[e-i] -= 50
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 3
            elif crut == 1:
                if x[e] == 50:
                    for i in range(0,4):
                        x[e-i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                y[e] -= 50
                x[e] -= 50
                x[e-3] -= 50
                y[e-3] += 50
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 2
        if fig == 7:
            if crut == 4:
                if x[e] == 50:
                    for i in range(0,4):
                        x[e-i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))

                x[e-3] -= 100
                y[e] += 100
                x[e-1] += 50
                y[e-1] -= 50
                for i in range(0,4):
                    pos[e-i] = ((x[e-i], y[e-i]))
                crut = 1
            elif crut == 3:
                if x[e] == 500:
                    for i in range(0,4):
                        x[e-i] -= 50
                        pos[e - i] = ((x[e - i], y[e - i]))
                x[e-3] += 100
                crut = 4
                pos[e] = ((x[e], y[e]))
            elif crut == 2:
                x[e-1] -= 50
                y[e-1] += 50
                crut = 3
                pos[e - 2] = ((x[e - 2], y[e - 2]))
            elif crut == 1:
                y[e] -= 100
                pos[e] = ((x[e], y[e]))
                crut = 2
        gamemod = 0
    if gamemod != 3:
        timeend = time.time()
        timeend = int(timeend)
        timeshet = int(timeshet)
        for i in range(0, 8):
            if timeshet == i:
                if timeend == timestart + (i + 1):
                    timeshet += 1
    if gamemod == 3:
        for i in range(2,17):
            for j in range(0,4):
                if padpos != 2:
                    for p in range(0,e-2):
                        if ((x[e - j], (y[e - j]) + 50) != pos[p]) and ((y[e-j]) != 800):
                            padpos = 1
                        else:
                            padpos = 2
                            break
            if padpos == 1:
                for j in range(0,4):
                    y[e - j] += 50
                    pos[e - j] = ((x[e - j], y[e - j]))
        for i in range(1,17):
            for j in range(1,11):
                if (j * 50,i * 50) in pos:
                    element = 1
                else:
                    element = 0
                    break
            if element == 1:
                shet = int(shet)
                shet += 1
                shet = str(shet)
                for h in range(1,11):
                    for k in range(0,e+1):
                        if (h * 50,i * 50) == pos[k]:
                            del x[k]
                            del y[k]
                            del pos[k]
                            e -= 1
                            element = 2
                            break
            if element == 2:
                for j in range(0,e+1):
                    if y[j] < i * 50:
                        y[j] += 50
                        pos[j] = ((x[j],y[j]))
                for i in range(0, e + 1):
                    while (x[i],y[i]+50) not in pos and y[i] != 800:
                        y[i] += 50
                        pos[e - i] = ((x[e - i], y[e - i]))


        fig = randint(1,7)
        putfig()
        gamemod = 0
        crut = 1
        timestart = time.time()
        timestart = int(timestart)
        timeshet = int(timeshet)
        timeshet = 0
    for j in range(0, e-3):
        if (y[j] < 300):
            padpos = 2
            break
        else:
            padpos = 0
    if (padpos == 2) or (timeshet == 8):
        sc.fill(WHITE)
        text3 = f2.render('Игра окончена', True, (180, 0, 0))
        shet = str(shet)
        text4 = f2.render('счёт =  ', True, (180, 0, 0))
        text5 = f2.render(shet, True, (180, 0, 0))
        sc.blit(text3, (150, 300))
        sc.blit(text4, (300, 450))
        sc.blit(text5, (520, 450))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        break
    pad(e)
    pygame.display.update()
    clock.tick(FPS)