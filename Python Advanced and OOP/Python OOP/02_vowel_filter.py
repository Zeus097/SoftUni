def vowel_filter(function):

    def wrapper():
        result = function()
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        available_vowels = []
        for vowel in vowels:
            if vowel in result:
                available_vowels.append(vowel)

        if available_vowels:
            return available_vowels

    return wrapper


# Test code

# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())
