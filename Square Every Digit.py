def square_digits(num):
    x = str(num)
    y = ""
    for i in x:
        y += str(int(i)**2)
    return int(y)