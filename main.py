import cv2
import mediapipe as mp
import random
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)
mycoordinatedata = {}
myfingers = []
userinput = ""
computerchoices = ["Scissor","Paper","Rock"]
computerinput = random.choice(computerchoices)
currenttime = time.time()
counter = 0
result = ""
while True:
    data,image = cap.read()
    image = cv2.flip(image,1)
    results = hands.process(image)
    height,width = image.shape[:2]
    checktime = time.time()
    if results.multi_hand_landmarks:
        for handid,hand_landmarks in enumerate(results.multi_hand_landmarks): #for hands
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            for id,lms in enumerate(hand_landmarks.landmark): #each landmark inside hand
                x_cord = lms.x * width
                y_cord = lms.y * height
                mycoordinatedata[id] = (x_cord,y_cord)
                try:
                    # print(mycoordinatedata[4][0]<mycoordinatedata[1][0])
                    if mycoordinatedata[8][1] < mycoordinatedata[5][1] and mycoordinatedata[12][1] < mycoordinatedata[9][1] and mycoordinatedata[16][1] > mycoordinatedata[13][1] and mycoordinatedata[20][1] > mycoordinatedata[17][1] and mycoordinatedata[4][0]<mycoordinatedata[1][0]:
                        userinput = "Scissor"
                        cv2.putText(image,userinput,(200,200),cv2.FONT_HERSHEY_COMPLEX,7,(255,255,255),4,cv2.LINE_AA)
                    if mycoordinatedata[8][1] < mycoordinatedata[5][1] and mycoordinatedata[12][1] < mycoordinatedata[9][1] and mycoordinatedata[16][1] < mycoordinatedata[13][1] and mycoordinatedata[20][1] < mycoordinatedata[17][1] and mycoordinatedata[4][0]>mycoordinatedata[1][0]:
                        userinput = "Paper"
                        cv2.putText(image,userinput,(200,200),cv2.FONT_HERSHEY_COMPLEX,7,(255,255,255),4,cv2.LINE_AA)
                    if mycoordinatedata[8][1] > mycoordinatedata[5][1] and mycoordinatedata[12][1] > mycoordinatedata[9][1] and mycoordinatedata[16][1] > mycoordinatedata[13][1] and mycoordinatedata[20][1] > mycoordinatedata[17][1] and mycoordinatedata[4][0]<mycoordinatedata[1][0]: #hahahaha 
                        userinput = "Rock"
                        cv2.putText(image,userinput,(200,200),cv2.FONT_HERSHEY_COMPLEX,7,(255,255,255),4,cv2.LINE_AA)
                    
                except KeyError:
                    pass
        if checktime - currenttime >= 1:
            print(5-counter)
            currenttime = time.time()
            
            counter+=1
            if counter == 5:
                print(f"Computer: {computerinput}\nUser: {userinput}")
                counter = 0
                computeroldchoice = computerinput
                if userinput == "Scissor" and computerinput == "Paper":
                    result = "You Win"
                elif userinput == "Paper" and computerinput == "Rock":
                    result = "You Win"
                elif userinput == "Rock" and computerinput == "Paper":
                    result = "You Win"
                elif userinput == computerinput:
                    result = "Draw"
                else:
                    result = "Computer Wins"
                computerinput = random.choice(computerchoices)
    cv2.putText(image,result,(500,1000),cv2.FONT_HERSHEY_COMPLEX,5,(255,105,97),4,cv2.LINE_AA)
    cv2.putText(image,str(5-counter),(1500,200),cv2.FONT_HERSHEY_COMPLEX,5,(255,105,97),4,cv2.LINE_AA)
    cv2.imshow("Project",image)
    cv2.waitKey(1)  

    
cap.release()
cv2.destroyAllWindows()