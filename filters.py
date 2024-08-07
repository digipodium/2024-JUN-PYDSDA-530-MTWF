import cv2

path =r"C:\Users\ZAID\Videos\Captures\THE FINALS   2023-12-08 21-18-30.mp4"
video = cv2.VideoCapture(path)

while True:
    state, frame = video.read()
    if not state: break
    frame = cv2.resize(frame, (0,0), fx=.5, fy=.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)

    # stacking frame
    s1 = cv2.hconcat([frame, cv2.merge([gray, gray, gray])])
    s2 = cv2.hconcat([rgb, hsv])
    f = cv2.vconcat([s1, s2])
    h, w, _ = f.shape
    # adding text
    f = cv2.putText(f, "Orignal", (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),5)
    f = cv2.putText(f, "Grayscale", (w//2 + 50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255),5)
    f = cv2.putText(f, "RGB", (50, h//2+100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),5)
    f = cv2.putText(f, "HSV", (w//2 + 50, h//2 + 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),5)
    
    cv2.imshow('frame', f)

    if cv2.waitKey(10) == ord('q'):
        break