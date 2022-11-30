from abc import ABC, abstractmethod


class Tires(ABC):
    @abstractmethod
    def should_be_serviced(self):
        pass
