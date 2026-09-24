# Buat file dengan nama if_nim.py
# Buat program untuk kondisi if
# Nma variabel ditambah 4 digit nim terakhir contoh: ipk_1010
# Program konversi nilai angka menjadi huruf

nilai_1010 = int(input("Masukkan nilai angka = "))

if nilai_1010 >= 81:
    print("A")
elif nilai_1010 >= 70:
    print("B")
elif nilai_1010 >= 60:
    print("C")
elif nilai_1010 >= 50:
    print("D")
else:
    print("E")