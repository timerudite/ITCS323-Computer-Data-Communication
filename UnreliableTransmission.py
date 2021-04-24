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
    print(y)
    return count
# end function


def tester(bit, p):
    infty = 100
    count = 0
    for i in range(infty):
        print("Round: {}".format(i+1))
        corrupt = unreliable_transmission(bit, p)
        count = count + corrupt
    # all number of corrupt / (number of bits * 100 time)
    ratio = count/(100*len(bit))
    print("Average ratio of erroneous bits and total number of bits for {}: ".format(p))
    return ratio
# end function


print("Output feild\n\n")
print("These are the result\n")
print(unreliable_transmission("10010001", 0.05))
print(unreliable_transmission("10010001", 0.1))
print(unreliable_transmission("10010001", 0.2))

print("Testing feild")
print("inframe = 10010001, p = 0.05\n")
print(tester("10010001", 0.05))

print("\n\n")

print("inframe = 10010001, p = 0.1\n")
print(tester("10010001", 0.1))

print("\n\n")

print("inframe = 10010001, p = 0.2\n")
print(tester("10010001", 0.2))
