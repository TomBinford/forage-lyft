from battery import Battery
from engine import Engine
from tires import Tires


class Car:
    def __init__(self, battery: Battery, engine: Engine, tires: Tires):
        self.battery = battery
        self.engine = engine
        self.tires = tires

    def needs_service(self):
        return (
            self.battery.should_be_serviced()
            or self.engine.should_be_serviced()
            or self.tires.should_be_serviced()
        )
