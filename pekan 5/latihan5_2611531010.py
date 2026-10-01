# Buat file dengan nama latihan5_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()
# Program menampilkan ouput segitiga dengan perulangan for

tinggi_1010 = int(input("Masukkan tinggi segitiga: "))

for i_1010 in range(1, tinggi_1010 + 1):
    print(" " * (tinggi_1010 - i_1010), end="")
    print("* " * i_1010)