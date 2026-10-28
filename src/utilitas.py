def konversi_nilai(teks):
    """Mengubah input menjadi nilai angka 0 sampai 100."""
    try:
        nilai = float(teks)
    except (ValueError, TypeError):
        raise ValueError("Nilai harus berupa angka.")

    if not 0 <= nilai <= 100:
        raise ValueError("Nilai harus berada pada rentang 0 sampai 100.")

    return nilai


def status_kelulusan(nilai, kkm=60):
    """Menentukan status kelulusan berdasarkan KKM."""
    if nilai >= kkm:
        return "Lulus"
    return "Tidak Lulus"