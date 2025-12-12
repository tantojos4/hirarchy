# Panduan Update Data SD Negeri dari Website Didaksmen

Dokumen ini menjelaskan cara memperbarui data sekolah dasar negeri di 27 file JSON untuk setiap kecamatan di Kabupaten Banyumas menggunakan data terbaru dari website Didaksmen (Direktorat Pendidikan Dasar dan Menengah).

## Sumber Data Resmi

Data sekolah dapat diambil dari sumber resmi berikut:

1. **Portal Data Kemendikdasmen** (Recommended)
   - URL: https://data.kemendikdasmen.go.id/data-induk
   - Format: CSV, XLSX (Excel)
   - Update: Harian

2. **Referensi Data Kemendikdasmen**
   - URL: https://referensi.data.kemendikdasmen.go.id/
   - Format: Web Table (dapat di-export)

3. **Data Pokok Pendidikan (Dapodik)**
   - URL: https://dapo.kemendikdasmen.go.id/sp
   - Format: Web Interface

4. **Open Data Kabupaten Banyumas**
   - URL: https://data.banyumaskab.go.id/dataset
   - Format: CSV, XLS

## Struktur Data yang Dibutuhkan

Setiap file JSON harus mengikuti format berikut:

```json
[
  {
    "No": "1",
    "NPSN": "20302232",
    "Nama Sekolah": "Sekolah Dasar Negeri 1 Banjarsari Kecamatan Ajibarang",
    "Alamat": "Banjarsari , Rt. 06 / Rw. 1",
    "Kelurahan": "Banjarsari",
    "Status": "NEGERI"
  },
  {
    "No": "2",
    "NPSN": "20302319",
    "Nama Sekolah": "Sekolah Dasar Negeri 1 Ciberung Kecamatan Ajibarang",
    "Alamat": "Jl. Raya Ajibarang - Bumiayu Km. 3",
    "Kelurahan": "Ciberung",
    "Status": "NEGERI"
  }
]
```

### Field Description:
- **No**: Nomor urut (string)
- **NPSN**: Nomor Pokok Sekolah Nasional (8 digit, string)
- **Nama Sekolah**: Nama lengkap sekolah termasuk "Kecamatan [nama kecamatan]"
- **Alamat**: Alamat lengkap sekolah
- **Kelurahan**: Nama desa/kelurahan
- **Status**: Selalu "NEGERI" untuk SD Negeri

## Daftar File yang Perlu Diupdate

27 file JSON untuk kecamatan di Kabupaten Banyumas:

1. `sd_negeri_ajibarang.json`
2. `sd_negeri_banyumas.json`
3. `sd_negeri_baturaden.json`
4. `sd_negeri_cilongok.json`
5. `sd_negeri_gumelar.json`
6. `sd_negeri_jatilawang.json`
7. `sd_negeri_kalibagor.json`
8. `sd_negeri_karanglewas.json`
9. `sd_negeri_kebasen.json`
10. `sd_negeri_kedung_banteng.json`
11. `sd_negeri_kembaran.json`
12. `sd_negeri_kemranjen.json`
13. `sd_negeri_lumbir.json`
14. `sd_negeri_patikraja.json`
15. `sd_negeri_pekuncen.json`
16. `sd_negeri_purwojati.json`
17. `sd_negeri_purwokerto_barat.json`
18. `sd_negeri_purwokerto_selatan.json`
19. `sd_negeri_purwokerto_timur.json`
20. `sd_negeri_purwokerto_utara.json`
21. `sd_negeri_rawalo.json`
22. `sd_negeri_sokaraja.json`
23. `sd_negeri_somagede.json`
24. `sd_negeri_sumbang.json`
25. `sd_negeri_sumpiuh.json`
26. `sd_negeri_tambak.json`
27. `sd_negeri_wangon.json`

## Metode 1: Menggunakan Script Otomatis (Jika Website Accessible)

### Instalasi Dependencies

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### Menjalankan Script

```bash
# Update semua kecamatan
python update_sd_data.py

# Update kecamatan tertentu saja
python update_sd_data.py --kecamatan ajibarang

# Dry run (preview tanpa mengubah file)
python update_sd_data.py --dry-run
```

## Metode 2: Mode Manual (Jika Website Diblokir)

Jika website didaksmen tidak dapat diakses langsung, ikuti langkah manual berikut:

### Langkah 1: Download Data

1. Buka https://data.kemendikdasmen.go.id/data-induk
2. Login jika diperlukan (atau gunakan akses publik)
3. Filter data:
   - **Provinsi**: Jawa Tengah
   - **Kabupaten/Kota**: Banyumas
   - **Jenjang**: SD (Sekolah Dasar)
   - **Status**: Negeri
4. Download data dalam format CSV atau Excel

### Langkah 2: Update Menggunakan File Manual

```bash
# Menggunakan file CSV/Excel yang sudah didownload
python update_sd_data.py --manual /path/to/data_sekolah_banyumas.csv

# Update kecamatan tertentu dari file manual
python update_sd_data.py --manual /path/to/data.csv --kecamatan cilongok
```

### Langkah 3: Verifikasi

Setelah update, verifikasi file JSON:

```bash
# Cek format JSON valid
python -m json.tool sd_negeri_ajibarang.json > /dev/null && echo "✓ Valid JSON"

# Hitung jumlah sekolah
python -c "import json; print(len(json.load(open('sd_negeri_ajibarang.json'))))"
```

## Metode 3: Update Manual Per File

Jika script tidak bisa digunakan, Anda dapat update manual setiap file:

1. Buka file JSON yang akan diupdate (misalnya `sd_negeri_ajibarang.json`)
2. Akses website didaksmen dan cari data untuk kecamatan tersebut
3. Salin data sekolah satu per satu dengan format yang benar
4. Pastikan:
   - Nomor urut benar (dimulai dari "1")
   - NPSN lengkap 8 digit
   - Nama sekolah include "Kecamatan [nama]"
   - Status selalu "NEGERI"
5. Validasi JSON format dengan online validator atau:
   ```bash
   python -m json.tool sd_negeri_ajibarang.json
   ```

## Troubleshooting

### Website Diblokir atau Tidak Bisa Diakses

**Solusi:**
1. Gunakan VPN untuk mengakses website pemerintah
2. Hubungi Dinas Pendidikan Kabupaten Banyumas untuk mendapatkan data
3. Gunakan data dari Portal Open Data Banyumas: https://data.banyumaskab.go.id

### Format Data Tidak Sesuai

**Masalah**: Data dari website memiliki format/kolom berbeda

**Solusi:**
1. Edit script `update_sd_data.py` pada fungsi `load_manual_data()`
2. Sesuaikan nama kolom sesuai dengan file yang didownload
3. Contoh mapping:
   ```python
   "NPSN": row.get('NPSN', row.get('Nomor NPSN', ''))
   "Nama Sekolah": row.get('Nama', row.get('Nama Satuan Pendidikan', ''))
   ```

### NPSN Tidak Lengkap atau Salah

**Solusi:**
1. Validasi NPSN di: https://referensi.data.kemendikdasmen.go.id/
2. Pastikan NPSN 8 digit
3. Jika NPSN tidak tersedia, cari manual di website atau hubungi sekolah

### Nama Sekolah Tidak Include Kecamatan

**Masalah**: Data dari website tidak include "Kecamatan [nama]" di nama sekolah

**Solusi**:
Script akan otomatis menambahkan kecamatan ke nama sekolah. Atau edit manual:
```python
school['Nama Sekolah'] = f"{nama_sekolah_asli} Kecamatan {nama_kecamatan}"
```

## Validasi dan Quality Check

Setelah update, lakukan validasi:

### 1. Format JSON Valid
```bash
for file in sd_negeri_*.json; do
    python -m json.tool "$file" > /dev/null && echo "✓ $file" || echo "✗ $file INVALID"
done
```

### 2. Cek Field Wajib
```python
import json

for filename in ['sd_negeri_ajibarang.json', ...]:  # semua file
    with open(filename) as f:
        schools = json.load(f)
    
    for school in schools:
        assert 'No' in school
        assert 'NPSN' in school and len(school['NPSN']) == 8
        assert 'Nama Sekolah' in school
        assert 'Alamat' in school
        assert 'Kelurahan' in school
        assert school['Status'] == 'NEGERI'
```

### 3. Cek Nomor Urut
```python
import json

for filename in ['sd_negeri_ajibarang.json', ...]:
    with open(filename) as f:
        schools = json.load(f)
    
    for idx, school in enumerate(schools, 1):
        assert school['No'] == str(idx), f"Nomor urut salah: {school['No']} != {idx}"
```

## Backup dan Restore

### Backup Otomatis
Script `update_sd_data.py` otomatis membuat backup dengan ekstensi `.json.bak`

### Manual Backup
```bash
# Backup semua file sebelum update
for file in sd_negeri_*.json; do
    cp "$file" "$file.backup.$(date +%Y%m%d)"
done
```

### Restore dari Backup
```bash
# Restore file tertentu
cp sd_negeri_ajibarang.json.bak sd_negeri_ajibarang.json

# Restore semua
for file in sd_negeri_*.json.bak; do
    mv "$file" "${file%.bak}"
done
```

## Commit Changes

Setelah yakin update sudah benar:

```bash
# Review changes
git status
git diff sd_negeri_*.json

# Add dan commit
git add sd_negeri_*.json
git commit -m "Update SD Negeri data from Didaksmen website (Dec 2024)"

# Push ke repository
git push origin main
```

## Kontak dan Support

Jika mengalami kesulitan:

1. **Dinas Pendidikan Kabupaten Banyumas**
   - Website: https://disdik.banyumaskab.go.id
   
2. **Layanan Terpadu Kemendikdasmen**
   - Call Center: 177
   - Website: https://data.kemendikdasmen.go.id
   
3. **BPS Kabupaten Banyumas**
   - Website: https://banyumaskab.bps.go.id
   - Data pendidikan dan statistik

## Catatan Penting

- ⚠️ **Jangan menghapus atau menambah file baru** - hanya replace data yang ada
- ⚠️ **Validasi NPSN** - pastikan NPSN valid dan unik
- ⚠️ **Include kecamatan di nama** - semua nama sekolah harus include "Kecamatan [nama]"
- ⚠️ **Backup dulu** - selalu backup sebelum update
- ⚠️ **Test validasi** - validasi JSON format setelah update

## Changelog

### 2024-12-12
- Initial guide created
- Script `update_sd_data.py` created
- Support untuk mode otomatis dan manual
- Validasi dan error handling

---

**Last Updated**: December 12, 2024
**Maintained by**: Repository Contributors
