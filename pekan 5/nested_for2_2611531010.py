# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1010 = int(input("Masukkan nilai batas: "))
for i_1010 in range(1, batas_1010+ 1):
    for j_1010 in range(1, batas_1010 + 1):
        print("*", end="")
    print() #pindahkan ke baris berikutnya