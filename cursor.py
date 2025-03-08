import cv2
import mediapipe as m
import pyautogui
cap=cv2.VideoCapture(0)
hand_detector=m.solutions.hands.Hands()
drawing_utils=m.solutions.drawing_utils
s_w,s_h=pyautogui.size()
index_y=0
while True:
    _,f=cap.read()
    f=cv2.flip(f,1)
    f_h,f_w,_=f.shape
    r=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    o=hand_detector.process(r)
    h=o.multi_hand_landmarks
    if h:
        for hand in h:
            drawing_utils.draw_landmarks(f,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*f_w)
                y=int(landmark.y*f_h)
                
                if id == 4:
                    cv2.circle(img=f, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x=s_w/f_w*x
                    index_y=s_h/f_h*y
                    pyautogui.moveTo(index_x,index_y)
                if id== 8:
                    cv2.circle(img=f, center=(x,y), radius=10, color=(0, 255, 255))
                    th_x=s_w/f_w*x
                    th_y=s_h/f_h*y
                    print('outside',abs(index_y - th_y))
                    if abs(index_y - th_y) < 12:
                        pyautogui.click()
                        pyautogui.sleep(1)
                if id== 12:
                    cv2.circle(img=f, center=(x,y), radius=10, color=(0, 255, 255))
                    h1_x=s_w/f_w*x
                    h2_y=s_h/f_h*y
                if id== 17:
                    cv2.circle(img=f, center=(x,y), radius=10, color=(0, 255, 255))
                    t1_x=s_w/f_w*x
                    t2_y=s_h/f_h*y
                    print('outside',abs(h2_y - t2_y))
                    if abs(h2_y - t2_y) < 12:
                        pyautogui.doubleClick()
                        pyautogui.sleep(1)
                        
    cv2.imshow("v m",f)
    cv2.waitKey(1)