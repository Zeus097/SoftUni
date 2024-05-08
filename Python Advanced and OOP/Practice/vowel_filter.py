def vowel_filter(function):

    def wrapper():
        result = function()
        vowels = [char for char in result if char.lower() in 'aeouyi']
        return vowels
    return wrapper


# Test Code

# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())


# Output

# ["a", "e"]
