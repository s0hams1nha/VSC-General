def naivematchstring(x, y):
    s = []
    for i in range(len(x) - len(y) + 1):
        j = 0
        while j < len(y) and x[i + j] == y[j]:
            j += 1
        if j == len(y):
            s.append(i)
    if len(s) == 0:
        return -1
    return s

x = input("Enter text: ")
y = input("Enter pattern: ")
print(naivematchstring(x, y))
