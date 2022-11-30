from typing import Tuple
from tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear: Tuple[float, float, float, float]):
        self.tire_wear = tire_wear

    def should_be_serviced(self):
        return sum(self.tire_wear) >= 3
