import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cam = cv2.VideoCapture(0)
mycoordinatedata = {}

while True:
    data,image = cam.read()
    image = cv2.flip(image,1)
    results = hands.process(image)
    height,width = image.shape[:2]
    if results.multi_hand_landmarks:
        for handid,hand_landmarks in enumerate(results.multi_hand_landmarks): #for hands
            
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            for id,lms in enumerate(hand_landmarks.landmark):
                x_cord = lms.x * width
                y_cord = lms.y * height
                mycoordinatedata[id] = (x_cord,y_cord)
                try:
                    if mycoordinatedata[8][1] < mycoordinatedata[5][1] and mycoordinatedata[12][1] < mycoordinatedata[9][1]:
                        print("Peace")
                    else:
                        print("War")
                except KeyError:
                    pass
            
            

    cv2.imshow("Project",image)
    cv2.waitKey(1)  

    
cam.release()
cv2.destroyAllWindows()


