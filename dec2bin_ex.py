def dec2bin_ex(target):
    i = int(target)
    f = target - i

    a = []

    while i != 0:
        a.append(i % 2)
        i = i // 2
    
    a.reverse()

    b = []
    n = 0

    while (f != 0):
        temp = f * 2
        b.append(int(temp))
        f = temp - int(temp)
        n += 1
        if (n >= 10):
            break

    return a, b

print(dec2bin_ex(1.5))