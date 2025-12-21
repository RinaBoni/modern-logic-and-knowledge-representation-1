class Owner:
    def __init__(self, name, age):
        self.name = name  # Имя владельца
        self.age = age    # Возраст владельца
        self.dogs = []    # Список собак владельца

    def add_dog(self, dog):
        self.dogs.append(dog)  # Добавляем собаку в список

    def display_info(self):
        print(f"Владелец: {self.name}, Возраст: {self.age} лет")
        print("Собаки:")
        for dog in self.dogs:
            dog.display_info()

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed  # Порода
        self.age = age      # Возраст
        self.color = color  # Цвет

    def display_info(self):
        print(f"  Порода: {self.breed}, Возраст: {self.age} лет, Цвет: {self.color}")

# Создаем владельцев
owner1 = Owner("Алексей", 30)
owner2 = Owner("Мария", 25)

# Создаем собак и добавляем их владельцам
dog1 = Dog("Лабрадор", 3, "Черный")
dog2 = Dog("Бульдог", 5, "Белый")
dog3 = Dog("Пудель", 2, "Коричневый")

owner1.add_dog(dog1)
owner1.add_dog(dog3)
owner2.add_dog(dog2)

# Отображаем информацию о владельцах и их собаках
owner1.display_info()
print("-" * 20)
owner2.display_info()