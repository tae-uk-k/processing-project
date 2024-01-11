import Spring
add_library('sound')
#sound
import processing.sound as sound

#sound setting
# sound1 = None

END = 5
r1=0
r2=0
stage1 = [
          [
           [2250, 1420, 20, 4000, 15]
           ],
          [
           [960, 940, 20, "Ready                           Get                           Set                             Go!"],
           [4200, 2500]
           ]
          ]

stage2 = [
         [
          [600, 700, 10, 300, 15],
          [850, 900, 20, 300, 15],
          [1100, 1100, 30, 300, 15],
          [1350, 1300, 30, 300, 15],
          [1470, 1500, -30, 300, 15]
          ],
         [
          [475, 475],
          [1270, 1800]
          ]
         ]

stage3 = [
          [
          [550, 700, 20, 300, 15],
          [800, 900, 25, 300, 15],
          [1050, 1120, 30, 300,15],
          [700, 700, -70, 100, 15],
          [1400, 1900, 20, 200, 15],
          [1680, 2050, 0.1, 400, 15],
          [1550, 2250, 10, 600, 15]
          ],
          [
          [1350, 800, 1000, 1000, radians(70), radians(110)],
          [1350, 1300, 1, 40],#blank
          [1650, 2050, 0],
          [1880, 1650, 200,  200, radians(270), radians(360)],
          [475, 475],
          [1900, 2300]
          ]
         ]

stage4 = [
          [
           [230, 500, 45, 300, 15],
           [720, 500, -45, 300, 15],
           
           [200,1200,45,100,15],[300,1200,90,100,15],[500,1200,45,100,15],[600,1200,45,100,15],[700,1200,90,100,15],
           [200,1300,1,100,15],[300,1300,-45,100,15],[400,1300,-45,100,15],[500,1300,90,100,15],[600,1300,1,100,15],[720,1320,-45,100,15],
           [200,1400,1,100,15],[300,1400,45,100,15],[400,1400,90,100,15],[500,1400,-1,100,15],[720,1420,45,100,15],
           [200,1500,1,100,15],[300,1500,-45,100,15],[400,1500,-45,100,15],[500,1500,90,100,15],[600,1500,1,100,15],
           [180,1600,90,100,15],[300,1600,-1,100,15],[400,1600,45,100,15],[500,1600,90,100,15],[600,1600,1,100,15],[720,1620,45,100,15],
           [300,1700,1,100,15],[400,1700,-45,100,15],[500,1700,-45,100,15],[600,1700,90,100,15],[720,1700,1,100,15]
           ],
          [
           [200, 150],
           [400, 750],
           [750, 150],
           [550, 750],
           [475, 150],
           
           [400, 1200],#2
           [600, 1400],#1
           [720, 1500],#4
           [200, 1700],#3
           [820, 1300]#5
           ]
          ]

stage5 = [
          [
           [1400, 1000, 20, 2000, 15]
           ],
          [
           [900, 790, 20, "Thank You"],
           [475, 475]
           ]
          ]
gear_range=200
gear_range_start=1
gear_range_end=4000

for i in range(gear_range_start,gear_range_end,gear_range):
    for j in range(gear_range_start,gear_range_end,gear_range):
        gear_random=random(1,3)
        gear_list=[random(i,i+gear_range),random(j,j+gear_range)]
        stage1.append(gear_list)
        stage2.append(gear_list)
        stage3.append(gear_list)
        stage4.append(gear_list)
        
stages = [stage1, stage2, stage3, stage4, stage5]



slides = [
          ]

traps =[3] #position of trap

slides2 = [
            ]

springs = [
           Spring.Spring(1970-450, 2230-300)
           ]

cX=450
cY=450
cS = 10
cV = [cS, 90]
cRad = 40
time = 1
doom = 0
stage = 1
a1 = False
flying = False
floating = False
ready = True

ball_who = True
page_slide = 0
page_speed = 10

def write_word(n):
    word = slides2[n][3]
    x = slides2[n][0]
    y = slides2[n][1]
    rot = slides2[n][2]
    translate(x, y)
    rotate(radians(rot))
    fill(200)
    textSize(100)
    text(word, 0, 0)
    rotate(radians(-rot))
    translate(-x, -y)
    

