import random

def is_prime_lehmann(p, t):
    if p <= 1:
        return False
    if p == 2:
        return True

    for _ in range(t):
        # Langkah (a): Bangkitkan bilangan acak a yang lebih kecil dari p
        a = random.randint(2, p - 2)

        # Langkah (b): Hitung a(p - 1)/2 mod p
        x = pow(a, (p - 1) // 2, p)

        # Langkah (c): Jika x bukan 1 atau -1 (mod p), maka p tidak prima
        if x != 1 and x != p - 1:
            return False

    # Jika langkah (b) selalu menghasilkan 1 atau -1, maka peluang p prima
    return True

try:
    p = int(input("Masukkan bilangan yang akan diuji keprimaannya (p): "))
    t = int(input("Masukkan jumlah pengujian (t): "))

    if is_prime_lehmann(p, t):
        print(f"{p} adalah bilangan prima.")
    else:
        print(f"{p} bukan bilangan prima.")
except ValueError:
    print("Masukkan bilangan bulat yang valid untuk p dan t.")
