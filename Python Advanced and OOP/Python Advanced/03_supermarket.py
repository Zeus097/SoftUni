from collections import deque


client_name = input()
client_deq = deque([])


while client_name != "End":
    if client_name == "Paid":
        while client_deq:
            print(client_deq.popleft())
    else:
        client_deq.append(client_name)
    client_name = input()

print(f"{len(client_deq)} people remaining.")
