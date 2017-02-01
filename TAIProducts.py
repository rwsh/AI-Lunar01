# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import TProduct

import TFact

# Определяем класс-наследник знания
class TF1Product(TProduct.TProduct):
    def __init__(self):
        super().__init__("F1", "Нужно включить большое торможение")

    # Реализация знания        
    def Do(self, Facts):
        if Facts.BoolFact("C") and Facts.BoolFact("D"):
            Facts.F.append(TFact.TFact("E", \
            "Нужно резко увеличить торможение", TFact.TP(1)))
            

# определяем класс-наследник знания
class TF2Product(TProduct.TProduct):
    def __init__(self):
        super().__init__("F2", "Нужно отключить торможение")
    
    # Реализация знания        
    def Do(self, Facts):
        if Facts.BoolFact("A"):
            Facts.F.append(TFact.TFact("F", \
            "Нужно отключить торможение", TFact.TP(1)))
            
# определяем класс-наследник знания
class TF3Product(TProduct.TProduct):
    def __init__(self):
        super().__init__("F3", "Нужно включить торможение")
    
    # Реализация знания        
    def Do(self, Facts):
        if Facts.BoolFact("B"):
            Facts.F.append(TFact.TFact("G", \
            "Нужно включить торможение", TFact.TP(1)))
            