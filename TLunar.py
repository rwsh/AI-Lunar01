# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:33:56 2017

@author: re
"""

# Класс спускаемого аппарата
class TLunar():
    # Передаем начальные условия
    def __init__(self, H = 1000., M = 100., g = 9.81):
        self.H = H # высота
        self.M = M # масса
        self.g = g # ускорение свободного падения
        self.v = 0.0 # скорость
        self.F = 0.0 # торможение
        
    # Расчет траектории аппарата за время dt=1
    def Run(self, dt = 1.):
        Fa = (-self.g + self.F) # ускорение с учетом торможения
        self.H = 0.5 * Fa * dt * dt + self.v * dt + self.H # высота
        self.v = Fa * dt + self.v # скорость

    # Печать состояния
    def Type(self):
        print(self.H.__str__()+"\t"+self.v.__str__()+"\t"+self.F.__str__())
        
    # Вычисление целевого функционала = модуль скорости
    def calc_quality(self):
        return abs(self.v)
        