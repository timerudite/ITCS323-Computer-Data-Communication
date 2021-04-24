import numpy as np


def one_dimesion(dataword, word_size, parity_type, array_size):
    # Base case
    if array_size >= 1:
        # print(len(dataword))
        #print("The original is {}".format(dataword))
        #print("Generated parity")
        for i in range(len(dataword)):
            # print(len(dataword[i]))
            if len(dataword[i]) == word_size:
                if parity_type == "one-dimensional-even":
                    count = dataword[i].count("1")
                    if count % 2 == 0:
                        #print(dataword[i] + "0")
                        dataword[i] = dataword[i] + "0"
                    elif count % 2 != 0:
                        #print(dataword[i] + "1")
                        dataword[i] = dataword[i] + "1"
                    # end if
                elif parity_type == "one-dimensional-odd":
                    count = dataword[i].count("1")
                    if count % 2 != 0:
                        #print(dataword[i] + "0")
                        dataword[i] = dataword[i] + "0"
                    elif count % 2 == 0:
                        #print(dataword[i] + "1")
                        dataword[i] = dataword[i] + "1"
                    # end if
                # end if
            elif len(dataword[i]) < word_size:
                extra = word_size - len(dataword[i])
                dataword[i] = dataword[i] + (extra*"0")
                if parity_type == "one-dimensional-even":
                    count = dataword[i].count("1")
                    if count % 2 == 0:
                        #print(dataword[i] + "0")
                        dataword[i] = dataword[i] + "0"
                    elif count % 2 != 0:
                        #print(dataword[i] + "1")
                        dataword[i] = dataword[i] + "1"
                    # end if
                elif parity_type == "one-dimensional-odd":
                    count = dataword[i].count("1")
                    if count % 2 != 0:
                        #print(dataword[i] + "0")
                        dataword[i] = dataword[i] + "0"
                    elif count % 2 == 0:
                        #print(dataword[i] + "1")
                        dataword[i] = dataword[i] + "1"
                    # end if
                # end if
            # end if
        # end for loop
        return dataword
    else:
        print("Error: you must enter array size more than 1")
# end function

# check number of one ion each column


def check_col(x, col):
    count = 0
    for i in range(len(x)):
        if(x[i][col] == "1"):
            count += 1
    return count

# even parity column


def check_two_even(y):
    for i in range(len(y)):
        if y[i] % 2 == 0:
            y[i] = 0
        elif y[i] % 2 != 0:
            y[i] = 1
    return y

# odd parity column


def check_two_odd(y):
    for i in range(len(y)):
        if y[i] % 2 == 0:
            y[i] = 1
        elif y[i] % 2 != 0:
            y[i] = 0
    return y


def two_dimesion(dataword, word_size, parity_type, array_size):
    # Base case
    if array_size >= 2:
        if parity_type == "two-dimensional-even":
            parity_type = "one-dimensional-even"
            # Check row
            new_dataword = one_dimesion(
                dataword, word_size, parity_type, array_size)
            x = new_dataword.copy()
            # print(x)

            y = []
            for i in range(word_size+1):
                y.insert(i, (check_col(x, i)))
            # print(y)

            check_two_even(y)

            for i in range(len(y)):
                y[i] = str(y[i])
            # print(y)

            add = ""
            for i in range(len(y)):
                add = add + y[i]

            # print(add)

            x.append(add)
            return (x)
        elif parity_type == "two-dimensional-odd":
            parity_type = "one-dimensional-odd"
            # Check row
            new_dataword = one_dimesion(
                dataword, word_size, parity_type, array_size)
            x = new_dataword.copy()
            # print(x)

            y = []
            for i in range(word_size+1):
                y.insert(i, (check_col(x, i)))
            # print(y)

            check_two_odd(y)

            for i in range(len(y)):
                y[i] = str(y[i])
            # print(y)

            add = ""
            for i in range(len(y)):
                add = add + y[i]

            # print(add)

            x.append(add)
            return (x)
    else:
        return ""

# The Generator


def parity_gen(dataword, word_size, parity_type, array_size):

    # Base case
    # Maximum size of each dataword (word_size) where word_size ≥ 5.
    if word_size < 5:
        print("Your word size is {}, please enter the value again")
    # end if

    # Check the parity type
    if parity_type == "one-dimensional-even":
        return one_dimesion(dataword, word_size, "one-dimensional-even", array_size)
    elif parity_type == "one-dimensional-odd":
        return one_dimesion(dataword, word_size, "one-dimensional-odd", array_size)
    elif parity_type == "two-dimensional-even":
        return two_dimesion(dataword, word_size, "two-dimensional-even", array_size)
    elif parity_type == "two-dimensional-odd":
        return two_dimesion(dataword, word_size, "two-dimensional-odd", array_size)
    # end if
