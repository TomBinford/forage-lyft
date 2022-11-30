from typing import Tuple
from tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear: Tuple[float, float, float, float]):
        self.tire_wear = tire_wear

    def should_be_serviced(self):
        return any(wear >= 0.9 for wear in self.tire_wear)
