class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, nama, nilai):
        self.data_mahasiswa[nama] = nilai
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            print("\nDaftar Nilai Mahasiswa")
            print("-----------------------")
            for nama, nilai in self.data_mahasiswa.items():
                print(f"Nama : {nama} | Nilai : {nilai}")

    def hapus(self, nama):
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print(f"Data {nama} berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.data_mahasiswa:
            self.data_mahasiswa[nama] = nilai_baru
            print(f"Data {nama} berhasil diubah.")
        else:
            print("Data tidak ditemukan.")


# ========== PROGRAM UTAMA ==========
daftar = DaftarNilaiMahasiswa()

while True:
    print("\nMenu Pilihan")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan Nama: ")
        nilai = input("Masukkan Nilai: ")
        daftar.tambah(nama, nilai)

    elif pilihan == "2":
        daftar.tampilkan()

    elif pilihan == "3":
        nama = input("Masukkan Nama yang akan dihapus: ")
        daftar.hapus(nama)

    elif pilihan == "4":
        nama = input("Masukkan Nama yang akan diubah: ")
        nilai_baru = input("Masukkan nilai baru: ")
        daftar.ubah(nama, nilai_baru)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")




