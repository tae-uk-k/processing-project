slideX=[410, 510, 300, 550]
slideY=[750, 950, 1150, 750]
slideR=[30, -30, -20, -60] #-90 < rot < 90

def fall_check():
    for slide in range(0, len(slideX)):
        if slideX[slide]-sW/2 cX < slideX[slide]+sW/2 and slideY[slide]<=tan(slideR[slide])*cX <= slideY[slide]+5:
            fall=False
        else:
            fall=True
