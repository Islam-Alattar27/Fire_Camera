import cv2 as c
import playsound as s

fire_classifier = c.CascadeClassifier('Algorithm.xml')
cap = c.VideoCapture(0)
sound_file = 'Abo_Araby.mp3'

while True:
    _, frame = cap.read()
    gray = c.cvtColor(frame, c.COLOR_BGR2GRAY)
    c.imshow("Fire Detection", frame)
    fire = fire_classifier.detectMultiScale(gray, 1.2, 55)  

    for (x, y, w, h) in fire:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        print("Found fire ya Islam")
        s.playsound(sound_file)

    if c.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
c.destroyAllWindows()