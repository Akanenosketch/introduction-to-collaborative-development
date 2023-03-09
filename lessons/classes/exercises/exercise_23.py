class Car:
    def __init__(self, color, license_plate, vin_number):
        self.color = color
        self._license_plate = license_plate
        self.__vin_number = vin_number

    def get_vin_number(self):
        return self.__vin_number




my_Car = Car("red", "1234ABCD", 12340987)
ext_color = my_Car.color
ext_license_plate = my_Car._license_plate
ext_vin_number = my_Car.get_vin_number()
