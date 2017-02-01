# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import TLunar

import TFact

import TProduct

import TAIProducts

# Класс интеллектуального аппарата
class TAILunar(TLunar.TLunar):
    def __init__(self, low_height, force_f):
        super().__init__()
        self.low_height = low_height # параметр для отметки малой высоты
        self.force_f = force_f # параметр сильного торможения
        
    # Добавить систему знаний    
    def CollectProducts(self):
        self.DoProduct = TProduct.TDoProduct()
        self.DoProduct.Products.append(TAIProducts.TF1Product())
        self.DoProduct.Products.append(TAIProducts.TF2Product())
        self.DoProduct.Products.append(TAIProducts.TF3Product())
    
    # Выполнить все знания
    def DoProducts(self):
        self.DoProduct.Do(self.Facts)

    # Выработать управление торможением
    def Control(self):
        self.CollectFact() # собрать факты
        
        self.DoProducts() # применить знания
        
        # проверить наличие факта E
        if self.Facts.BoolFact("E"):
            self.SetF(self.force_f) # если да, то включить  
            return                  # сильное торможение

        # проверить наличие факта F
        if self.Facts.BoolFact("F"): 
            self.SetF(0) # если да, то выключить торможение
            return

        # проверить наличие факта G
        if self.Facts.BoolFact("G"):
            self.SetF(7) # если да, то включить обычное торможение
            return
        
        self.SetF(0) # если нет фактов, не включаем торможение
        
    # установить силу торможения
    def SetF(self, FF):
        self.F = FF

    # собрать факты
    def CollectFact(self):
        self.Facts = TFact.TFacts() # создать список фактов
        
        # определить факты из объективной информации
        if self.v > 0:
            self.Facts.F.append(TFact.TFact("A", \
            "Скорость положительная", TFact.TP(1)))
        
        if self.v <= 0:
            self.Facts.F.append(TFact.TFact("B", \
            "Скорость отрицательная", TFact.TP(1)))
            
        if self.v < -5:
            self.Facts.F.append(TFact.TFact("C", \
            "Скорость еще высокая", TFact.TP(1)))
            
        if self.H < self.low_height:
            self.Facts.F.append(TFact.TFact("D", \
            "Высота низкая", TFact.TP(1)))
