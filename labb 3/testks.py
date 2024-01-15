import time
def f1(n):
    start = time.time()
    summa = 0
    for i in range(n):
        for j in range(n):
            summa = summa + i * j
    end = time.time()
    x = end - start
    return summa,x
x, summa = f1(4)
print(summa,x)
#(15562562500, 0.04282689094543457)

