from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        return cls(floor(float_value)) if isinstance(float_value, float) else "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        int_value = 0

        for i in range(len(value)):
            if value[i] in roman_values:
                if i + 1 < len(value) and roman_values[value[i]] < roman_values[value[i + 1]]:
                    int_value -= roman_values[value[i]]
                else:
                    int_value += roman_values[value[i]]

        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        return cls(int(value)) if isinstance(value, str) else "wrong type"


# Test code

# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
