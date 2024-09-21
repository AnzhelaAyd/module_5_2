class Hous:
    def __init__(self, name, number_of_floors):
        self.name=name
        self.number_of_floors= number_of_floors


    def go_to(self,new_floors):
        if (new_floors < 0) or (new_floors > self.number_of_floors) :
            print('такого этожа не существует ')
        else:
            for i in range(1, new_floors+1):
                  print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print("Название: ", self.name, 'кол-во этажей: ', self.number_of_floors)

h1 = Hous('ЖК Эльбрус', 10)
h2 = Hous('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))