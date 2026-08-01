from abc import ABC, abstractmethod
import numpy as np

class FrameSourceInter(ABC):
    """
    모든 입력장치의 공통 인터페이스
    """

    @abstractmethod
    def get_frame(self)->np.ndarray | None:
    
        """
        Frame 반환
        """
        pass    
    @abstractmethod
    def release(self):
        """
        자원해제
        """
        pass