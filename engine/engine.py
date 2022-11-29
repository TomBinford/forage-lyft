from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def should_be_serviced(self):
        pass
