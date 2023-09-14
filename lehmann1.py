def is_prime_lehmann(n, k):
    import random

    if n <= 1:
        return False, "Bukan prima (n <= 1)"
    if n == 2:
        return True, "Prima (n = 2)"
    if n % 2 == 0:
        return False, "Bukan prima (n genap)"

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, (n - 1) // 2, n)
        if x != 1 and x != n - 1:
            return False, f"Bukan prima (uji ke-{k} gagal)"

    return True, f"Prima (uji ke-{k} berhasil)"

try:
    n = int(input("Masukkan sebuah bilangan: "))
    k = 5  # Jumlah pengujian Lehmann, bisa disesuaikan

    is_prime, reason = is_prime_lehmann(n, k)

    if is_prime:
        print(f"{n} adalah bilangan prima. Alasan: {reason}")
    else:
        print(f"{n} bukan bilangan prima. Alasan: {reason}")
except ValueError:
    print("Masukkan bilangan bulat yang valid.")
