import time

def test(x):
    a = 0

    #now you count only the loop time
    t1 = time.time()
    while(a < x):
        a += 1

    t2 = time.time()

    print("Time for {} was {}".format(x, t2 - t1))
    return a

print(test(100000000))
