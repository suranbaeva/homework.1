class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры и Сеттеры
    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    # Метод make_computations
    def make_computations(self):
        result = self.__cpu * self.__memory
        return f"Результат вычислений с cpu={self.__cpu} и memory={self.__memory}: {result}"

    # Магический метод __str__
    def __str__(self):
        return f"Computer [CPU: {self.__cpu}, Memory: {self.__memory}]"

    # Магические методы для сравнения (сравнение по атрибуту memory)
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттеры и Сеттеры
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Метод call
    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print(f"Ошибка: сим-карта номер {sim_card_number} не найдена")

    # Магический метод __str__
    def __str__(self):
        return f"Phone [SIM Cards: {', '.join(self.__sim_cards_list)}]"
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод use_gps
    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    # Переопределение метода __str__
    def __str__(self):
        return f"SmartPhone [CPU: {self.get_cpu()}, Memory: {self.get_memory()}, SIM Cards: {', '.join(self.get_sim_cards_list())}]"
# Создание объектов
computer = Computer(cpu=3.5, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MTS", "Megafon"])
smartphone1 = SmartPhone(cpu=2.8, memory=64, sim_cards_list=["Beeline", "MTS"])
smartphone2 = SmartPhone(cpu=2.0, memory=128, sim_cards_list=["Megafon"])

# Распечатка информации
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Тестирование методов
print(computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Алматы")

# Пример сравнения
print(computer > smartphone1)
print(smartphone1 == smartphone2)
