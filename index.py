# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:28:12 2017

@author: Roman Shamin
"""

import matplotlib.pyplot as plt

import TAIlunar

# Запускаем аппарат со следующими параметрами
# низкая высота = 200, сильное торможение = 20
Lunar = TAIlunar.TAILunar(200, 20)

# Подготовить знания
Lunar.CollectProducts()

"""
Версия без поиска оптимального управления

hh = list()
vv = list()

# Продолжать пока высота положительная
while Lunar.H > 0:
    Lunar.Control() # выбрать управление
    Lunar.Run()     # изменить положение аппарата
    Lunar.Type()    # напечатать состояние
    hh.append(Lunar.H)
    vv.append(Lunar.v)

plt.figure(1)
plt.plot(hh)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Height")
plt.axis(ymin = 0, ymax = 1050, xmax = 28)
plt.savefig("lunar_h.eps")

plt.figure(2)
plt.plot(vv)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("velocity")
plt.axis(xmax = 28)
plt.savefig("lunar_v.eps")

"""

"""
Далее версия с поиском оптимального управления
"""

# Функция для вычисления градиента целевого функционала
def calc_grad(l, f, delta_l, delta_f):
    lunar0 = calc_lunar(l, f) # вычислить значение в точке
    
    # вернуть конечную разность по двум переменным
    return [(calc_lunar(l + delta_l, f)-lunar0)/delta_l, \
            (calc_lunar(l, f + delta_f)-lunar0)/delta_f]

# Функция для вычисления целевого функционала
def calc_lunar(low, force):
    Lunar = TAIlunar.TAILunar(low, force)
    Lunar.CollectProducts()
    T = 0
    while Lunar.H > 0 and T < 10000:
        Lunar.Control()
        Lunar.Run()
        T = T + 1
    return Lunar.calc_quality()
    
# Процедура обучения

low_height = 100 # устанавливаем начальные приближения
force_f = 20

delta_h = 10 # обучающие параметры
delta_f = 1

optimal_j = list() # для сохранения текущих значений

# В начале укажем нулевое значение, как текущее оптимальное

min_j = calc_lunar(low_height, force_f)
optimal_j.append(min_j)


optimal = [0, 0] # переменные для оптимальных значений 

# Повторять обучение 100 раз
for n in range(100):
    # Вычислить градиент
    grad = calc_grad(low_height, force_f, delta_h, delta_f)
    
    # обучить параметрам
    low_height = low_height - delta_h * grad[0]
    force_f = force_f - delta_f * grad[1]

    # Вычислить новое значение функционала
    lunar_j = calc_lunar(low_height, force_f)

    # Сохранить текущее значение    
    optimal_j.append(lunar_j)

    # Если найденное решение лучше, то сохранить ее
    if lunar_j < min_j:
        min_j = lunar_j
        optimal[0] = low_height
        optimal[1] = force_f

# Напечатать оптимальные параметры
print(optimal[0].__str__() + "\t" + optimal[1].__str__())
print(calc_lunar(optimal[0], optimal[1]).__str__())
    
plt.figure(3)
plt.plot(optimal_j)
plt.grid(True)
plt.xlabel("Step")
plt.ylabel("J")
#plt.axis(xmax = 28)
plt.savefig("lunar_j.eps")


