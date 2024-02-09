words = input().split()
palindrome = input()
founded_palindromes = [current_palindrome for current_palindrome in words if current_palindrome == current_palindrome[::-1]]
palindrome_counter = words.count(palindrome)

print(founded_palindromes)
print(f"Found palindrome {palindrome_counter} times")
