import cv2 as cv 

capturar_video = cv.VideoCapture(1)
if not capturar_video.isOpened():
    print("No Camaras found")
    exit()
while True: 
    tipocamara, camara = capturar_video.read()
    grises = cv.cvtColor(camara,cv.COLOR_BGR2GRAY,)
    #cv.imshow("En vivo", camara)
    cv.imshow("En vivo grises", grises)
    if cv.waitKey(1) == ord("q"):
        break
capturar_video.release()
cv.destroyAllWindows()