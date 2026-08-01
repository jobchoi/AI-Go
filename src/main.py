import cv2

from input.phone_camera import PhoneCamera


url = "http://192.168.22.26:8080/video"

camera = PhoneCamera(url)
cv2.namedWindow('AI-Go Camera Test', cv2.WINDOW_NORMAL)
cv2.resizeWindow('AI-Go Camera Test', 800, 600)

while True:

    frame = camera.get_frame()

    if frame is None:
        print("frame 없음")
        continue

    print(frame.shape)

    cv2.imshow("AI-Go Camera Test", frame)
   
    if cv2.waitKey(1) == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()