# end function


def parity_check(codeword, parity_type, size):

    if parity_type == "one-dimensional-even":
        for i in range(len(codeword)):
            # print("1")
            if codeword[i].count("1") % 2 == 0:
                return 1
            elif codeword[i].count("1") % 2 != 0:
                return 0
    elif parity_type == "one-dimensional-odd":
        for i in range(len(codeword)):
            # print("1")
            if codeword[i].count("1") % 2 == 0:
                return 0
            elif codeword[i].count("1") % 2 != 0:
                return 1
    elif parity_type == "two-dimensional-even":
        for i in range(len(codeword)):
            # print("1")
            if codeword[i].count("1") % 2 == 0:
                return 1
            elif codeword[i].count("1") % 2 != 0:
                return 0
    elif parity_type == "two-dimensional-odd":
        for i in range(len(codeword)):
            # print("1")
            if codeword[i].count("1") % 2 == 0:
                return 0
            elif codeword[i].count("1") % 2 != 0:
                return 1
# end function


print("Testing feild\n\n")
print("These are the result\n")
print("For the validity: PASS=1 or FAIL=0 ")
print("One dimensional parity check\n")

print("One-dimensional-even")
print("[11101011], 8, one-dimensional-even, 1")
test_1 = parity_gen(["11101011"], 8, "one-dimensional-even", 1)
print(test_1)
print("Even validility: {}".format(
    parity_check(test_1, "one-dimensional-even", 1)))
print("Odd validility: {}".format(parity_check(test_1, "one-dimensional-odd", 1)))

print("\n")

print("[101010,101,100111], 6, one-dimensional-even, 3")
test_2 = parity_gen(["101010", "101", "100111"], 6, "one-dimensional-even", 3)
print(test_2)
print("Even validility: {}".format(
    parity_check(test_2, "one-dimensional-even", 3)))
print("Odd validility: {}".format(parity_check(test_2, "one-dimensional-odd", 3)))

print("\n")

print("One-dimensional-odd")
print("[11101011], 8, one-dimensional-odd, 1")
test_3 = parity_gen(["11101011"], 8, "one-dimensional-odd", 1)
print(test_3)
print("Even validility: {}".format(
    parity_check(test_3, "one-dimensional-even", 1)))
print("Odd validility: {}".format(parity_check(test_3, "one-dimensional-odd", 1)))

print("\n")

print("[101010,101,100111], 6, one-dimensional-odd, 3")
test_4 = parity_gen(["101010", "101", "100111"], 6, "one-dimensional-odd", 3)
print(test_4)
print("Even validility: {}".format(
    parity_check(test_4, "one-dimensional-even", 3)))
print("Odd validility: {}".format(parity_check(test_4, "one-dimensional-odd", 3)))

print("\n\n\n")

print("Two dimensional parity check\n")

print("Two-dimensional-even")
print("[101010,101,100111], 6, two-dimensional-even, 3")
test_5 = parity_gen(["101010", "101", "100111"], 6, "two-dimensional-even", 3)
print(test_5)
print("Even validility: {}".format(
    parity_check(test_5, "two-dimensional-even", 3)))
print("Odd validility: {}".format(parity_check(test_5, "two-dimensional-odd", 3)))

print("\n")


print("[101010,101,100111, 100], 6, two-dimensional-even, 4")
test_6 = parity_gen(["101010", "101", "100111", "100"],
                    6, "two-dimensional-even", 4)
print(test_6)
print("Even validility: {}".format(
    parity_check(test_6, "two-dimensional-even", 4)))
print("Odd validility: {}".format(parity_check(test_6, "two-dimensional-odd", 4)))


print("\n")

print("Two-dimensional-odd")
print("[101010,101,100111], 6, two-dimensional-odd, 3")
test_7 = parity_gen(["101010", "101", "100111"], 6, "two-dimensional-odd", 3)
print(test_7)
print("Even validility: {}".format(
    parity_check(test_7, "two-dimensional-even", 3)))
print("Odd validility: {}".format(parity_check(test_7, "two-dimensional-odd", 3)))

print("\n")

print("[101010,101,100111, 100], 6, two-dimensional-odd, 4")
test_8 = parity_gen(["101010", "101", "100111", "100"],
                    6, "two-dimensional-odd", 4)
print(test_8)
print("Even validility: {}".format(
    parity_check(test_8, "two-dimensional-even", 4)))
print("Odd validility: {}".format(parity_check(test_8, "two-dimensional-odd", 4)))
