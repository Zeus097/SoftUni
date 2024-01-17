paper_rolls = int(input())
cloth_rolls = int(input())
glue_liters = float(input())
percent_discount = int(input())

paper_rolls *= 5.8
cloth_rolls *= 7.2
glue_liters *= 1.2
total_sum = paper_rolls + cloth_rolls + glue_liters
total_sum = total_sum - percent_discount / 100 * total_sum

print(f"{total_sum:.3f}")