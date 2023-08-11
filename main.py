import cv2
import mediapipe as mp
from threadedCam import threadedCam
from calculateCollisions import calculateCollisions
from Ball import Ball

#Next Steps: determine what way the ball should bounce based on how it impacts the hand | optimize hand detection??? need something faster maybe some python shape library? consider not a cv2 shape but a py shape object
#Hardware limitations: run it on an embeded system + lidar for better distance detection and fidelitey in low light environments

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 2, model_complexity = 1, min_detection_confidence = 0.7, min_tracking_confidence = 0.1)
mpDraw = mp.solutions.drawing_utils

cap = threadedCam(0).start()

sequence_landmark_list = []

ball = Ball(100, 300, 12, 10, "moving")

while True:

    bg = cv2.imread("image.png")

    frame = cap.read()

    frame = cv2.resize(frame, None, None, fx = 0.3, fy = 0.3, interpolation = cv2.INTER_LANCZOS4)
    x, y, c = frame.shape

    frame =  cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)

    landmarks = []

    if result.multi_hand_landmarks:
        
        for handslms in result.multi_hand_landmarks: # MULTI_HAND_LANDMARKS a list of LANDMARK objects | MULTI_HAND_WORLD_LANDMARKS is a list of the actual normalized coordinates | MULTI_HANDEDNESS is which hand it is
            for lm in handslms.landmark: #this provides normalized coords
                landmarks.append([int(lm.x * 1000), int(lm.y * 600)])
                #mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
                #mpDraw.draw_landmarks(bg, handslms, mpHands.HAND_CONNECTIONS)
        orderedLandmarks = calculateCollisions.orderedLandmarks(landmarks) #ordered landmark format = [[[0x, 0y], [1x, 1y]...], [[0x, 0y], [1x, 1y]....]....]

        for segment in orderedLandmarks: #draws the lines between the circles of the hand
            for index, value in enumerate(segment):
                if(index != (len(segment) - 1)):
                    pt1 = (value[0], value[1])
                    pt2 = (segment[index + 1][0], segment[index + 1][1])
                    cv2.line(bg, pt1, pt2, (255, 255, 255), 5)
       
        for item in landmarks: #draws the circles that make up the hand
            cv2.circle(bg, (item[0], item[1]), 5, (0, 0, 255), -1) 
                                                  #B, G, R

    touched = calculateCollisions.checkCollision(ball.posX, ball.posY, 20, landmarks)
    ball.updateBall(bg, touched)

    cv2.line(bg, (500, 0), (500, 600), (255, 255, 255), 3)
    #cv2.imshow("Output", frame)
    cv2.imshow("Output", bg)

    if cv2.waitKey(1) == ord ('q'):
        break

cap.stop()

cv2.destroyAllWindows()