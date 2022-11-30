from typing import Tuple
from car import Car
from engine import *
from battery import *
from tires import *
from datetime import date


class CarFactory:
    class CarMissingTires:
        def __init__(self, battery: Battery, engine: Engine):
            self.battery = battery
            self.engine = engine

        def with_carrigan_tires(self, tire_wear: Tuple[float, float, float, float]):
            tires = CarriganTires(tire_wear)
            return Car(self.battery, self.engine, tires)

        def with_octoprime_tires(self, tire_wear: Tuple[float, float, float, float]):
            tires = OctoprimeTires(tire_wear)
            return Car(self.battery, self.engine, tires)

    @staticmethod
    def create_calliope(
        last_service_date: date,
        current_date: date,
        last_service_mileage: int,
        current_mileage: int,
    ):
        return CarFactory.CarMissingTires(
            SpindlerBattery(last_service_date, current_date),
            CapuletEngine(last_service_mileage, current_mileage),
        )

    @staticmethod
    def create_glissade(
        last_service_date: date,
        current_date: date,
        last_service_mileage: int,
        current_mileage: int,
    ):
        return CarFactory.CarMissingTires(
            SpindlerBattery(last_service_date, current_date),
            WilloughbyEngine(last_service_mileage, current_mileage),
        )

    @staticmethod
    def create_palindrome(
        last_service_date: date,
        current_date: date,
        warning_light_is_on: bool,
    ):
        return CarFactory.CarMissingTires(
            SpindlerBattery(last_service_date, current_date),
            SternmanEngine(warning_light_is_on),
        )

    @staticmethod
    def create_rorschach(
        last_service_date: date,
        current_date: date,
        last_service_mileage: int,
        current_mileage: int,
    ):
        return CarFactory.CarMissingTires(
            NubbinBattery(last_service_date, current_date),
            WilloughbyEngine(last_service_mileage, current_mileage),
        )

    @staticmethod
    def create_thovex(
        last_service_date: date,
        current_date: date,
        last_service_mileage: int,
        current_mileage: int,
    ):
        return CarFactory.CarMissingTires(
            NubbinBattery(last_service_date, current_date),
            CapuletEngine(last_service_mileage, current_mileage),
        )
