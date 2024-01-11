slides = [
          [550, 700, 20, 300, 15],
          [800, 900, 25, 300, 15],
          [1050, 1120, 30, 300,15],
          [700, 700, -70, 100, 15],
          [1400, 1900, 20, 200, 15],
          [1680, 2050, 0.1, 400, 15],
          [1600, 2200, 10, 700, 15]
          ]

traps =[3] #position of trap

slides2  = [
            [1350, 800, 1000, 1000, radians(70), radians(110)],
            [1350, 1300, 1, 40],#blank
            [1580, 2050, 0],
            [1880, 1650, 200,  200, radians(225), radians(360)]
            ]

#spring variables
springHeight = 10
left = 100      
right = 200    
maxHeight = 100
minHeight = 10
over = False
move = False
M,K,D,R,v,a,f=0.8,0.2,0.92,150,0.0,0,0
ps=R

cX=450
cY=450
cS = 10
cV = [cS, 90]
cRad = 40
time = 1
stage = 1
a1 = False

ball_who = True
page_slide = 0
page_speed = 10

def draw_slide(x, y, w, h, rot):
    translate(x, y)
    rotate(radians(rot))
    rect(-w/2, -h/2, w, h)

    rotate(radians(-rot))
    translate(-x, -y)

def spring_check():
    global cX, cY, springHeight, left, right

def fall_check():
    global cX, cY, cV, cRad
    global slides, traps
    n=0
    for slide in traps:
        sW = slides[slide][3]
        sH = slides[slide][4]
        center_x = slides[slide][0]
        center_y = slides[slide][1]
        dx1 = center_x - (sqrt(sH**2 + sW**2)/2) * cos(atan2(sH, sW) + radians(slides[slide][2]))
        dy1 = center_y - (sqrt(sH**2 + sW**2)/2) * sin(atan2(sH, sW) + radians(slides[slide][2]))
        dx2 = center_x + (sqrt(sH**2 + sW**2)/2) * cos(-atan2(sH, sW) + radians(slides[slide][2]))
        dy2 = center_y + (sqrt(sH**2 + sW**2)/2) * sin(-atan2(sH, sW) + radians(slides[slide][2]))
        
        if cRad/2 >= abs(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW)\
            and sqrt((sW + cRad)**2 + (sH + cRad)**2)/2 >= dist(center_x, center_y, cX, cY) and slide == traps[n]:
            n += 1
            fall = 'blocked'
            if (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) < -1 and ball_who:
                for s in range(0, len(slides)):
                    slides[s][0] += (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))
                    slides[s][1] -= (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))
                for s in range(0, len(slides2)):
                    slides2[s][0] += (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))
                    slides2[s][1] -= (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))
            return fall, slide
        
    for slide in range(0, len(slides)):
        sW = slides[slide][3]
        sH = slides[slide][4]
        center_x = slides[slide][0]
        center_y = slides[slide][1]
        dx1 = center_x - (sqrt(sH**2 + sW**2)/2) * cos(atan2(sH, sW) + radians(slides[slide][2]))
        dy1 = center_y - (sqrt(sH**2 + sW**2)/2) * sin(atan2(sH, sW) + radians(slides[slide][2]))
        dx2 = center_x + (sqrt(sH**2 + sW**2)/2) * cos(-atan2(sH, sW) + radians(slides[slide][2]))
        dy2 = center_y + (sqrt(sH**2 + sW**2)/2) * sin(-atan2(sH, sW) + radians(slides[slide][2]))

        if cRad/2 >= abs(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW)\
            and sqrt((sW + cRad)**2 + (sH + cRad)**2)/2 >= dist(center_x, center_y, cX, cY):
            fall = False
            if (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) < -1 and ball_who:
                for s in range(0, len(slides)):
                    slides[s][0] += int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))-1
                    slides[s][1] -= int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))+1
                for s in range(0, len(slides2)):
                    slides2[s][0] += int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))-1
                    slides2[s][1] -= int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))+1
            return fall, slide
        else: 
            fall = True
    
    for slide in range(0, len(slides2)):
        if 110 > degrees(atan2(cY-slides2[slide][1], cX-slides2[slide][0])) > 70 and slides2[slide][2]/2+25 >= dist(cX, cY, slides2[slide][0], slides2[slide][1]) >= slides2[slide][2]/2-25:
            fall = 'swinged'
            if dist(cX, cY, slides2[slide][0], slides2[slide][1])<slides2[slide][2]/2-30:
                for s in range(0, len(slides)):
                    slides[s][0] += abs(dist(cX, cY, slides2[slide][0], slides2[slide][1])-(slides2[slide][2]/2-15)) * sin(atan2(cY-slides2[slide][1], cX-slides2[slide][0]))-1
                    slides[s][1] -= abs(dist(cX, cY, slides2[slide][0], slides2[slide][1])-(slides2[slide][2]/2-15)) * cos(atan2(cY-slides2[slide][1], cX-slides2[slide][0]))+1
                for s in range(0, len(slides2)):
                    slides2[s][0] += abs(dist(cX, cY, slides2[slide][0], slides2[slide][1])-(slides2[slide][2]/2-15)) * sin(atan2(cY-slides2[slide][1], cX-slides2[slide][0]))-1
                    slides2[s][1] -= abs(dist(cX, cY, slides2[slide][0], slides2[slide][1])-(slides2[slide][2]/2-15)) * cos(atan2(cY-slides2[slide][1], cX-slides2[slide][0]))+1
            if time < -0.7:
                fall = True
            break
    return fall, slide

