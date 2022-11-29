from car import Car
from engine import *
from battery import *
from datetime import date


class CarFactory:
    @staticmethod
    def create_calliope(
        last_service_date: date,
        current_date: date,
        last_service_mileage: int,
        current_mileage: int,
    ):
        return Car(
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
        return Car(
            SpindlerBattery(last_service_date, current_date),
            WilloughbyEngine(last_service_mileage, current_mileage),
        )

    @staticmethod
    def create_palindrome(
        last_service_date: date,
        current_date: date,
        warning_light_is_on: bool,
    ):
        return Car(
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
        return Car(
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
        return Car(
            NubbinBattery(last_service_date, current_date),
            CapuletEngine(last_service_mileage, current_mileage),
        )
