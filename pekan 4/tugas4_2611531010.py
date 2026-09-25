# =========================================================
# SISTEM LOKET TERPADU & AUDIT TRANSAKSI EKSPEDISI WAHANA
# Modul Pekan 4 - Praktikum Struktur Data
# =========================================================

# Input Data Pengunjung & String Handling
nama_1010 = input("Masukkan Nama Pengunjung        : ")
umur_1010 = int(input("Input umur anda                 : "))

# mengambil karakter pertama dan diubah ke huruf kecil
sim_input_1010 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
sim_1010 = sim_input_1010[0] if sim_input_1010 else "t"

# menampilkan pilihan paket wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

pilihan_paket_1010 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1010 = int(input("Masukkan jumlah tiket           : "))

# penerapan IF tunggal untuk validasi kuota tiket
if jumlah_tiket_1010 <= 0: print("\n[Peringatan] Jumlah kuota tiket tidak valid!")

# input status member dan kode promo
is_member_input_1010 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_input_1010 = (input("Apakah kode promo valid? (y/t)  : ").strip().lower())

# inisialisasi variabel pendukung
nama_wahana_1010 = ""
harga_satuan_1010 = 0
valid_paket_1010 = True

# Pemilihan Wahana Menggunakan match-case (1-5 & default _)
match pilihan_paket_1010:
    case 1:
        nama_wahana_1010 = "Wahana Safari Rimba"
        harga_satuan_1010 = 50000
    case 2:
        nama_wahana_1010 = "Wahana Arung Jeram"
        harga_satuan_1010 = 75000
    case 3:
        nama_wahana_1010 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1010 = 120000
    case 4:
        nama_wahana_1010 = "Wahana Roller Coaster Kilat"
        harga_satuan_1010 = 100000
    case 5:
        nama_wahana_1010 = "Wahana All-Access VIP"
        harga_satuan_1010 = 220000
    case _:
        print("\nPaket wahana tidak valid!")
        valid_paket_1010 = False

# Eksekusi sisa transaksi jika paket wahana valid
if valid_paket_1010:
    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

    # validasi Izin Kendali Wahana Menggunakan if - elif - else dan Operator Logika (and, !=)
    if pilihan_paket_1010 == 3:
        if umur_1010 >= 17 and sim_1010 == "y":
            print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
        elif umur_1010 >= 17 and sim_1010 != "y":
            print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_1010 < 17 and sim_1010 == "y":
            print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
    else:
        if umur_1010 >= 10:
            print(f"Status Akses: Pengunjung memenuhi syarat usia untuk {nama_wahana_1010}.")
        else:
            print(f"Status Akses: Pengunjung belum cukup umur untuk {nama_wahana_1010}.")

    # Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
    subtotal_1010 = harga_satuan_1010 * jumlah_tiket_1010
    total_diskon_persen_1010 = 0

    if subtotal_1010 >= 200000:
        total_diskon_persen_1010 += 10  # Diskon Belanja Besar

    if is_member_input_1010 in ["y", "ya"]:
        total_diskon_persen_1010 += 5  # Diskon Member

    if kode_promo_input_1010 in ["y", "ya"]:
        total_diskon_persen_1010 += 15  # Diskon Voucher Promo

    if jumlah_tiket_1010 >= 5:
        total_diskon_persen_1010 += 5  # Diskon Tambahan Rombongan

    # Evaluasi Kelulusan Audit & Rincian Pembayaran
    nominal_diskon_1010 = subtotal_1010 * (total_diskon_persen_1010 / 100)
    total_bayar_1010 = subtotal_1010 - nominal_diskon_1010

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {subtotal_1010:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_1010}% (Rp {nominal_diskon_1010:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_1010:,.0f}")

    if total_bayar_1010 > 300000:
        print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
    else:
        print("Catatan Layanan  : Terima kasih telah berkunjung.")

    print("Program Selesai")