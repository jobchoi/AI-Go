import cv2


class PhoneCamera:
    def __init__(self, url):
        self.cap = cv2.VideoCapture(url)

    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            return frame

        return None

    def release(self):
        self.cap.release()