def draw_slide(x, y, w, h, rot):
    fill(200)
    translate(x, y)
    rotate(radians(rot))
    rect(-w/2, -h/2, w, h)

    rotate(radians(-rot))
    translate(-x, -y)
    
###
def portal_in(n, cx, cy):
    global cX, cY, slides2
    x = slides2[n][0]
    y = slides2[n][1]
    fill(0, 0, 255)
    circle(x, y, 90)
    fill(0)
    circle(x, y, 80)
    stroke(1)
    
    dist_portal=dist(cX,cY,x,y)
    
    if dist_portal<50:
        cX=cx
        cY=cy
    
        
def portal_out(n, falling=False):
    global slides2, ball_who
    x = slides2[n][0]
    y = slides2[n][1]
    fill(200, 200, 100)
    circle(x, y, 90)
    fill(0)
    circle(x, y, 80)
    stroke(1)
    if cX == x and cY == y and falling == True:
        ball_who = True

def portal_stage(n, cx, cy):
    global stage, stages, slides, slides2, cX, cY, springs, flying, ball_who
    x = slides2[n][0]
    y = slides2[n][1]
    fill(100, 200, 255)
    circle(x, y, 90)
    fill(0)
    circle(x, y, 80)
    stroke(1)
    
    dist_portal=dist(cX,cY,x,y)
    if dist_portal<30:
        cX=cx
        cY=cy
        stage += 1
        slides = stages[stage-1][0]
        slides2 = stages[stage-1][1]
        if stage == END-1:
            springs[0].springX = 800-450
            springs[0].springY = 1900-300
        if stage == END:
            ball_who = True
        if flying == True:
            flying = False
###

