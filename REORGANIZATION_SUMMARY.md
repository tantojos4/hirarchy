# Summary Reorganisasi Sekolah Dasar Negeri

## Latar Belakang
Berdasarkan permintaan dalam issue, sekolah dasar negeri (SD Negeri) di Kabupaten Banyumas harus diorganisir berdasarkan kecamatan mereka, bukan di bawah Dinas Pendidikan.

**Contoh yang diberikan:**
- Sekolah Dasar Negeri 1 Arcawinangun Kecamatan Purwokerto Timur

## Perubahan yang Dilakukan

### 1. Struktur Sebelum Reorganisasi
```
Dinas Pendidikan
├─ Sekretariat Dinas Pendidikan
├─ Bidang PAUD dan DIKMAS
├─ Bidang Pembinaan SD
├─ Bidang Pembinaan SMP
├─ Bidang Pembinaan Guru dan Tenaga Kependidikan
├─ Sekolah Dasar Negeri 1 Adisana          ← 716 SD Negeri di sini
├─ Sekolah Dasar Negeri 1 Arcawinangun
├─ ... (714 SD Negeri lainnya)
├─ SMP Negeri 1 Ajibarang
└─ ... (SMP dan unit lainnya)
```

### 2. Struktur Setelah Reorganisasi
```
Dinas Pendidikan
├─ Sekretariat Dinas Pendidikan
├─ Bidang PAUD dan DIKMAS
├─ Bidang Pembinaan SD
├─ Bidang Pembinaan SMP
├─ Bidang Pembinaan Guru dan Tenaga Kependidikan
├─ SMP Negeri 1 Ajibarang
└─ ... (SMP dan unit non-SD Negeri lainnya)

Kecamatan Purwokerto Timur
├─ Kelurahan Arcawinangun
├─ Kelurahan Kranji
├─ ... (kelurahan lainnya)
├─ Sekolah Dasar Negeri 1 Arcawinangun    ← SD Negeri sekarang di kecamatan
├─ Sekolah Dasar Negeri 3 Arcawinangun
└─ ... (9 SD Negeri lainnya di kecamatan ini)

Kecamatan Sumbang
├─ Sekolah Dasar Negeri 1 Banteran
├─ Sekolah Dasar Negeri 1 Banjarsari Kulon
└─ ... (27 SD Negeri lainnya)

... (25 kecamatan lainnya dengan SD Negeri mereka)
```

## Hasil Reorganisasi

### Statistik
- **Total SD Negeri:** 716 sekolah
- **Berhasil dipetakan ke kecamatan:** 542 sekolah (75.7%)
- **Belum terpetakan:** 174 sekolah (24.3%)
- **Total kecamatan:** 27 kecamatan
- **Total desa/kelurahan dipetakan:** 310 desa/kelurahan

### Distribusi Per Kecamatan
| No | Kecamatan | Jumlah SD Negeri |
|----|-----------|------------------|
| 1  | Ajibarang | 26 |
| 2  | Banyumas | 21 |
| 3  | Baturraden | 12 |
| 4  | Cilongok | 33 |
| 5  | Gumelar | 27 |
| 6  | Jatilawang | 29 |
| 7  | Kalibagor | 15 |
| 8  | Karanglewas | 8 |
| 9  | Kebasen | 15 |
| 10 | Kedungbanteng | 24 |
| 11 | Kembaran | 18 |
| 12 | Kemranjen | 18 |
| 13 | Lumbir | 34 |
| 14 | Patikraja | 13 |
| 15 | Pekuncen | 29 |
| 16 | Purwojati | 16 |
| 17 | Purwokerto Barat | 15 |
| 18 | Purwokerto Selatan | 23 |
| 19 | Purwokerto Timur | 11 |
| 20 | Purwokerto Utara | 15 |
| 21 | Rawalo | 16 |
| 22 | Sokaraja | 24 |
| 23 | Somagede | 19 |
| 24 | Sumbang | 29 |
| 25 | Sumpiuh | 26 |
| 26 | Tambak | 17 |
| 27 | Wangon | 9 |
| **TOTAL** | **542** |

## Sumber Data

Pemetaan desa/kelurahan ke kecamatan didasarkan pada sumber resmi:

1. **Wikipedia:** [Daftar kecamatan dan kelurahan di Kabupaten Banyumas](https://id.wikipedia.org/wiki/Daftar_kecamatan_dan_kelurahan_di_Kabupaten_Banyumas)
2. **BPS Kabupaten Banyumas:** Data statistik wilayah administrasi
3. **Situs resmi desa/kelurahan** di Kabupaten Banyumas
4. **Penelitian tambahan** untuk desa-desa yang tidak tercantum dalam daftar utama

### Contoh Pemetaan yang Berhasil
- Arcawinangun → Kecamatan Purwokerto Timur ✓
- Adisana → Kecamatan Kebasen ✓
- Banjarsari Kulon → Kecamatan Sumbang ✓
- Cikidang → Kecamatan Cilongok ✓
- Batuanten → Kecamatan Cilongok ✓

## Sekolah yang Belum Terpetakan

174 sekolah belum dapat dipetakan karena nama desa/kelurahan mereka tidak ditemukan dalam data resmi yang tersedia. Sekolah-sekolah ini tetap berada di Dinas Pendidikan untuk verifikasi manual.

Contoh desa yang belum ditemukan:
- Bojong (nama umum, bisa di beberapa kecamatan)
- Ciarus
- Jambu
- Kemiri
- Kotayasa
- Kuntili
- Mengangkang
- Plangkapan
- Rancabanteng
- Rawaheng
- Selanegara
- Sikapat
- Tanggeran
- Windunegara

**Catatan:** Desa-desa ini mungkin:
1. Menggunakan nama lama atau tidak resmi
2. Merupakan bagian dari desa lain (dusun/RW)
3. Ada kesalahan penulisan dalam data sekolah

## Verifikasi

### Fungsi Export Masih Berfungsi
Export ke XLSX telah diuji dan berfungsi dengan baik:
```
Total records: 1506
File: hierarchy_export.xlsx (29K)
```

### Integritas Data
- ✓ Semua unit non-SD Negeri tetap di Dinas Pendidikan
- ✓ Struktur kecamatan tidak berubah
- ✓ Hierarki parent-child terjaga
- ✓ Format JSON valid

## Rekomendasi

1. **Verifikasi Manual:** Sekolah yang belum terpetakan (174 sekolah) perlu diverifikasi secara manual dengan data dari:
   - Dinas Pendidikan Kabupaten Banyumas
   - Kepala sekolah masing-masing
   - Data DAPODIK (Data Pokok Pendidikan)

2. **Update Berkala:** Saat ada penambahan SD Negeri baru atau perubahan nama desa, update mapping perlu dilakukan.

3. **Dokumentasi:** Simpan mapping desa-kecamatan sebagai referensi untuk update di masa depan.

## Kesimpulan

Reorganisasi berhasil memindahkan **542 dari 716 SD Negeri (75.7%)** dari Dinas Pendidikan ke kecamatan masing-masing sesuai dengan lokasi desa/kelurahan mereka. Contoh yang diberikan dalam issue (**SD Negeri 1 Arcawinangun → Kecamatan Purwokerto Timur**) telah berhasil diimplementasikan.

Sisa 174 sekolah memerlukan verifikasi manual karena data desa/kelurahan mereka tidak ditemukan dalam sumber resmi yang tersedia.

---

**Tanggal:** 12 Desember 2025  
**Status:** ✓ Selesai (75.7% berhasil dipetakan)
