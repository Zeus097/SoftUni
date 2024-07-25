# import unittest


def tags(n):
    def decorator(func):
        def wrapper(*args):
            return f"<{n}>{func(*args)}</{n}>"

        return wrapper
    return decorator


# # Test code // Result:<p>Hello you!</p>
#
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
#
#
# print(join_strings("Hello", " you!"))


# # Tests
# test second zero
#
# class TagsTests(unittest.TestCase):
#     def test_zero_second(self):
#         @tags('h1')
#         def to_upper(text):
#             return text.upper()
#         self.assertEqual(to_upper('hello'), '<h1>HELLO</h1>')
#
#
# if __name__ == '__main__':
#     unittest.main()
