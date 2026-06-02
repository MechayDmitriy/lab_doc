import ctypes

cal_primes_lib = ctypes.CDLL("./libcalc.so")
cal_primes_lib.calculate_primes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

n,m = map(int, input("Введите нижнюю и верхнюю границу через пробел: ").split())
primes = (ctypes.c_int*(m+1))()

cal_primes_lib.calculate_primes(primes,m)

k = n
while k<=m:
    counter = 0
    x = -1
    y = 0
    i = 2
    while i <= k/2:
        if (primes[i]==1 and primes[k-i]==1):
            if x == -1:
                x = i
                y = k-i
            counter += 1
        i+=1
    print(f"{k} {counter} {x} {y}")
    k+=2
