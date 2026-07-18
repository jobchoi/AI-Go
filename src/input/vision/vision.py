import cv2

class VisionModule:
    """Vision Module MVP"""

    def process(self, frame):
        """
        현재는 Frame을 그대로 반환한다.
        이후 Board Detection 등이 이곳에 추가될 예정이다.
        """
        return frame