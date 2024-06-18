def draw_figure(n):
    if n == 0:
        return
    print('*' * n)

    draw_figure(n - 1)
    print('#' * n)


num = int(input())
draw_figure(num)
