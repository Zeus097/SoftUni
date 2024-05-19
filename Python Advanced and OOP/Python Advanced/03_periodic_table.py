n = int(input())
unique_chemical_elements = set()

for i in range(n):
    chemical_compound = input().split()
    for j in range(len(chemical_compound)):
        unique_chemical_elements.add(chemical_compound[j])

print(*unique_chemical_elements, sep='\n')
