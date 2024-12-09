class Frame:
    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.related_frames = {}

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def add_related_frame(self, key, frame):
        self.related_frames[key] = frame

    def display(self):
        output = f"Фрейм: {self.name}\n"
        print(f"Фрейм: {self.name}")
        output += "Атрибуты:\n"
        print("Атрибуты:")
        for key, value in self.attributes.items():
            output += f"  - {key}: {value}\n"
            print(f"  - {key}: {value}")
        for key, frame in self.related_frames.items():
            output += f"  - Связанный фрейм: {key}\n"
            print(f"  - Связанный фрейм: {key}")
            frame.display()
        return output


def build_initial_frames():
    # Создаем фрейм для поезда
    train_frame = Frame("Поезд")
    train_frame.add_attribute("Номер поезда", "123А")
    train_frame.add_attribute("Тип", "Пассажирский")
    train_frame.add_attribute("Маршрут", "Москва - Санкт-Петербург")
    train_frame.add_attribute("Время отправления", "10:00")
    train_frame.add_attribute("Время прибытия", "14:30")
    train_frame.add_attribute("Количество вагонов", 10)

    # Создаем фрейм для состава
    composition_frame = Frame("Состав")
    composition_frame.add_related_frame("Вагон 1", Frame("Вагон 1"))
    composition_frame.related_frames["Вагон 1"].add_attribute("Тип", "Плацкарт")
    composition_frame.related_frames["Вагон 1"].add_attribute("Вместимость", 54)

    composition_frame.add_related_frame("Вагон 2", Frame("Вагон 2"))
    composition_frame.related_frames["Вагон 2"].add_attribute("Тип", "Купе")
    composition_frame.related_frames["Вагон 2"].add_attribute("Вместимость", 36)

    composition_frame.add_related_frame("Вагон 3", Frame("Вагон 3"))
    composition_frame.related_frames["Вагон 3"].add_attribute("Тип", "СВ")
    composition_frame.related_frames["Вагон 3"].add_attribute("Вместимость", 18)

    # Создаем фрейм для персонала
    staff_frame = Frame("Персонал")
    staff_frame.add_related_frame("Машинист", Frame("Машинист"))
    staff_frame.related_frames["Машинист"].add_attribute("Имя", "Сергей")
    staff_frame.related_frames["Машинист"].add_attribute("Стаж", "15 лет")

    staff_frame.add_related_frame("Проводник", Frame("Проводник"))
    staff_frame.related_frames["Проводник"].add_attribute("Имя", "Анна")
    staff_frame.related_frames["Проводник"].add_attribute("Стаж", "5 лет")

    # Связываем состав и персонал с фреймом поезда
    train_frame.add_related_frame("Персонал", staff_frame)
    train_frame.add_related_frame("Состав", composition_frame)


    # Отображаем информацию о фрейме поезда
    train_frame.display()
    return train_frame
    