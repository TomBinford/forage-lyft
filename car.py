from battery import Battery
from engine import Engine


class Car:
    def __init__(self, battery: Battery, engine: Engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.should_be_serviced() or self.engine.should_be_serviced()
