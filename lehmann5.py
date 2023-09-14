import random

def is_prime_lehmann(p, t):
    if p <= 1:
        return False, ["Bukan prima (p <= 1)"]
    if p == 2:
        return True, ["Prima (p = 2)"]

    results = []
    for i in range(t):
        # Langkah (a): Bangkitkan bilangan acak a yang lebih kecil dari p
        a = random.randint(2, p - 2)
        results.append(f"Langkah (a) - Uji ke-{i + 1}: a = {a}")

        # Langkah (b): Hitung a(p - 1)/2 mod p
        x = pow(a, (p - 1) // 2, p)
        results.append(f"Langkah (b) - Uji ke-{i + 1}: x = {a}^(({p} - 1)/2) mod {p} = {x}")

        # Langkah (c): Jika x bukan 1 atau -1 (mod p), maka p tidak prima
        if x != 1 and x != p - 1:
            return False, results + [f"Langkah (c) - Uji ke-{i + 1}: x ({x}) bukan 1 atau -1 (mod {p}), p tidak prima"]

    # Jika langkah (b) selalu menghasilkan 1 atau -1, maka peluang p prima
    return True, results + [f"Prima (uji ke-{t} berhasil)"]

try:
    p = int(input("Masukkan bilangan yang akan diuji keprimaannya (p): "))
    t = int(input("Masukkan jumlah pengujian (t): "))

    is_prime, reasons = is_prime_lehmann(p, t)

    if is_prime:
        print(f"{p} adalah bilangan prima.")
        print("Detail Perhitungan:")
        for reason in reasons:
            print(reason)
    else:
        print(f"{p} bukan bilangan prima.")
        print("Detail Perhitungan:")
        for reason in reasons:
            print(reason)
except ValueError:
    print("Masukkan bilangan bulat yang valid untuk p dan t.")
