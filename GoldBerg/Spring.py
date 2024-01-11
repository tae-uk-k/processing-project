
class Spring:
    def __init__(self, springX, springY):
        self.springHeight = 32
        self.left = 380  
        self.right = 520
        self.maxHeight = 300  
        self.minHeight = 10 
        self.over = False 
        self.move = False
        self.ps=150
        self.springY=springY
        self.springX=springX
        self.R = 150
        self.v = 0.0
        
    def drawSpring(self):
        rectMode(CORNERS)
        noStroke()
        translate(self.springX, self.springY)
        # Draw base
        fill(0.2)
        baseWidth = 0.5 * self.ps + -8
    
        # Set color and draw top bar.
        if self.over or self.move:
            fill(220)
        else:
            fill(204)
        rect(self.left, self.ps, self.right, self.ps + self.springHeight, 50)
    
        x_previous = 450 - baseWidth
        y_previous = self.ps + self.springHeight
        stroke(255)
        for x in range(int(self.ps+self.springHeight), 300):
            y = 50 * cos((self.ps+self.springHeight)/600 * x)-(450)
            rotate(radians(90))
            if x>int(self.ps+self.springHeight):
                line(x_previous, y_previous, x, y)
            rotate(radians(-90))
            x_previous = x
            y_previous = y
        translate(-self.springX, -self.springY)
        rectMode(CORNER)
        stroke(1)
    
    def updateSpring(self):
        M,K,D,R,a,f=0.8,0.2,0.92,150,0,0
        translate(self.springX, self.springY)
        if not self.move:
            f = -K * (self.ps - R)  # f=-ky
            a = f / M  # Set the acceleration. f=ma == a=f/m
            self.v = D * (self.v + a)  # Set the velocity.
            self.ps = self.ps + self.v  # Updated position
        if abs(self.v) < 0.1:
            self.v = 0.0
        # Test if mouse is over the top bar
        self.over = (self.left < mouseX-self.springX < self.right) and (self.ps < mouseY-self.springY < self.ps + self.springHeight)
        # Set and constrain the position of top bar.
        if self.move:
            self.ps = mouseY - self.springY - self.springHeight / 2
            if self.ps > self.maxHeight:
                self.ps = self.maxHeight
            elif self.ps < self.minHeight:
                self.ps = self.minHeight
        translate(-self.springX, -self.springY)
