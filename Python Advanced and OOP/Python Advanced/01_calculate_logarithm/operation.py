from logic import calculate_logarithm

n = int(input())
base_input = input()

result = calculate_logarithm(n, base_input)
print(f"{result:.2f}")
