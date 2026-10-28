# Dokumentasi Pengujian Program

## Identitas
- Nama: Khunaepi
- NIM: 2225250053
- Proyek: Program Rekap dan Analisis Nilai Matematika Kelas
- Pertemuan: 15

## Tujuan
Memastikan program dapat memvalidasi nilai, menghitung statistik,
menentukan kelulusan, membaca data, dan menyimpan laporan.

## Daftar Test Case

| ID | Fitur | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Konversi nilai | 80 | Nilai diterima |
| TC02 | Nilai minimum | 0 | Nilai diterima |
| TC03 | Nilai maksimum | 100 | Nilai diterima |
| TC04 | Input bukan angka | abc | ValueError |
| TC05 | Nilai di atas batas | 101 | ValueError |
| TC06 | Nilai di bawah batas | -1 | ValueError |
| TC07 | Batas kelulusan | 60 | Lulus |
| TC08 | Di bawah KKM | 59 | Tidak Lulus |
| TC09 | Rata-rata | 70, 80, 90 | 80 |
| TC10 | Data kosong | List kosong | Rata-rata 0 |
| TC11 | Data tidak valid | Budi,abc | Kesalahan dicatat |
| TC12 | File tidak ditemukan | Lokasi tidak tersedia | FileNotFoundError |
| TC13 | Simpan laporan | Data nilai siswa | File laporan dibuat |

## Hasil Pengujian
Hasil aktual dan status PASS/FAIL diisi setelah pengujian
dijalankan. Jangan menandai PASS sebelum hasilnya diperiksa.

## Kesimpulan
Pengujian digunakan untuk memeriksa fungsi utama dan menangani
input tidak valid serta kondisi file yang bermasalah.