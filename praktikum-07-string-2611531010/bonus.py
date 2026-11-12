Nama = input("Masukkan Kalimat:")
nama = Nama.lower().strip()
nama_terbalik = nama[::-1]
if nama == nama_terbalik:
    print("Palindrome")
else:
    print("Not a palindrome")