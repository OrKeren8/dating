from abc import ABC, abstractmethod

class AppController(ABC):

    @abstractmethod
    def open_web(self) -> None:
        raise NotImplemented
    
    @abstractmethod
    def swipe_right(self) -> None:
        raise NotImplemented
    
    @abstractmethod
    def check_notifications(self):
        raise NotImplemented
    
    @abstractmethod
    def click(self):
        raise NotImplemented

    @abstractmethod
    def decide(self):
        raise NotADirectoryError