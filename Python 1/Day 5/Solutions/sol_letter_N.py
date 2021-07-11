n = int(input("введите высоту: "))
for i in range(n, 0, -1):
    print("*" + (n - i) * " " + "*" + (i - 1) * " " + "*")
