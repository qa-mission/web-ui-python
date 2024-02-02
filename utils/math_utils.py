from decimal import Decimal, ROUND_HALF_UP


class MathUtils:
    @staticmethod
    def round_double(value, places):
        if places < 0:
            raise ValueError("Decimal places must be non-negative")
        decimal_value = Decimal(str(value))
        rounded_value = decimal_value.quantize(Decimal('1e-{0}'.format(places)), rounding=ROUND_HALF_UP)
        return float(rounded_value)
