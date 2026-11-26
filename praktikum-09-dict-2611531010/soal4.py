# membaca input
all_students = input().split()
submitted_students = input().split()

# mengubah menjadi set untuk menghilangkan duplikat
all_set = set(all_students)
submitted_set = set(submitted_students)

# menghitung mahasiswa yang sudah mengumpulkan
submitted = all_set & submitted_set

# menghitung mahasiswa yang belum mengumpulkan
not_submitted = all_set - submitted_set

# menampilkan hasil
print(f"Submitted: {len(submitted)} students")
print(f"Not submitted: {len(not_submitted)} students")

# menampilkan nomor absen yang belum mengumpulkan
for student in all_students:
    if student in not_submitted:
        print(student)
        not_submitted.remove(student)