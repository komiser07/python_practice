import datetime


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    @classmethod
    def from_vin(cls, vin):
        manufacturer_code = vin[:3]

        years = ['2019', '2020', '2021']
        makes = ['Toyota', 'Honda', 'Ford']
        models = ['Corolla', 'Civic', 'Focus']

        if manufacturer_code == 'AAA':
            make = 'Toyota'
            model = 'Prius'
            year = '2019'
        elif manufacturer_code == 'BBB':
            make = 'Honda'
            model = 'Civic'
            year = '2020'
        elif manufacturer_code == 'CCC':
            make = 'Ford'
            model = 'Focus'
            year = '2021'
        else:
            print(f"Неверный VIN: {manufacturer_code}")

        return cls(make, model, year)

    @staticmethod
    def is_valid_year(year):
        current_year = datetime.datetime.now().year
        min_year = 1886
        max_year = current_year
        return min_year <= int(year) <= max_year


toyota = Car.from_vin('BBB123456789012345')
print(toyota.get_info())
print(Car.is_valid_year('2026'))
