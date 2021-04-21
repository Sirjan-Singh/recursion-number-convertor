def number_word1converter(x):
    number = f"{x}"

    y = len(number)

    # LISTS

    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    teenline = ["ten", "eleven", "twelwe", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                "nineteen"]

    tenline = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    symbols = [" Thousand ", " Million ", " Billion ", " Trillion "]
    if y > 0:
        digit1 = digits[int(number[-1])]
        if int(number[-1]) > 0:
            digit2 = digit1
        else:
            digit2 = ""
    if y > 1:
        if int(number[-2]) == 1:
            tens1 = teenline[int(number[-1])]
        elif int(number[-2]) == 0:
            tens1 = digit2
        else:
            tens1 = tenline[int(number[-2]) - 2] + " " + digit2
    if y > 2:
        hundreds1 = digits[int(number[-3])] + " hundred "
        if int(number[-3]) > 0:
            hundreds2 = hundreds1
        else:
            hundreds2 = ""
    if y == 1:
        print(digit1.title(),end="")

    if y == 2:
        print(tens1.title(),end="")

    if y == 3:
        print((hundreds2 + tens1).title(),end="")


def recwordnum(x):
    list1 = []
    n = f"{x}"
    y = len(n)
    if y % 3 == 2:
        n = "0" + n
    elif y % 3 == 1:
        n = "00" + n
    # 001 000
    for i in range(0, len(n) - 2, 3):
        b = f"{n[i:i + 3]}"

        while b[0] == "0":
            if b == "000":
                b = " "
            b = b.lstrip("0")
        list1.append(b)
    for j in range(0 - len(list1), 0, 1):
        if list1[j] == None:
            pass
        if j == -11 and int(list1[-11]) > 0:
            number_word1converter(list1[-11])
            print(" decillion ", end="")
        if j == -10 and int(list1[-10]) > 0:
            number_word1converter(list1[-10])
            print(" Nonillion ", end="")
        if j == -9 and int(list1[-9]) > 0:
            number_word1converter(list1[-9])
            print(" Octillion ", end="")
        if j == -8 and int(list1[-8]) > 0:
            number_word1converter(list1[-8])
            print(" Septillion ", end="")
        if j == -7 and int(list1[-7]) > 0:
            number_word1converter(list1[-7])
            print(" Sextillion ", end="")
        if j == -6 and int(list1[-6]) > 0:
            number_word1converter(list1[-6])
            print(" Quintillion ", end="")
        if j == -5 and int(list1[-5]) > 0:
            number_word1converter(list1[-5])
            print(" Quadrillion ", end="")
        if j == -4 and int(list1[-4]) > 0:
            number_word1converter(list1[-4])
            print(" Trillion ", end="")
        if j == -3 and int(list1[-3]) > 0:
            number_word1converter(list1[-3])
            print(" Million ", end="")
        if j == -2 and int(list1[-2]) > 0:
            number_word1converter(list1[-2])
            print(" Thousand ", end="")
        if j == -1 and int(list1[-1]) > 0:
            number_word1converter(list1[-1])
















