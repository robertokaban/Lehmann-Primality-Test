def is_prime_lehmann(n, k):
    import random
    
    # Handle kasus khusus n < 2
    if n <= 1:
        return False
    
    # Handle kasus khusus n = 2
    if n == 2:
        return True
    
    # Handle kasus khusus n genap
    if n % 2 == 0:
        return False
    
    # Melakukan pengujian Lehmann sebanyak k kali
    for _ in range(k):
        # Pilih bilangan acak a dalam rentang [2, n-2]
        a = random.randint(2, n - 2)
        
        # Hitung sisa kuadrat a^((n-1)/2) modulo n
        x = pow(a, (n - 1) // 2, n)
        
        # Jika x bukan 1 atau -1 (mod n), maka n bukan bilangan prima
        if x != 1 and x != n - 1:
            return False
    
    # Jika seluruh pengujian berhasil, n kemungkinan besar adalah bilangan prima
    return True

# Contoh penggunaan
n = 1001  # Ganti dengan bilangan yang ingin Anda uji
k = 5   # Jumlah pengujian yang ingin Anda lakukan
result = is_prime_lehmann(n, k)

if result:
    print(f"{n} adalah bilangan prima.")
else:
    print(f"{n} bukan bilangan prima.")
