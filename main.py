class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])#добавил через append список args.

        return object.__new__(cls)

    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'название: {self. name}, кол-во этажей: {self. number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self .number_of_floors == other .number_of_floors
        return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self .number_of_floors < other .number_of_floors
        return  NotImplemented
    def __le__(self, other):
        if isinstance(other,House):
            return self. number_of_floors <= other.number_of_floors
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, House):
            return self .number_of_floors >= other .number_of_floors
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, House):
            return self .number_of_floors >= other .number_of_floors
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, House):
            return self .number_of_floors != other .number_of_floors
        return True
    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented
    def __radd__(self, value):
        return  self.__add__(value)

    def __del__(self):
        print(self.name, "снесен, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)