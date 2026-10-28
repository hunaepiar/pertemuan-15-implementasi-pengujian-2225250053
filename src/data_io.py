from pathlib import Path
from utilitas import konversi_nilai, status_kelulusan


def baca_data(lokasi_file):
    """Membaca data siswa dari file teks."""
    data = []
    kesalahan = []
    lokasi_file = Path(lokasi_file)

    with lokasi_file.open("r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                kesalahan.append(
                    f"Baris {nomor}: format harus Nama,Nilai."
                )
                continue

            nama = bagian[0].strip()

            if not nama:
                kesalahan.append(
                    f"Baris {nomor}: nama siswa tidak boleh kosong."
                )
                continue

            try:
                nilai = konversi_nilai(bagian[1].strip())
            except ValueError as error:
                kesalahan.append(f"Baris {nomor}: {error}")
                continue

            data.append({"nama": nama, "nilai": nilai})

    return data, kesalahan


def simpan_laporan(lokasi_file, data, statistik, kkm=60):
    """Menyimpan hasil analisis ke dalam file teks."""
    lokasi_file = Path(lokasi_file)
    lokasi_file.parent.mkdir(parents=True, exist_ok=True)

    with lokasi_file.open("w", encoding="utf-8") as file:
        file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
        file.write("=" * 38 + "\n")
        file.write(f"Jumlah siswa : {statistik['jumlah']}\n")
        file.write(
            f"Rata-rata    : {statistik['rata_rata']:.2f}\n"
        )
        file.write(f"Nilai minimum: {statistik['minimum']}\n")
        file.write(f"Nilai maksimum: {statistik['maksimum']}\n")
        file.write(f"KKM          : {kkm}\n")
        file.write(f"Jumlah lulus : {statistik['lulus']}\n")
        file.write(
            f"Jumlah tidak lulus: {statistik['tidak_lulus']}\n\n"
        )

        file.write("DAFTAR NILAI SISWA\n")
        file.write("-" * 38 + "\n")

        for siswa in data:
            status = status_kelulusan(siswa["nilai"], kkm)
            file.write(
                f"{siswa['nama']}: {siswa['nilai']:g} - {status}\n"
            )