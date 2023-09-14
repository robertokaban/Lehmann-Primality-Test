## Algoritma Lehmann
Algoritma Lehmann adalah salah satu algoritma yang digunakan untuk menguji bilangan prima.
Langkah-langkahnya adalah sebgai berikut:

a) Bangkitkan bilangan acak a yang lebih kecil dari p.
b) Hitung a(p – 1)/2 mod p.
c) Jika a(p – 1)/2 / 1 atau –1 (mod p), maka p tidak prima.
d) Jika a(p – 1)/2  1 atau –1 (mod p), maka peluang p bukan prima adalah 50%.

Ulangi pengujian dengan algoritma Lehmann di atas sebanyak t kali (dengan nilai a yang berbeda). Jika hasil perhitungan langkah (b) sama dengan 1 atau –1, tetapi tidak selalu sama dengan 1, maka peluang p adalah prima mempunyai kesalahan tidak lebih dari 1/2t. 

Bilangan acak a yang digunakan pada algoritma Lehmann dapat dipilih nilai yang kecil agar perhitungan lebih cepat. Sedangkan jumlah pengujian yang disarankan adalah lima kali.
