import random


def unreliable_transmission(bit, p):
    x = [0]*len(bit)
    y = ["0"]*len(bit)

    for i in range(len(x)):
        x[i] = random.random()
    # print(x)

    count = 0
    for j in range(len(x)):
        if x[j] < 0.5:
            if bit[j] == "0":
                y[j] = "1"
            elif bit[j] == "1":
                y[j] = "0"
            # end if
            count += 1
        # end if
    # print(y)
    return count


print(unreliable_transmission("10010001", 0.05))
print(unreliable_transmission("10010001", 0.1))
print(unreliable_transmission("10010001", 0.2))


def tester(bit, p):
    infty = 100
    count = 0
    for i in range(infty):
        corrupt = unreliable_transmission(bit, p)
        count = count + corrupt
    # all number of corrupt / (number of bits * 100 time)
    ratio = count/(100*len(bit))
    return ratio


print(tester("10010001", 0.05))
print(tester("10010001", 0.1))
print(tester("10010001", 0.2))
