pool_mass = int(input())
p1_pipe_quantity = int(input())
p2_pipe_quantity = int(input())
time_away = float(input())

needed_time_p1_pipe_quantity = p1_pipe_quantity * time_away
needed_time_p2_pipe_quantity = p2_pipe_quantity * time_away
total_sum = needed_time_p1_pipe_quantity + needed_time_p2_pipe_quantity

percent_p1_pipe = needed_time_p1_pipe_quantity / total_sum * 100
percent_p2_pipe = needed_time_p2_pipe_quantity / total_sum * 100
percent_pool_mass = total_sum / pool_mass * 100

if pool_mass >= total_sum:
    print(f"The pool is {percent_pool_mass:.2f}% full. Pipe 1: {percent_p1_pipe:.2f}%. Pipe 2: {percent_p2_pipe:.2f}%.")
else:
    extra_liters = abs(pool_mass - total_sum)
    print(f"For {time_away:.2f} hours the pool overflows with {extra_liters:.2f} liters.")