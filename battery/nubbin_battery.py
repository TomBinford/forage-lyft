from battery import Battery
from datetime import date, timedelta


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        pass

    def should_be_serviced(self):
        return self.current_date - self.last_service_date > timedelta(days=365 * 4)
