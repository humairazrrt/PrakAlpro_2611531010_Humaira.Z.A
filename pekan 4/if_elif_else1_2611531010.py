# Buat file dengan nama proram if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_1010 = int(input("Input umur anda: "))
sim_1010 = input("Apakah Anda Sudah Punya Sim C: ") [0]

if umur_1010 >= 17 and sim_1010 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")
elif umur_1010 >= 17 and sim_1010 != 'y':
    print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")
elif umur_1010 < 17 and sim_1010 == 'y':
    print("Anda belum cukup umur punya SIM")
else: 
    print("Anda Belum Cukup Umur dan Tidak boleh bawa motor")
print("Program Selesai")