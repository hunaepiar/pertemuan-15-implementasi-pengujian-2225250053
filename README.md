Program Rekap dan Analisis Nilai Matematika Kelas

Identitas
- Nama: Khunaepi
- Nim: 2225250053
- Kelas: 3B

1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program berbasis Python yang digunakan untuk mengolah nilai siswa secara otomatis. Program ini dapat membaca data nilai dari file teks, menghitung statistik nilai, menentukan status kelulusan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan hasil analisis dalam bentuk laporan.

Proyek ini merupakan implementasi dari proposal yang telah disusun pada Pertemuan 14 dan dikembangkan lebih lanjut pada Pertemuan 15.

2. Tujuan Proyek

- Mengimplementasikan rancangan proyek menjadi program Python yang dapat dijalankan.
- Mempermudah proses rekapitulasi nilai matematika siswa.
- Menghitung statistik nilai secara otomatis.
- Menentukan status kelulusan siswa berdasarkan KKM.
- Melakukan pengujian dan perbaikan program.
- Menyusun dokumentasi agar program mudah dipahami dan digunakan kembali.

3. Teknologi yang Digunakan

- Python 3.12 sebagai bahasa pemrograman.
- Visual Studio Code sebagai editor kode.
- "uv" untuk menjalankan Python dengan versi yang ditentukan.
- Git untuk mencatat perubahan kode.
- GitHub untuk menyimpan repositori proyek.
- Modul "unittest" untuk melakukan pengujian program.

4. Struktur Proyek

pertemuan-15-implementasi-pengujian-2225250053/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   └── test_program.py
└── output/
    ├── .gitkeep
    └── laporan_nilai.txt

5. Fitur Program

1. Membaca data nama dan nilai siswa dari file teks.
2. Memvalidasi nilai agar berada pada rentang 0–100.
3. Menangani data yang tidak sesuai format.
4. Menghitung jumlah siswa dan rata-rata nilai.
5. Menentukan nilai minimum dan maksimum.
6. Menentukan status kelulusan siswa berdasarkan KKM 60.
7. Menampilkan hasil analisis pada terminal.
8. Menyimpan hasil analisis ke dalam file laporan.

6. Pengembangan Proyek

Pengembangan dilakukan berdasarkan proposal proyek pada Pertemuan 14. Program dibagi menjadi beberapa modul agar kode lebih terstruktur dan mudah dipelihara.

- "main.py": menjalankan program utama dan menampilkan hasil analisis.
- "data_io.py": membaca data siswa dan menyimpan laporan.
- "analisis.py": menghitung statistik nilai siswa.
- "utilitas.py": memvalidasi nilai dan menentukan status kelulusan.

Program dikembangkan dengan menggunakan fungsi, struktur data berupa list dan dictionary, serta pengolahan file teks. Setiap modul memiliki tanggung jawab yang berbeda agar program lebih mudah diuji dan dikembangkan kembali.

7. Cara Menjalankan Program

Pastikan Python 3.12 dan "uv" telah tersedia di lingkungan pengembangan.

Buka terminal VS Code pada folder utama proyek, kemudian jalankan:

uv run --python 3.12 python .\src\main.py

Program akan membaca data dari "data/nilai_contoh.txt", menampilkan hasil analisis pada terminal, dan menyimpan laporan ke "output/laporan_nilai.txt".

8. Pengujian Program

Pengujian dilakukan menggunakan modul "unittest" untuk memastikan fungsi program berjalan sesuai harapan.

Jalankan perintah berikut di terminal VS Code:

uv run --python 3.12 python -m unittest discover -s tests -v

Pengujian mencakup:

- Konversi nilai yang valid.
- Nilai batas minimum dan maksimum.
- Input yang bukan angka.
- Nilai di luar rentang 0–100.
- Penentuan status kelulusan.
- Perhitungan rata-rata dan statistik nilai.
- Pembacaan data siswa.
- Penanganan file yang tidak ditemukan.
- Penyimpanan laporan.

Hasil pengujian menunjukkan "OK", yang berarti seluruh test case yang dijalankan berhasil.

9. Data Contoh

Data siswa yang digunakan untuk pengujian program:

Nama| Nilai
Ani| 80
Budi| 70
Citra| 90
Deni| 60
Eka| 50

KKM yang digunakan adalah 60.

Berdasarkan data tersebut, jumlah siswa adalah 5, rata-rata nilai 70, nilai minimum 50, nilai maksimum 90, jumlah siswa lulus 4, dan jumlah siswa tidak lulus 1.

10. Debugging dan Perbaikan Bug

Proses debugging dilakukan ketika pengujian mengalami kendala. Salah satu kendala yang ditemukan adalah program pengujian tidak dapat menemukan modul Python karena masalah lokasi atau nama folder sumber kode.

Perbaikan dilakukan dengan memeriksa struktur folder proyek dan menyesuaikan lokasi modul yang digunakan dalam pengujian. Setelah perbaikan, pengujian dijalankan kembali hingga menghasilkan "OK".

Pengujian ulang dilakukan untuk memastikan perbaikan tidak mengganggu fungsi program lainnya.

11. Hasil dan Kesimpulan

Program berhasil dijalankan dan diuji. Fitur pembacaan data, validasi nilai, perhitungan statistik, penentuan kelulusan, dan penyimpanan laporan telah diimplementasikan.

Melalui proyek ini, penggunaan fungsi, modularisasi, pengolahan file, pengujian otomatis, debugging, serta dokumentasi menggunakan README dapat diterapkan dalam pengembangan program Python.

12. Referensi

1. Bahan Ajar Algoritma dan Pemrograman, Pertemuan 14: Perancangan Proyek VS Code dan GitHub, Program Studi Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa, Tahun Ajaran 2026/2027.
2. Bahan Ajar Algoritma dan Pemrograman, Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi Proyek di VS Code, Git, dan GitHub, Program Studi Pendidikan Matematika, FKIP Universitas Sultan Ageng Tirtayasa, Tahun Ajaran 2026/2027.
3. Python Software Foundation. Python 3 Documentation. https://docs.python.org/3/
4. Python Software Foundation. unittest — Unit Testing Framework. https://docs.python.org/3/library/unittest.html
5. GitHub Docs. GitHub Documentation. https://docs.github.com/

13. Bantuan dan Pengembangan Lanjutan

Pengembangan proyek ini mengacu pada materi perkuliahan, dokumentasi resmi Python, dokumentasi "unittest", serta dokumentasi GitHub. Bantuan dalam proses pengembangan juga diperoleh melalui diskusi dan penggunaan ChatGPT untuk memahami kode, memperbaiki kesalahan, dan menyusun dokumentasi.

Pengembangan selanjutnya dapat mencakup:

- Menambahkan fitur input nilai secara langsung dari pengguna.
- Menyediakan pilihan KKM yang dapat diubah.
- Menyimpan laporan dalam format CSV.
- Menambahkan tampilan antarmuka yang lebih mudah digunakan.
- Memperluas test case untuk menguji lebih banyak kondisi input.

14. Informasi Proyek

- Nama proyek: Program Rekap dan Analisis Nilai Matematika Kelas
- Mata kuliah: Algoritma dan Pemrograman
- Pertemuan: 15
- Bahasa pemrograman: Python
- Status: Implementasi dan pengujian telah dilakukan