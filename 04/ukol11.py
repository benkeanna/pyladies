n = 5
for j in range (n):
    for i in range(n):
        end = ' '
        if i == n-1:
            end = "\n"
        print('x',end=end)