def fall_check():
    global cX, cY, cV, cRad
    global slides, traps, springs, time, floating
    global flying, stage
    n=0
    if stage == END-2:
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
                    if stage == END-2 or stage == END-1:
                        for spring in springs:
                            spring.springX += (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))
                            spring.springY -= (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))
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
            
            if (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) < -1:
                if ball_who:
                    for s in range(0, len(slides)):
                        slides[s][0] += int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))-1
                        slides[s][1] -= int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))+1
                    for s in range(0, len(slides2)):
                        slides2[s][0] += int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))-1
                        slides2[s][1] -= int(dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))+1
                    if stage == END-2 or stage == END-1:
                        for spring in springs:
                            spring.springX += (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * sin(radians(slides[slide][2]))
                            spring.springY -= (dist(dx1, dy1, cX, cY) * dist(dx2, dy2, cX, cY) * sin(atan2(dy1 - cY, dx1 - cX) - atan2(dy2 - cY, dx2 - cX)) / sW - cRad/2) * cos(radians(slides[slide][2]))
                
            return fall, slide
        else:
            if flying:
                fall = 'flying'
            else:
                fall = True
    
    for spring in springs:#cannot check spring
        if spring.springY + cRad >= cY - 300 >= spring.springY - spring.R - cRad and spring.springX + 75 > cX - 450 > spring.springX - 75:
            fall = 'springed'
            slide = spring
            if spring.v > 10:
                flying = True
            if flying:
                fall = 'flying'
            return fall, slide
    
    for slide in range(0, len(slides2)):
        if len(slides2[slide]) == 6:
            if atan2(cY-slides2[slide][1], cX-slides2[slide][0]) < 0:
                angle = atan2(cY-slides2[slide][1], cX-slides2[slide][0]) + PI*2
            else:
                angle = atan2(cY-slides2[slide][1], cX-slides2[slide][0])
            if slides2[slide][5]+radians(10) > angle > slides2[slide][4]-radians(10) and slides2[slide][2]/2+35 >= dist(cX, cY, slides2[slide][0], slides2[slide][1]) >= slides2[slide][2]/2-35:
                fall = 'swinged'
                
                if time < -0.77:
                    fall = True
                flying = False
                floating = True
                break
    return fall, slide
        
def draw_hole(x, y, w, h):
    noStroke()
    fill(50)
    rect(x-w/2, y-h/2, w, h)
    fill(100)
    stroke(50)

def ball_swinging(slide):
    global slides2, cV, time, cS
    if atan2(cY-slides2[slide][1], cX-slides2[slide][0]) < 0:
        angle = atan2(cY-slides2[slide][1], cX-slides2[slide][0]) + PI*2
    else:
        angle = atan2(cY-slides2[slide][1], cX-slides2[slide][0])
    cV = [cS*time, degrees(angle-(PI/2))]
    if slide == 0:
        time -= 0.018
    if time<0.5:
        return True
    return False

def ball_move():
    global cX, cY, cV, cS, a1, ball_who, stage

    fall, slide = fall_check()
    
    if fall == True:
        if 0<cV[1]<80:
            cV[1]+=10
        elif 100<cV[1] and cV[1]< 180:
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
        if slide == 4 and (stage == END-2 or stage == END-1):
            ball_who = False
    
    for slide in range(0, len(slides)):
        slides[slide][0] -= cV[0]*cos(radians(cV[1]))
        slides[slide][1] -= cV[0]*sin(radians(cV[1]))
    for slide in range(0, len(slides2)):
        slides2[slide][0] -= cV[0]*cos(radians(cV[1]))
        slides2[slide][1] -= cV[0]*sin(radians(cV[1]))
    if stage == END-2 or stage == END-1:
        for spring in springs:
            spring.springX -= cV[0]*cos(radians(cV[1]))
            spring.springY -= cV[0]*sin(radians(cV[1]))
        
    if a1==True and stage == END-2:
        draw_hole(slides2[1][0], slides2[1][1], (0.5-time)*60, slides2[1][3])

def ball_move2():
    global cX, cY, cV, cS, page_slide, page_speed, time, floating
    time = 1
    fall, slide = fall_check()
    #print(fall)
    if fall == True:
        if 0<cV[1]<80:
            cV[1]+=7
        elif 100<cV[1] and cV[1]<= 180:
            if floating:
                cV[1]-=1.5
            else:
                cV[1]-=5
        else:
            cV=[8,90]
    elif fall == 'blocked':
        cV = [0, 0]
    elif fall == 'springed':
        cV = [0, 0]
        cY = slide.springY + slide.ps - cRad/2 + 1
    elif fall == 'swinged':
        ball_swinging(slide)
    elif fall == 'flying':
        cS = 15
        cV = [cS, 270]
    else:
        rot = slides[slide][2]%180
        cV = [8, rot]
        if slide == 4 and stage == END-2:
            ball_who = False
            
    cX += cV[0]*cos(radians(cV[1]))
    cY += cV[0]*sin(radians(cV[1]))
    if stage == END-2:
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
        for spring in springs:
            spring.springX -= page_speed
    
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
    stroke(200)
    arc(a, b, c, d, r1, r2)
    stroke(1)
    strokeWeight(1)
    fill(100)

def rotate_rectrap(n):
    global cX, cY, fixed, slides, floating
    if fixed == False and cX-100 < slides2[n][0] < cX+30 and cY-80 < slides2[n][1] < cY+80:
        slides2[n][2] += 8
        slides2[n][2] = min(90, slides2[n][2])
    if fixed == True and cX < slides2[n][0] < cX+10 and cY-80 < slides2[n][1] < cY+80:
        slides[5][2] = -0.1
        floating = False
    if slides2[n][2] >= 90:
        fixed = True
    else: fixed = False

def Gear(X,Y,radius,teeth,r):
    global r1, r2
    
    translate(X, Y)
    
    angle = 360 / teeth
    bladeSize = 30  
    rotate(radians(r))
    
    
    for i in range(teeth):
        
        out_x1 = radius * cos(radians((i-0.2) * angle))
        out_y1 = radius * sin(radians((i-0.2) * angle))
        
        out_x2 = radius * cos(radians((i+0.2) * angle))
        out_y2 = radius * sin(radians((i+0.2) * angle))
        
        
        
        in_x1 = (radius-(radius/4)) * cos(radians((i-0.5 ) * angle))
        in_y1 = (radius-(radius/4)) * sin(radians((i-0.5 ) * angle))
    
        in_x2 = (radius-(radius/4)) * cos(radians((i+0.5) * angle))
        in_y2 = (radius-(radius/4)) * sin(radians((i+0.5 ) * angle))
    
    
        noStroke()
        fill(250,250,250,50)
        quad(out_x1, out_y1, out_x2, out_y2, in_x2, in_y2, in_x1, in_y1)
        quad( in_x2, in_y2, in_x1, in_y1,0,0,0,0)
        stroke(0)
        # line(in_x, in_y, blade_x1, blade_y1)
        # # line(in_x, in_y, blade_x2, blade_y2)
    rotate(radians(-r))
    translate(-X, -Y)
    
def setup():
    global fixed
    global left, right
    global slides, slides2, stage1, stage, ball_who, cX, cY, springs, sound1
    global r1, r2
    size(950,950)
    sound1 = sound.SoundFile(this, "C:\Users\user\Downloads\Dreams.mp3")
    sound1.play()
    background(50)
    stroke(50)
    fixed = False
    stage = 1
    
    if stage == 1:
        ball_who = True
        slides = stage1[0]
        slides2 = stage1[1]
        cX = 475
        cY = 475
    if stage == END-1:
        ball_who = False
        slides = stage4[0]
        slides2 = stage4[1]
        springs[0].springX = 800-450
        springs[0].springY = 1900-300
        cX = 200
        cY = 150
    
def draw():
    global cV, cY, cX, sRot, sX, sY, sW, sH, cRad, ball_who, page_slide, slides2, slides, stage, doom,r1,r2
    background(50)
    # translate(width/2,height/2)
    Gear(200,-250,100,12,r1)
    Gear(350,-250,50,12,r2)
    Gear(-200,250,70,12,r1)
    Gear(-300,250,30,12,r2)
    # Gear(100,250,30,12,r2)
    # translate(-width/2,-height/2)
    r1+=1
    r2-=1.8
    for slide in slides:
        draw_slide(slide[0], slide[1], slide[3], slide[4], slide[2])
        
    if stage == 1:
        write_word(0)
        portal_stage(1, 475, 475)
    
    if stage == 2:
        portal_out(0)
        portal_stage(1, 475, 475)
        print(len(slides2))
        # for i in range(2, 402):
        #     Gear(slides2[i][0],slides2[i][1],100,12,r1)
        #     print('halo')
            
    
    if stage == END-2:
        for trap in traps:
            move_trap(trap)
        
        for spring in springs:
            spring.drawSpring()
            spring.updateSpring()
    
        draw_dropper(slides2[0][0], slides2[0][1], slides2[0][2], slides2[0][3], slides2[0][4], slides2[0][5])
        draw_dropper(slides2[3][0], slides2[3][1], slides2[3][2], slides2[3][3], slides2[3][4], slides2[3][5])
        draw_rectrap(2)
        rotate_rectrap(2)
        portal_out(4)
        portal_stage(5, 200, 150)
    
    [400, 1200],#2
    [600, 1400],#1
    [720, 1500],#4
    [200, 1700],#3
    
    if stage == END-1:
        portal_out(0)
        portal_in(1, 750, 150)
        portal_out(2)
        portal_in(3, 475, 150)
        portal_out(4, falling=True)
        portal_in(6, slides2[5][0], slides2[5][1])
        portal_out(5)
        portal_in(8, slides2[7][0], slides2[7][1])
        portal_out(7)
        for spring in springs:
            spring.drawSpring()
            spring.updateSpring()
        portal_stage(9, 475, 475)
    
    if ready == False:
        if ball_who == True:
            ball_move()
        elif ball_who == False:
            ball_move2()
    
    fill(200)
    circle(cX, cY, cRad)
    if stage == END:
        write_word(0)
        portal_out(1)
        doom += 1
        fill(200)
        circle(cX, cY, cRad)
        fill(0, max(0, min(doom, 255)))
        rect(0, 0, 1000, 1000)

def mousePressed():
    global ready
    if ready:
        ready = False
    for spring in springs:
        if spring.over:
            spring.move = True

def mouseReleased():
    for spring in springs:
        spring.move = False
