a = 515
c = 1
m = 2**9
xn = 1

list = []
for i in range(0,100000):
    xn = (a*xn + c) % m
    if xn in list:
        print("Repetido %s" % xn)
        print(len(list))
        break
    else:
        print(xn)
        list.append(xn)
    