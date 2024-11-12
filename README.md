# PRAKTIKUM 4

## Step 1
Pertama-tama, kita memulai dengan membuat list kosong bernama data_mahasiswa. List ini akan berfungsi sebagai wadah untuk menyimpan semua data yang akan dimasukkan oleh pengguna.

![foto](foto/ss1.png)

## Step 2
Selanjutnya, kita menggunakan sebuah perulangan while True untuk meminta pengguna memasukkan data secara berulang. Perulangan ini akan terus berjalan sampai pengguna memutuskan untuk berhenti. Di dalam perulangan, program akan menampilkan pesan untuk memasukkan data mahasiswa.

![foto](foto/ss2.png)

## Step 3
Pada bagian ini, program akan meminta pengguna untuk menginput nama mahasiswa, nilai tugas, nilai UTS, dan nilai UAS. Nilai tugas, UTS, dan UAS dimasukkan sebagai angka desimal (float) untuk memungkinkan input nilai dengan angka pecahan (misalnya 85.5).

Setelah pengguna memasukkan data, program akan menghitung nilai akhir mahasiswa. Rumus yang digunakan untuk menghitung nilai akhir adalah sebagai berikut:

* 30% dari nilai tugas
* 35% dari nilai UTS
* 35% dari nilai UAS

![foto](foto/ss3.png)

## Step 4
Setelah nilai akhir dihitung, program menyimpan semua informasi yang sudah dimasukkan (nama, nilai tugas, UTS, UAS, dan nilai akhir) ke dalam list data_mahasiswa. Data tersebut disimpan dalam bentuk dictionary agar lebih terstruktur.

![foto](foto/ss4.png)

## Step 5
Setiap kali data mahasiswa baru ditambahkan, program akan menanyakan apakah pengguna ingin menambahkan data mahasiswa lain. Jika pengguna menjawab 'y', program akan kembali ke awal perulangan dan meminta input data lagi. Namun, jika pengguna menjawab 't', program akan keluar dari perulangan dan mulai menampilkan daftar data yang sudah dikumpulkan.

![foto](foto/ss5.png)

## Step 6
Setelah keluar dari perulangan, program akan mencetak daftar seluruh mahasiswa beserta nilai-nilai mereka dalam format tabel. Program menggunakan perulangan for untuk membaca setiap elemen dalam list data_mahasiswa dan menampilkannya satu per satu.

![foto](foto/ss6.png)

# OUTPUT
Maka, program akan menghasilkan output seperti berikut:

![foto](foto/ss7.png)

# Flowchart

