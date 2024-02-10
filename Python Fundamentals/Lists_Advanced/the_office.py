def improve_happiness():
    employees_happiness = list(map(int, input().split()))
    happy_factor = int(input())

    improved_happiness = [employee * happy_factor for employee in employees_happiness]
    average_happiness = sum (improved_happiness) / len(improved_happiness)

    happy_count = sum(employee >= average_happiness for employee in improved_happiness)
    total_count = len(improved_happiness)

    message = "happy" if happy_count >= total_count / 2 else "not happy"
    result = f"Score: {happy_count}/{total_count}. Employees are {message}!"

    return result


result = improve_happiness()
print(result)
