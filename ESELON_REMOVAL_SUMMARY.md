# Eselon Removal Summary

## Problem
Schools (Sekolah) and health centers (Puskesmas) should not have echelon (eselon) levels as they are not part of the structural bureaucracy hierarchy. Previously, all 861 Puskesmas and Sekolah entries in `hierarchy.json` had "eselon: III.b" assigned to them.

## Solution
Created and executed `remove_eselon_sekolah_puskesmas.py` script to remove the eselon field from all Puskesmas and Sekolah entries in `hierarchy.json`.

## Results

### Removed Eselon from hierarchy.json
- **Total entries modified**: 861
- **Puskesmas entries**: Health centers across various districts
- **Sekolah entries**: Schools including:
  - Sekolah Menengah Pertama Negeri (Junior High Schools)
  - Sekolah Dasar Negeri (Elementary Schools) in hierarchy.json

### Schools Without Eselon (SD Negeri Files)
Found **748 Elementary Schools (SD Negeri)** in 27 separate JSON files that never had eselon fields:

| File | Number of Schools |
|------|-------------------|
| sd_negeri_ajibarang.json | 33 |
| sd_negeri_banyumas.json | 31 |
| sd_negeri_baturaden.json | 22 |
| sd_negeri_cilongok.json | 43 |
| sd_negeri_gumelar.json | 32 |
| sd_negeri_jatilawang.json | 36 |
| sd_negeri_kalibagor.json | 21 |
| sd_negeri_karanglewas.json | 21 |
| sd_negeri_kebasen.json | 28 |
| sd_negeri_kedung_banteng.json | 26 |
| sd_negeri_kembaran.json | 28 |
| sd_negeri_kemranjen.json | 32 |
| sd_negeri_lumbir.json | 34 |
| sd_negeri_patikraja.json | 26 |
| sd_negeri_pekuncen.json | 34 |
| sd_negeri_purwojati.json | 20 |
| sd_negeri_purwokerto_barat.json | 18 |
| sd_negeri_purwokerto_selatan.json | 21 |
| sd_negeri_purwokerto_timur.json | 19 |
| sd_negeri_purwokerto_utara.json | 15 |
| sd_negeri_rawalo.json | 22 |
| sd_negeri_sokaraja.json | 28 |
| sd_negeri_somagede.json | 19 |
| sd_negeri_sumbang.json | 37 |
| sd_negeri_sumpiuh.json | 30 |
| sd_negeri_tambak.json | 27 |
| sd_negeri_wangon.json | 45 |
| **TOTAL** | **748** |

These SD Negeri files contain basic school information (NPSN, Nama Sekolah, Alamat, Kelurahan, Status) and correctly do not include eselon fields as they are educational institutions, not bureaucratic positions.

## Verification
After modification:
- ✅ All 861 Puskesmas and Sekolah entries in hierarchy.json now have NO eselon field
- ✅ All 748 SD Negeri schools in separate files continue to have NO eselon field (as expected)
- ✅ Other organizational units (Dinas, Badan, etc.) retain their appropriate eselon levels

## Script Usage
To apply this change:
```bash
python3 remove_eselon_sekolah_puskesmas.py
```

The script:
1. Reads `hierarchy.json`
2. Recursively finds all entries with "Puskesmas" or "Sekolah" in the name
3. Removes the "eselon" field from these entries
4. Writes the updated hierarchy back to `hierarchy.json`
