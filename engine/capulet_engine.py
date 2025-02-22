from engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000
