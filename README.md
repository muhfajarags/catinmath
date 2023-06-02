# catinmath

`catinmath` adalah sebuah paket Python yang menyediakan berbagai rumus matematika terkait dengan kucing. Paket ini dapat digunakan untuk melakukan perhitungan dan analisis yang berkaitan dengan pertumbuhan kucing, genetika kucing, kebutuhan makanan, populasi kucing, dan masih banyak lagi.

## Instalasi

Paket `catinmath` dapat diinstal menggunakan pip. Jalankan perintah berikut ini:

```
pip install catinmath
```

## Penggunaan

Berikut ini adalah contoh penggunaan paket `catinmath`:

from catinmath import kucing_pertumbuhan, hitung_probabilitas_genetik, hitung_kebutuhan_makanan

# Contoh penggunaan rumus dalam catinmath
from catinmath import (
    kucing_pertumbuhan,
    hitung_probabilitas_genetik,
    hitung_kebutuhan_makanan,
    model_populasi_kucing,
    hitung_imt_kucing,
    konversi_umur_kucing,
    hitung_kebutuhan_cairan,
    hitung_energi_metabolis,
    konversi_kilogram_ke_pound,
    konversi_pound_ke_kilogram,
    hitung_daya_tahan_fisik,
    hitung_jumlah_anak_kucing,
    hitung_kebutuhan_vitamin_mineral,
)

# Contoh penggunaan rumus pertumbuhan kucing
berat_awal = 1.5  # kg
bulan = 6
berat_kucing = kucing_pertumbuhan(berat_awal, bulan)
print("Berat kucing setelah 6 bulan:", berat_kucing)

# Contoh penggunaan rumus probabilitas genetik
probabilitas = hitung_probabilitas_genetik("Aa", "Aa")
print("Probabilitas penampilan genetik:", probabilitas)

# Contoh penggunaan rumus kebutuhan makanan
berat_badan = 3.2  # kg
kebutuhan_makanan = hitung_kebutuhan_makanan(berat_badan)
print("Kebutuhan makanan harian:", kebutuhan_makanan)

# Contoh penggunaan model populasi kucing
populasi_awal = 100
tahun = 5
populasi_akhir = model_populasi_kucing(populasi_awal, tahun)
print("Populasi kucing setelah 5 tahun:", populasi_akhir)

# Contoh penggunaan rumus IMT kucing
berat_badan = 4.5  # kg
tinggi_badan = 25  # cm
imt = hitung_imt_kucing(berat_badan, tinggi_badan)
print("Indeks Massa Tubuh (IMT) kucing:", imt)

# Contoh penggunaan konversi umur kucing
umur_tahun = 2
umur_bulan = 6
umur_hari = konversi_umur_kucing(umur_tahun, umur_bulan, umur_hari)
print("Umur kucing dalam hari:", umur_hari)

# Contoh penggunaan rumus kebutuhan cairan
berat_badan = 3.5  # kg
kebutuhan_cairan = hitung_kebutuhan_cairan(berat_badan)
print("Kebutuhan cairan harian kucing:", kebutuhan_cairan)

# Contoh penggunaan rumus energi metabolis
berat_badan = 4.0  # kg
energi_metabolis = hitung_energi_metabolis(berat_badan)
print("Kebutuhan energi metabolis kucing:", energi_metabolis)

# Contoh penggunaan konversi berat kucing
berat_kilogram = 3.2  # kg
berat_pound = konversi_kilogram_ke_pound(berat_kilogram)
print("Berat kucing dalam pound:", berat_pound)

berat_pound = 7.0  # pound
berat_kilogram = konversi_pound_ke_kilogram(berat_pound)
print("Berat kucing dalam kilogram:", berat_kilogram)

# Contoh penggunaan rumus daya tahan fisik
umur = 4  # bulan
daya_tahan = hitung_daya_tahan_fisik(umur)
print("Daya tahan fisik kucing:", daya_tahan)

# Contoh penggunaan rumus jumlah anak kucing
jumlah_induk = 5
jumlah_anak = hitung_jumlah_anak_kucing(jumlah_induk)
print("Jumlah anak kucing dalam satu kehamilan:", jumlah_anak)

# Contoh penggunaan rumus kebutuhan vitamin dan mineral
berat_badan = 3.8  # kg
kebutuhan_vitamin, kebutuhan_mineral = hitung_kebutuhan_vitamin_mineral(berat_badan)
print("Kebutuhan vitamin kucing:", kebutuhan_vitamin)
print("Kebutuhan mineral kucing:", kebutuhan_mineral)


## Daftar Rumus

Berikut ini adalah daftar rumus yang tersedia dalam paket `catinmath`:

- Rumus Pertumbuhan Kucing
- Rumus Probabilitas Penampilan Genetik
- Rumus Perhitungan Kebutuhan Makanan
- Model Populasi Kucing
- Rumus Indeks Massa Tubuh (IMT) Kucing
- Rumus Konversi Umur Kucing
- Rumus Perhitungan Kebutuhan Cairan
- Rumus Perhitungan Energi Metabolis
- Rumus Perhitungan Daya Tahan Fisik Kucing
- Rumus Perhitungan Kebutuhan Vitamin dan Mineral Kucing