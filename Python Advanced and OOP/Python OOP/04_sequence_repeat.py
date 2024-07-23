class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            i = self.i % len(self.sequence)
            self.i += 1
            return self.sequence[i]
        raise StopIteration


# # test zero
# import unittest
#
# class Tests(unittest.TestCase):
#     def test_zero(self):
#         result = list(sequence_repeat('abc', 5))
#         self.assertEqual(result, ['a', 'b', 'c', 'a', 'b'])
#
# if __name__ == '__main__':
#     unittest.main()
