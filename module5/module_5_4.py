
class House :

    houses_history = []

    def __new__(cls, *args, **kwargs):
        houses_history = super().__new__(cls)
        for i in args:
                if i not in cls.houses_history:
                    cls.houses_history.append(i)
                return houses_history

    def __del__(self):
        print(f"Название: {self.name} снесён, но он останется в истории")




    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __len__(self):
           return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self,new_floor):
        if new_floor < 1 or new_floor  > self.number_of_floors:
            print("Такого этажа не существует")

        else:
            for i in range(1,new_floor + 1 ):
                print(i)



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
