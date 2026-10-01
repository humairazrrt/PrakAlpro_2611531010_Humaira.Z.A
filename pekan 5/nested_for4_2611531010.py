# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1010 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1010 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1010 = tinggi_1010
    c_1010 = a_1010
    lebar_1010 = (2 * tinggi_1010) - 2

    for i_1010 in range(1, tinggi_1010 + 1):
        b_1010 = c_1010 + 1

        for j_1010 in range(1, lebar_1010 + 1):

            # Baris atas dan bawah
            if i_1010 == 1 or i_1010 == tinggi_1010:
                if j_1010 == 1 or j_1010 == lebar_1010:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_1010 == 1 or j_1010 == lebar_1010:
                    print("|", end="")
                elif j_1010 == c_1010:
                    print("<", end="")
                elif j_1010 == b_1010:
                    print(">", end="")
                elif j_1010 == (lebar_1010 - c_1010):
                    print("<", end="")
                elif j_1010 == (lebar_1010 - c_1010 + 1):
                    print(">", end="")
                elif b_1010 < j_1010 < (lebar_1010 - c_1010):
                    print(".", end="")
                else:
                    print(" ", end="")

        print()  # pindah baris setelah satu baris selesai

        # Logika asli Java (update nilai untuk baris berikutnya)
        a_1010 -= 2
        if a_1010 <= 0:
            c_1010 = (-a_1010) + 2
        else:
            c_1010 = a_1010                
            
    