def draw_hole(x, y, w, h):
    noStroke()
    fill(255)
    rect(x-w/2, y-h/2, w, h)
    fill(100)
    stroke(50)

def ball_swinging(slide):
    global slides2, cV, time
    cV = [cS*time, degrees(atan2(cY-slides2[slide][1], cX-slides2[slide][0])-(PI/2))]
    time -= 0.018
    if time<0.5:
        return True
    return False

def ball_move():
    global cX, cY, cV, cS, a1, ball_who

    fall, slide = fall_check()
    
    if fall == True:
        if 0<cV[1]<80:
            cV[1]+=10
        elif 100<cV[1] and cV[2]< 180:
            cV[1]-=10
        else:
            cV=[8,90]
            
        
    elif fall == 'blocked':
        cV = [0, 0]
    elif fall == 'swinged':
        a1 = ball_swinging(slide)
    else:
        rot = slides[slide][2]%180
        cV = [8, rot]
        if slide == 4:
            ball_who = False
    
    for slide in range(0, len(slides)):
        slides[slide][0] -= cV[0]*cos(radians(cV[1]))
        slides[slide][1] -= cV[0]*sin(radians(cV[1]))
    for slide in range(0, len(slides2)):
        slides2[slide][0] -= cV[0]*cos(radians(cV[1]))
        slides2[slide][1] -= cV[0]*sin(radians(cV[1]))
    if a1==True:
        draw_hole(slides2[1][0], slides2[1][1], (0.5-time)*60, slides2[1][3])

def ball_move2():
    global cX, cY, cV, cS, page_slide, page_speed
    fall, slide = fall_check()
    if fall == True:
        cV = [5, 90]
    elif fall == 'blocked':
        cV = [0, 0]
    else:
        rot = slides[slide][2]%180
        cV = [8, rot]
        if slide == 4:
            ball_who = False
            
    cX += cV[0]*cos(radians(cV[1]))
    cY += cV[0]*sin(radians(cV[1]))
    
    if page_slide < 300:
        page_speed = 5
    else:
        page_speed = 0
    page_slide += page_speed
    
    cX -= page_speed
    for slide in range(0, len(slides)):
        slides[slide][0] -= page_speed
    for slide in range(0, len(slides2)):
        slides2[slide][0] -= page_speed


    
def rotate_seesaw(n):
    global slides, cX
    fall, slide = fall_check()
    if fall == False and slide == n:
        if cX < slides[n][0]:
            slides[n][2] -= 1
        else:
            slides[n][2] += 1

def move_trap(n):
    global slides, cX, traps
    fall, slide = fall_check()
    if slide == n:
        center_x = slides[slide][0]
        center_y = slides[slide][1]
        distance = dist(center_x, center_y, mouseX, mouseY)
        if mousePressed and distance <= 20:
            slides[slide][0] = center_x + (mouseY - center_y)*tan(slides[slide][2])
            slides[slide][1] = mouseY

def draw_rectrap(n):
    translate(slides2[n][0], slides2[n][1])
    rotate(radians(slides2[n][2]))
    fill(200)
    rect(-10, -80, 10, 80)
    rect(-80, -10, 80, 10)
    fill(100)
    rotate(radians(-slides2[n][2]))
    translate(-slides2[n][0], -slides2[n][1])

def draw_dropper(a, b, c, d, r1, r2):
    noFill()
    strokeWeight(15)
    arc(a, b, c, d, r1, r2)
    strokeWeight(1)
    fill(100)

def rotate_rectrap(n):
    global cX, cY, fixed, slides
    if fixed == False and cX-100 < slides2[n][0] < cX+30 and cY-80 < slides2[n][1] < cY+80:
        slides2[n][2] += 8
        slides2[n][2] = min(90, slides2[n][2])
    if fixed == True and cX < slides2[n][0] < cX+10 and cY-80 < slides2[n][1] < cY+80:
        slides[5][2] = -0.1
    if slides2[n][2] >= 90:
        fixed = True
    else: fixed = False
    


def setup():
    global fixed
    global left, right
    size(900,900)
    
    background(255)
    stroke(50)
    fixed = False
    
def draw():
    global cV, cY, cX, sRot, sX, sY, sW, sH, cRad, ball_who, page_slide
    background(255)
    
    for slide in slides:
        draw_slide(slide[0], slide[1], slide[3], slide[4], slide[2])
    
    for trap in traps:
        move_trap(trap)
    
    draw_dropper(slides2[0][0], slides2[0][1], slides2[0][2], slides2[0][3], slides2[0][4], slides2[0][5])
    draw_dropper(slides2[3][0], slides2[3][1], slides2[3][2], slides2[3][3], slides2[3][4], slides2[3][5])
    draw_rectrap(2)
    rotate_rectrap(2)
    
    if ball_who == True:
        ball_move()
    elif ball_who == False:
        ball_move2()
    print(ball_who)
    
    fill(100)
    circle(cX, cY, cRad)
    print(ball_who)

def mousePressed():
    global move
    if over:
        move = True

def mouseReleased():
    global move
    move = False
        
