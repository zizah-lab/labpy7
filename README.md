# Labbotarium Python 7
## Program class untuk menampilkan daftar nilai mahasiswa
Program ini merupakan implementasi konsep Object Oriented Programming (OOP) pada bahasa pemrograman Python untuk mengelola daftar nilai mahasiswa.
Program memiliki kemampuan untuk menambah, menampilkan, menghapus, dan mengubah data mahasiswa menggunakan method dalam class.

Program dijalankan secara interaktif melalui menu pilihan sehingga pengguna dapat mengoperasikan sistem dengan mudah.

### Fitur Program
#### Fitur	Method	Fungsi
1. Menambah data	tambah()	Menambah data mahasiswa (nama & nilai)
2. Menampilkan data	tampilkan()	Menampilkan semua data mahasiswa
3. Menghapus data	hapus(nama)	Menghapus data mahasiswa berdasarkan nama
4. Mengubah data	ubah(nama)	Mengubah nilai mahasiswa berdasarkan nama

## Diagram
```
+-----------------------------------------+
|         DaftarNilaiMahasiswa            |
+-----------------------------------------+
| - data_mahasiswa : dict                 |
+-----------------------------------------+
| + tambah(nama, nilai)                   |
| + tampilkan()                           |
| + hapus(nama)                           |
| + ubah(nama, nilai)                     |
+-----------------------------------------+
```

## Kesimpulan

Program ini berhasil mengimplementasikan konsep OOP dasar meliputi:

Class dan object

Atribut dan method

Penggunaan struktur data dictionary

## Flowchart
```
          +-----------------------+
          |     Mulai Program     |
          +-----------+-----------+
                      |
              +-------v-------+
              |  Menu Pilihan |
              +---+---+---+---+
                  |   |   |
         +--------v   v   v--------+
   tambah()   tampilkan()   hapus() / ubah()
                  |
          +-------v-------+
          |  tampil data  |
          +-------+-------+
                  |
          +-------v-------+
          |     Selesai   |
          +---------------+
```
Method CRUD (Create, Read, Update, Delete)

Program ini juga mudah dikembangkan lebih lanjut menjadi GUI atau database.
