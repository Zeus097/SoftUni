def multiply(times):

    def decorator(function):

        def wrapper(*args):
            result = function(*args)
            return result * times

        return wrapper

    return decorator


# # Test code (Output 39)
#
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
#
# print(add_ten(3))


# # Test code (Output 80)
#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
#
# print(add_ten(6))
