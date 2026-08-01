import cv2
from input.frame_source import FrameSource

class PhoneCamera(FrameSource):
    def __init__(self, url):
        self.cap = cv2.VideoCapture(url)

    # def get_frame(self, FrameSource):
    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            return frame

        return None

    def release(self):
        self.cap.release()