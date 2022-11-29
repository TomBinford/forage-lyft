from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def should_be_serviced(self):
        pass
