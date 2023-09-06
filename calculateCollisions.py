import math
import numpy as np

class calculateCollisions:

    def checkLine(h, k, r, x1, y1, x2, y2):
       
       segmentLength = (x2 - x1)**2 + (y2 - y1)**2

       #catch 0 length segment
       if segmentLength == 0:
           return math.sqrt((h - x1)**2 + (k - y1)**2) - r
       
       t = max(0, min(1, ((h - x1) * (x2 - x1) + (k - y1) * (y2 - y1)) / segmentLength))
       projection_x = x1 + t * (x2 - x1)
       projection_y = y1 + t * (y2 - y1)

       distance = math.sqrt((h - projection_x)**2 + (k - projection_y)**2) - r

       if distance < r:
           return True
       else:
           return False
       
    def orderedLandmarks(landmarks): #landmarks = [[0x,0y], [1x,1y], [2x, 2y], etc.]
        if len(landmarks) <= 21:
            connectingPoints = [[0, 1, 2, 3, 4], [0, 5, 6, 7, 8], [9, 10, 11, 12,], [13, 14, 15, 16], [0, 17, 18, 19, 20], [2, 5, 9, 13, 17]] ##MODIFIED
        else:
            connectingPoints = [[0, 1, 2, 3, 4], [0, 5, 6, 7, 8], [9, 10, 11, 12,], [13, 14, 15, 16], [0, 17, 18, 19, 20], [2, 5, 9, 13, 17], [21, 22, 23, 24, 25], [21, 26, 27, 28, 29], [30, 31, 32, 33], [34, 35, 36, 37], [21, 38, 39, 40, 41], [23, 26, 30, 34, 38]] 
        orderedLandmarks = []
        
        # build 3d matrix = [[[0x, 0y], [1x, 1y]....], [[0x, 0y], [1x, 1y]...]]
        if len(landmarks) > 0:
            for group in connectingPoints:
                segment = []
                for value in group:
                    segment.append(landmarks[value])
                orderedLandmarks.append(segment)
        
        return orderedLandmarks
    
    def checkCollision(h, k, r, landmarks): #List return format: [Collision? 0 = false | 1 = true, Type? 0 = point | 1 = line, Index? [p1, p2] (if point only fill p1, leave p2 zero)]
        for lm in landmarks:
            if pow((lm[0] - h), 2) + pow((lm[1] - k), 2) >= pow(r, 2) / 1.3 and pow((lm[0] - h), 2) + pow((lm[1] - k), 2) <= pow(r, 2) * 1.3:
                return True

        for segment in calculateCollisions.orderedLandmarks(landmarks):
            for index, value in enumerate(segment):
                if index < len(segment) - 1:
                    if calculateCollisions.checkLine(h, k, r, value[0], value[1], segment[index + 1][0], segment[index + 1][1]):
                        return True
                    
        return False
    
    
