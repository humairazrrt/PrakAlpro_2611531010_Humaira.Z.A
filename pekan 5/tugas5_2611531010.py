print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_1010 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border atas
print("#", end="")

for baris_1010 in range(4 * n_1010 + 5):
    print("=", end="")

print("#")

# Fase 1: Jam pasir atas
for baris_1010 in range(n_1010, 0, -1):
    print("|", end=" ")
    
    # Spasi penyeimbang kiri
    for spasi_1010 in range(2 * (n_1010 - baris_1010)):
        print(" ", end="")
    
    # Angka menurun
    for angka_1010 in range(baris_1010, 0, -1):
        print(angka_1010, end=" ")
    
    # Poros kristal
    print("<*>", end="")
    
    # Angka menaik
    for angka_1010 in range(1, baris_1010 + 1):
        print(" ", end="")
        print(angka_1010, end="")
    
    # Spasi penyeimbang kanan
    for spasi_1010 in range(2 * (n_1010 - baris_1010)):
        print(" ", end="")
    
    print(" |")

# Fase 2: Poros titik pusat
print("|", end=" ")

for spasi_1010 in range(2 * n_1010 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_1010 in range(2 * n_1010 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bawah
for baris_1010 in range(1, n_1010 + 1):
    print("|", end=" ")
    
    # Spasi penyeimbang kiri
    for spasi_1010 in range(2 * (n_1010 - baris_1010)):
        print(" ", end="")
    
    # Angka menurun
    for angka_1010 in range(baris_1010, 0, -1):
        print(angka_1010, end=" ")
    
    # Poros kristal
    print("<*>", end="")
    
    # Angka menaik
    for angka_1010 in range(1, baris_1010 + 1):
        print(" ", end="")
        print(angka_1010, end="")
    
    # Spasi penyeimbang kanan
    for spasi_1010 in range(2 * (n_1010 - baris_1010)):
        print(" ", end="")
    
    print(" |")

# Border bawah
print("#", end="")

for baris_1010 in range(4 * n_1010 + 5):
    print("=", end="")

print("#")