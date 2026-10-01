# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1010 = int(input("Masukkan jumlah perulangan: "))

jumlah_1010 = 0
for i_1010 in range(1_1010, ulang_1010 + 1):
    print(i_1010, end=" ")
    jumlah_1010 = jumlah_1010 + 1
    
    if i_1010 < ulang_1010:
        print("+", end="")
    else: 
        print("=", jumlah_1010, end="") 
print()
print("Jumlah =", jumlah_1010)           