n_length, m_length = list(map(int, input().split()))

n_set = set()
m_set = set()

for _ in range(n_length):
    n_set.add(int(input()))

for _ in range(m_length):
    m_set.add(int(input()))

print(*(n_set & m_set), sep='\n')
