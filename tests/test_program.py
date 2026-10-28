import sys
import tempfile
import unittest
from pathlib import Path

FOLDER_PROYEK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FOLDER_PROYEK / "src"))

from utilitas import konversi_nilai, status_kelulusan
from analisis import hitung_rata_rata, ringkasan
from data_io import baca_data, simpan_laporan


class TestProgram(unittest.TestCase):

    def test_konversi_nilai_valid(self):
        self.assertEqual(konversi_nilai("80"), 80.0)

    def test_nilai_batas(self):
        self.assertEqual(konversi_nilai("0"), 0.0)
        self.assertEqual(konversi_nilai("100"), 100.0)

    def test_nilai_bukan_angka(self):
        with self.assertRaises(ValueError):
            konversi_nilai("abc")

    def test_nilai_di_luar_rentang(self):
        with self.assertRaises(ValueError):
            konversi_nilai("101")

        with self.assertRaises(ValueError):
            konversi_nilai("-1")

    def test_status_kelulusan(self):
        self.assertEqual(status_kelulusan(60), "Lulus")
        self.assertEqual(status_kelulusan(59), "Tidak Lulus")

    def test_rata_rata(self):
        self.assertEqual(hitung_rata_rata([70, 80, 90]), 80)
        self.assertEqual(hitung_rata_rata([]), 0)

    def test_ringkasan(self):
        hasil = ringkasan([70, 80, 90])
        self.assertEqual(hasil["jumlah"], 3)
        self.assertEqual(hasil["rata_rata"], 80)
        self.assertEqual(hasil["minimum"], 70)
        self.assertEqual(hasil["maksimum"], 90)
        self.assertEqual(hasil["lulus"], 3)
        self.assertEqual(hasil["tidak_lulus"], 0)

    def test_baca_data(self):
        with tempfile.TemporaryDirectory() as folder:
            file_data = Path(folder) / "data.txt"
            file_data.write_text(
                "Ani,80\nBudi,abc\nCitra,90\n",
                encoding="utf-8",
            )

            data, kesalahan = baca_data(file_data)

            self.assertEqual(len(data), 2)
            self.assertEqual(len(kesalahan), 1)

    def test_file_tidak_ditemukan(self):
        with self.assertRaises(FileNotFoundError):
            baca_data("file_yang_tidak_ada.txt")

    def test_simpan_laporan(self):
        with tempfile.TemporaryDirectory() as folder:
            file_laporan = Path(folder) / "output" / "laporan.txt"
            data = [{"nama": "Ani", "nilai": 80}]
            statistik = ringkasan([80])

            simpan_laporan(file_laporan, data, statistik)

            self.assertTrue(file_laporan.exists())
            isi = file_laporan.read_text(encoding="utf-8")
            self.assertIn("Ani: 80 - Lulus", isi)


if __name__ == "__main__":
    unittest.main()