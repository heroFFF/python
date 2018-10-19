import time
scale = 3
t = time.clock()
for i in range(scale + 1):
    a = '.' * i
    c = (i / scale) * 100
    t -= time.clock()
    print("\r Starting {:^3.0f}%[{}]{:.2f}s Done".format(c,a,-t), end='')
    time.sleep(0.05)
