from abc import ABC, abstractmethod

@property
@abstractmethod
def name(self):
    pass

class Figure(ABC):
    @abstractmethod
    def S(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass