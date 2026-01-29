# BPS Data Availability Checker

Skrip sederhana untuk mengecek ketersediaan berbagai jenis data BPS (Badan Pusat Statistik) di Web API BPS untuk domain tertentu.

## Fitur

Skrip ini dapat mengecek ketersediaan data berikut:

1. **Static Tables** - Tabel statis BPS
2. **Dynamic Tables** - Tabel dinamis/data BPS
3. **Subjects** - Subjek/topik data BPS
4. **Publications** - Publikasi BPS
5. **Press Releases** - Siaran pers BPS
6. **Strategic Indicators** - Indikator strategis BPS
7. **News** - Berita BPS
8. **Infographics** - Infografis BPS

## Penggunaan

### 1. Persiapan

Pastikan Anda memiliki:
- Python 3.x terinstall
- Library yang dibutuhkan: `stadata`, `requests`, `pandas`
- API Key dari WebAPI BPS (dapatkan di https://webapi.bps.go.id/developer/)

### 2. Konfigurasi

Edit file `bps_data_checker.py` dan ganti API key:

```python
API_KEY = 'your_api_key_here'  # Ganti dengan API key Anda
```

### 3. Menjalankan Pengecekan Lengkap

```bash
python bps_data_checker.py
```

Script akan mengecek semua jenis data untuk domain Gorontalo (7500) dan menyimpan hasil ke file JSON.

### 4. Menggunakan sebagai Library

```python
from bps_data_checker import BPSDataChecker

# Inisialisasi checker
checker = BPSDataChecker(api_key='your_api_key', domain='7500')

# Mengecek satu jenis data tertentu
static_tables = checker.check_static_tables(limit=10)
publications = checker.check_publications(limit=5)

# Mengecek semua data sekaligus
results = checker.check_all_data_availability(limit_per_category=5)

# Simpan hasil ke file JSON
checker.save_results_to_json(results, 'hasil_cek_data.json')
```

## Output

### Console Output
```
[START] Memulai pengecekan ketersediaan data BPS untuk Domain Gorontalo (7500)
======================================================================
[CHECKING] Mengecek Static Tables untuk domain 7500...
[SUCCESS] Ditemukan 280 Static Tables
[DATA] Static Tables: [SUCCESS] Available
...
======================================================================
[SUCCESS] Pengecekan selesai!
[SAVE] Hasil disimpan ke: bps_data_availability_7500_20260127_160427.json

[SUMMARY] RINGKASAN KETERSEDIAAN DATA BPS GORONTALO
==================================================
[DATA] Static Tables: 280 items
[DATA] Dynamic Tables: 0 items
[DATA] Subjects: 10 items
...
```

### File JSON Output
Script akan menghasilkan file JSON dengan struktur:

```json
{
  "domain": "7500",
  "domain_name": "Gorontalo",
  "check_timestamp": "2026-01-27 16:04:17",
  "data_availability": {
    "static_tables": {
      "status": "success",
      "total_tables": 280,
      "sample_tables": [...],
      "last_checked": "2026-01-27 16:04:17"
    },
    "publications": {
      "status": "success",
      "total_publications": 10,
      "sample_publications": [...],
      "api_response": {...},
      "last_checked": "2026-01-27 16:04:17"
    },
    ...
  }
}
```

## Domain BPS

Untuk menggunakan domain BPS lainnya, ganti parameter domain:

- **7500**: Gorontalo (default)
- **0000**: Pusat/Nasional
- **1100**: Aceh
- **1200**: Sumatera Utara
- dst. (lihat dokumentasi BPS untuk kode lengkap)

```python
# Contoh untuk domain Aceh
checker = BPSDataChecker(api_key='your_api_key', domain='1100')
```

## API Endpoints yang Digunakan

Script ini menggunakan berbagai endpoint Web API BPS:

- `/list/model/statictable/` - Static Tables
- `/list/model/dynamictable/` - Dynamic Tables
- `/list/model/subject/` - Subjects
- `/list/model/publication/` - Publications
- `/list/model/pressrelease/` - Press Releases
- `/list/model/strategicindicator/` - Strategic Indicators
- `/list/model/news/` - News
- `/list/model/infographic/` - Infographics

## Error Handling

Script dilengkapi dengan error handling yang baik:
- Menampilkan pesan error yang jelas di console
- Tetap melanjutkan pengecekan meskipun ada endpoint yang error
- Menyimpan status error di file JSON output

## Dependencies

```txt
stadata
requests
pandas
```

Install dengan:
```bash
pip install stadata requests pandas
```

## Lisensi

Script ini dibuat untuk keperluan pengecekan data BPS dan dapat dimodifikasi sesuai kebutuhan.