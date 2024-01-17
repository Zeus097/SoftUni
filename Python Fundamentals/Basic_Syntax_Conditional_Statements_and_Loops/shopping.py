budget = int(input())
total_budget = 0

while True:
     command = input()
     if command == "End":
          print("You bought everything needed.")
          break

     current_price = int(command)

     if total_budget + current_price > budget:
          print("You went in overdraft!")
          break

     total_budget += current_price
