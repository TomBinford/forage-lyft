from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def should_be_serviced(self):
        return self.warning_light_is_on
