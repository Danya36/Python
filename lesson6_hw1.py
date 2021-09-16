"""Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод."""

import time

class TrafficLight:

    __traffic_light_color = "Traffic signal"

    def running(self):
        while True:
            print("Red light")
            time.sleep(7)
            print("Yellow light")
            time.sleep(2)
            print("Green light")
            time.sleep(7)


TrafficLight = TrafficLight()
TrafficLight.running()