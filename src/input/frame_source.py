from abc import ABC, abstractmethod

class FrameSource(ABC):
    """
    Abstract base class for frame sources.
    """

    @abstractmethod
    def get_frame(self):
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