from decimal import Decimal

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RangeValidator:
    def __init__(self, min_value: int | Decimal, max_value: int | Decimal, message: str=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    def __call__(self, value: int | Decimal):
        if not (self.min_value <= value <= self.max_value):
            raise ValidationError(self.message)

