# Buat file dengan nama proram multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: umur_1234
# Program ini menggunakan fungsi input()

umur_1010 = int(input("Input umur anda: "))
sim_1010 = input("Apakah Anda Sudah Punya Sim C (y/t): ") [0]

if umur_1010 >= 17 and sim_1010 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")
    
if umur_1010 >= 17 and sim_1010 != 'y':
   print("Anda Sudah Dewasa tetapi tidak boleh bawa motor")
   
if umur_1010 < 17  and sim_1010 == 'y' :
    print("Anda belum cukup umur punya SIM")
    
if umur_1010 <17 and sim_1010 != 'y':
    print("Anda belum cukup umur bawa motor")