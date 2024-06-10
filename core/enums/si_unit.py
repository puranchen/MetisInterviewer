from enum import Enum

class SIUnit(Enum):
    MILLIMETER = "mm"
    CENTIMETER = "cm"
    METER = "m"
    KILOMETER = "km"
    GRAM = "g"
    KILOGRAM = "kg"
    SECOND = "s"
    MINUTE = "min"
    HOUR = "h"
    LITER = "L"
    MILLILITER = "mL"
    CELSIUS = "ºC"
    FAHRENHEIT = "F"

__all__ = ['SIUnit']