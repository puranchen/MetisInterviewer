from enums import SIUnit
from typing import Union

class BodyTemperature:
    def __init__(self, temperature: float, unit: Union[SIUnit.CELSIUS, SIUnit.FAHRENHEIT] = SIUnit.CELSIUS):
        self.temperature = temperature
        self.unit = unit

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if isinstance(value, (int, float)):
            self._temperature = float(value)
        else:
            raise ValueError(f"Invalid value for temperature: {value!r}")
        
    @property
    def unit(self):
        return self.unit
    
    @unit.setter
    def unit(self, value):
        if value is not None:
            if isinstance(value, str) and value.upper() in ["CELSIUS", "FAHRENHEIT"]:
                self._unit = SIUnit[value.upper()]
            elif value in [SIUnit.CELSIUS, SIUnit.FAHRENHEIT]:
                self._unit = value
            else:
                raise ValueError(f"Invalid unit: {value}")
        else:
            raise ValueError(f"Invalid unit: {value}")
        
    def __repr__(self):
        return f"BodyTemperature(temperature={self._temperature}{self._unit.value})"
    
__all__ = ['BodyTemperature']