class Transport:
    def init(self, marka, number , sped , load_capacity):
        self.marka = marka
        self.number = number
        self.speed = sped
        self.load_capacity = load_capacity

    def print_info(self):
        print(f'Марка: {self.marka} \nНомер: {self.number}\nСкорость: {self.speed}'
              f'\nГрузоподъемность: {self.get_load_capacity()}\n')

    def get_load_capacity(self):
        return self.load_capacity


class Car(Transport):
    def init(self, marka, number , sped , load_capacity):
        super().init(marka, number , sped , load_capacity)        # вызов конструктора родителя

    def print_info(self):
        print("АВТОМОБИЛЬ")
        print(f'Марка: {self.marka} \nНомер: {self.number}\nСкорость: {self.speed}'
              f'\nГрузоподъемность: {self.get_load_capacity()}\n')

    def get_load_capacity(self):
        return self.load_capacity

class Moto(Transport):
    def init(self, marka, number , sped , load_capacity, ballast=False):
        super().init(marka, number , sped , load_capacity)
        self.ballast = ballast

    def print_info(self):
        status = "есть" if self.ballast else "нет"
        print("МОТОЦИКЛ")
        print(f'Марка: {self.marka} \nНомер: {self.number}\nСкорость: {self.speed}'
              f'\nНаличие коляски: {status}\nГрузоподъемность: {self.get_load_capacity()}\n')

    def get_load_capacity(self):
        if self.ballast:
            return self.load_capacity
        else:
            return 0


class Truk(Transport):
    def init(self, marka, number , sped , load_capacity, ballast=False):
        super().init(marka, number, sped, load_capacity)
        self.ballast = ballast

    def print_info(self):
        status = "есть" if self.ballast else "нет"
        print("ГРУЗОВИК")
        print(f'Марка: {self.marka} \nНомер: {self.number}\nСкорость: {self.speed}'
              f'\nНаличие прицепа: {status}\nГрузоподъемность: {self.get_load_capacity()}\n')

    def get_load_capacity(self):
        if self.ballast:
            return self.load_capacity * 2
        else:
            return self.load_capacity


car = Car("BMW", "Q123WE77", 300, 12000)
car.print_info()

moto = Moto("Motoland", "A234SD16", 200, 150)
moto.print_info()
moto_b = Moto("Kawasaki", 'Z345XC32', 250, 250, True)
moto_b.print_info()

truck = Truk("Sollers Argo", 'F456HU118', 180, 10000)
truck.print_info()
truck_b = Truk('КамАЗ-54901', 'U765IR116', 300, 3000000, True)
truck_b.print_info()











