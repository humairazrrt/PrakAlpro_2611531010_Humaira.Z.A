# Name: <Humaira Zahratul 'Aini>
# NIM: <2611531010>
# Question Bonus

kalimat = input("Masukkan Kalimat: ")
teks = kalimat.replace(" "," ").lower()
if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
    