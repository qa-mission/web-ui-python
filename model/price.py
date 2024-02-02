from enum import Enum
import decimal
from decimal import Decimal


class Unit(Enum):
    EA = "EA"
    KG = "KG"
    LB = "LB"
    HNDML = "HNDML"
    ONEML = "ONEML"
    PKG = "PKG"
    ZEROGR = "ZEROGR"
    HNDGR = "HNDGR"
    ONEGR = "ONEGR"

class Price:
    KG_TO_LB = 2.20462

    def __init__(self, value: float, unit: Unit, type: str = ""):
        self.value = value
        self.type = type
        self.unit = unit

        if unit == Unit.HNDGR:
            self.value = 10 * value
            self.unit = Unit.KG
        elif unit == Unit.ONEGR:
            self.value = 1000 * value
            self.unit = Unit.KG
        elif unit == Unit.ZEROGR:
            self.value = 0.0
            self.unit = Unit.ZEROGR

    def get_type(self) -> str:
        return self.type

    def get_unit(self) -> Unit:
        return self.unit

    def get_value(self) -> float:
        return round(self.value, 2)

    def get_value_as_string(self) -> str:
        return "{:.2f}".format(self.value)

    def get_price_per(self, unit: Unit) -> float:
        if (self.unit == Unit.EA) and (unit == Unit.EA):
            return self.value
        elif (self.unit == Unit.EA) and (unit != Unit.EA):
            raise RuntimeError("Unable to convert price per unit into price per Kg or Lb")
        elif (self.unit == Unit.KG) and (unit == Unit.KG):
            return round(self.value, 2)
        elif (self.unit == Unit.KG) and (unit == Unit.LB):
            return round(self.value / self.KG_TO_LB, 2)
        elif (self.unit == Unit.KG) and (unit == Unit.HNDML):
            raise RuntimeError("Unable to convert Kg into mL")
        elif (self.unit == Unit.LB) and (unit == Unit.LB):
            return round(self.value, 2)
        elif (self.unit == Unit.LB) and (unit == Unit.KG):
            return round(self.value * self.KG_TO_LB, 2)
        elif (self.unit == Unit.LB) and (unit == Unit.HNDML):
            raise RuntimeError("Unable to convert LB into mL")
        elif (self.unit == Unit.HNDML) and (unit == Unit.HNDML):
            return round(self.value, 2)
        elif (self.unit == Unit.HNDML) and (unit == Unit.ONEML):
            return round(self.value / 100, 2)
        elif (self.unit == Unit.ONEML) and (unit == Unit.ONEML):
            return round(self.value, 2)
        elif (self.unit == Unit.ONEML) and (unit == Unit.HNDML):
            return round(self.value * 100, 2)
        elif (self.unit == Unit.PKG) and (unit == Unit.PKG):
            return round(self.value, 2)
        else:
            raise RuntimeError(f"Unable to convert {self.unit} into {unit}")

    def __lt__(self, other: "Price") -> bool:
        return self.get_value() < other.get_value()

    def __eq__(self, other: "Price") -> bool:
        return self.value == other.value
