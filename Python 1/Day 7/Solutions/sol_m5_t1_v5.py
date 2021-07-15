def func_1(p1, p2, p3, p4, p5, p6):
    a = p1 - p5
    b = p3 - p5
    c = p2 - p6
    d = p4 - p6
    a_1 = a * d
    b_1 = b * c
    f = a_1 - b_1
    return 'success' if s else "failure"


def func_2(p1, p2, p3, p4, p5, p6):
    a = p1 - p5
    b = p3 - p5
    c = p2 - p6
    d = p4 - p6
    a_1 = a * d
    b_1 = b * c
    f = a_1 - b_1
    s = 0.5 * abs(f)

    return s if s else "failure"


def func_3(x1, y1, x2, y2, x3, y3):
    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = (x3 - x1) ** 2 + (y3 - y1) ** 2
    c = (x3 - x2) ** 2 + (y3 - y2) ** 2
    res = ("прямоугольный", "не прямоугольный")
    if a + b == c or a + c == b or b + c == a:
        result = res[0]
    else:
        result = res[1]
    return result


x_1 = int(input("enter x1:"))
y_1 = int(input("enter y1:"))
x_2 = int(input("enter x2:"))
y_2 = int(input("enter y2:"))
x_3 = int(input("enter x3:"))
y_3 = int(input("enter y3:"))

print(func_1(x_1, y_1, x_2, y_2, x_3, y_3))
print(func_2(x_1, y_1, x_2, y_2, x_3, y_3))
print(func_3(x_1, y_1, x_2, y_2, x_3, y_3))
