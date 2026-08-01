import cv2
import numpy as np  
from input.frame_source import FrameSourceInter

class PhoneCamera(FrameSourceInter):
    def __init__(self, url):
        if url is None:
            raise ValueError("URL이 None입니다. 유효한 URL을 입력해주세요.")
        self.cap = cv2.VideoCapture(url)

    def get_frame(self)->np.ndarray | None:
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("프레임을 가져오지 못했습니다. URL 주소나 네트워크 연결을 다시 확인해 주세요.")  

        for _ in range(5):
            ret, frame = self.cap.read()

            if ret:
                return frame

        return None

    def release(self) -> None:
        self.cap.release()