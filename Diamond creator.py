N = 44

for i in range(N):
    for j in range(N-1, i, -1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()
for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print('')
    