"""Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:

    name = "Petr"
    surname = "Sidorov"
    position = "Doctor"
    profit = 60000
    bonus = 20000
    _income = {"Оклад": profit,
               "Премия": bonus
               }
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_profit(self):
        self.total_profit = self.profit + self.bonus
        return ", Profit wiht bonus: {}".format(self.total_profit)


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.profit)

p = Position()
print("\n General information about the employee: ")
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w._income))