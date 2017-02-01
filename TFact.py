# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

# класс для хранения фактов
class TFacts:
    def __init__(self):
        # список фактов
        self.F = list()
    
# проверить есть ли факт с заданным символом, если есть,
# то вернуть ссылку на класс с описанием этого факта        
    def IsFact(self, Symbol):
        for f in self.F:
            if f.Symbol == Symbol:
                return f
        return None

# проверить, есть ли истинное значение факта с заданным символом        
    def BoolFact(self, Symbol):
        Fact = self.IsFact(Symbol)
        if Fact is None:
            return False
        else:
            return Fact.getbool()

# класс для описания факта
# Symbol - обозначение факта, уникальный идентификатор
# Name - описание факта
# p - класс TP для хранения значения факта
class TFact:
    def __init__(self, Symbol, Name, p):
        self.Symbol = Symbol 
        self.Name = Name
        self.p = p

# установить четкое значение факта        
    def setbool(self, p):
        self.p.setbool(p)

# получить четкое значение факта        
    def getbool(self):
        return self.p.getbool()

# класс для описания вероятностного знания
# p = -1 означает ложное высказывания
# p = 1  означает истинное высказывание
# p = 0  означает полную неопределенность
# p - означает вероятность высказывания
class TP:
    def __init__(self, p):
        self.p = p
        
# установить четкое значение по булевой переменной b
    def setbool(self, b):
        if b:
            self.p = 1
        else:
            self.p = -1
    
# получить четкое значение в булеву переменную            
    def getbool(self):
        if self.p > 0:
            return True
        else:
            return False
        
            