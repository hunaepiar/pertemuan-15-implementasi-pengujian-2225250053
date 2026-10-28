from pathlib import Path

from data_io import baca_data, simpan_laporan
from analisis import ringkasan


# Lokasi proyek diambil dari folder utama proyek.
FOLDER_PROYEK = Path(__file__).resolve().parent.parent
FILE_DATA = FOLDER_PROYEK / "data" / "nilai_contoh.txt"
FILE_LAPORAN = FOLDER_PROYEK / "output" / "laporan_nilai.txt"
KKM = 60


def main():
    print("=" * 42)
    print("PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA")
    print("=" * 42)

    try:
        data, kesalahan = baca_data(FILE_DATA)
    except FileNotFoundError:
        print(f"File data tidak ditemukan: {FILE_DATA}")
        return

    if kesalahan:
        print("\nData yang perlu diperiksa:")
        for pesan in kesalahan:
            print(f"- {pesan}")

    if not data:
        print("\nTidak ada data valid yang dapat dianalisis.")
        return

    nilai = [siswa["nilai"] for siswa in data]
    statistik = ringkasan(nilai, KKM)

    print(f"\nJumlah siswa : {statistik['jumlah']}")
    print(f"Rata-rata    : {statistik['rata_rata']:.2f}")
    print(f"Nilai minimum: {statistik['minimum']:g}")
    print(f"Nilai maksimum: {statistik['maksimum']:g}")
    print(f"KKM          : {KKM}")
    print(f"Jumlah lulus : {statistik['lulus']}")
    print(f"Jumlah tidak lulus: {statistik['tidak_lulus']}")

    print("\nDAFTAR NILAI SISWA")
    for siswa in data:
        status = (
            "Lulus" if siswa["nilai"] >= KKM else "Tidak Lulus"
        )
        print(f"{siswa['nama']}: {siswa['nilai']:g} - {status}")

    simpan_laporan(FILE_LAPORAN, data, statistik, KKM)
    print(f"\nLaporan berhasil disimpan di: {FILE_LAPORAN}")


if __name__ == "__main__":
    main()