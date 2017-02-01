# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

# класс для последовательного применения списка знаний
class TDoProduct:
    # конструктор создает пустой список знаний, 
    # который в дальнейшем
    # наполняется последовательностью знаний
    def __init__(self):
        self.Products = list()

    # последовательно применить знания к множеству фактов Facts
    def Do(self, Facts):
        self.Facts = Facts
        for P in self.Products:
            P.Do(self.Facts)

# класс для реализации знания
class TProduct:
    def __init__(self, Symbol, Name):
        self.Symbol = Symbol # обозначение знания
        self.Name = Name     # описание знания

    # метод для реализации знания по фактам.
    # сейчас это абстрактный метод, 
    # который будет переопределен
    def Do(self, Facts):
        return True
                
