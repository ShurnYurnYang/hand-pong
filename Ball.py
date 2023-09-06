import cv2

class Ball:
    
    def __init__(self, posX, posY, xVelocity, yVelocity, state):
        self.vX = xVelocity
        self.vY = yVelocity
        self.posX = posX
        self.posY = posY
        self.state = state

        self.leftScore = 0
        self.rightScore = 0
    
    def updateBall(self, frame, touched):

        #touched by hand
        if touched and self.state != "touched":
            self.vX = self.vX * -1
            self.state = "touched"

        #touching top and bottom walls
        if self.posY <= 0 and self.vY < 0:
            self.vY = self.vY * -1
        if self.posY >= 324 and self.vY > 0:
            self.vY = self.vY * -1

        #touching left and right walls
        if self.posX <= 0 and self.vX < 0:
            self.vX = self.vX * -1
            self.rightScore = self.rightScore + 1
        if self.posX >= 576 and self.vX > 0:
            self.vX = self.vX * -1
            self.leftScore = self.leftScore + 1

        #state machine
        if self.state == "touched":
            if self.vX > 0 and self.posX >= 288:
                self.state = "moving"
            if self.vX < 0 and self.posX <= 288:
                self.state = "moving"

        self.posX += self.vX
        self.posY += self.vY

        cv2.circle(frame, (self.posX, self.posY), 10, (255, 255, 255), -1)

        cv2.putText(frame, str(self.leftScore), (144, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)
        cv2.putText(frame, str(self.rightScore), (432, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)