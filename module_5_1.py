class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        new = range(new_floor)
        if self.number_of_floors < new_floor:
            print("Ошибка")
        else:
            for i in new:
                print(i)
                if (i + 1) == new_floor:
                    print(new_floor)


jojo = House("ЖК Дыра", 20)
jojo.go_to(21)
