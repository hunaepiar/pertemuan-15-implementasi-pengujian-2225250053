from utilitas import status_kelulusan


def hitung_rata_rata(nilai):
    """Menghitung rata-rata nilai."""
    if not nilai:
        return 0

    return sum(nilai) / len(nilai)


def ringkasan(nilai, kkm=60):
    """Menghasilkan ringkasan statistik nilai siswa."""
    if not nilai:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0,
            "tidak_lulus": 0,
        }

    jumlah_lulus = sum(
        1 for angka in nilai
        if status_kelulusan(angka, kkm) == "Lulus"
    )

    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "lulus": jumlah_lulus,
        "tidak_lulus": len(nilai) - jumlah_lulus,
    }