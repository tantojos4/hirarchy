# Summary Reorganisasi Sekolah Dasar Negeri

## Perubahan Terbaru

Berdasarkan feedback, struktur telah diubah sehingga:
- **Sekolah BUKAN sebagai children dari kecamatan**
- **Nama sekolah langsung menyertakan kecamatan**
- **Semua sekolah tetap di bawah Dinas Pendidikan**

## Struktur Akhir

### Format Nama Sekolah
```
Sekolah Dasar Negeri [nomor] [nama desa] Kecamatan [nama kecamatan]
```

**Contoh:**
- `Sekolah Dasar Negeri 1 Arcawinangun Kecamatan Purwokerto Timur`
- `Sekolah Dasar Negeri 3 Arcawinangun Kecamatan Purwokerto Timur`
- `Sekolah Dasar Negeri 1 Ciberung Kecamatan Ajibarang`

### Hierarki dalam JSON
```
Dinas Pendidikan
├─ Sekretariat Dinas Pendidikan
├─ Bidang PAUD dan DIKMAS
├─ Bidang Pembinaan SD
├─ Bidang Pembinaan SMP
├─ Bidang Pembinaan Guru dan Tenaga Kependidikan
├─ Sekolah Dasar Negeri 1 Arcawinangun Kecamatan Purwokerto Timur
├─ Sekolah Dasar Negeri 3 Arcawinangun Kecamatan Purwokerto Timur
├─ Sekolah Dasar Negeri 4 Arcawinangun Kecamatan Purwokerto Timur
├─ Sekolah Dasar Negeri 5 Arcawinangun Kecamatan Purwokerto Timur
├─ ... (538 SD Negeri lainnya dengan kecamatan di nama)
├─ SMP Negeri 1 Ajibarang
└─ ... (SMP dan unit lainnya)
```

**Catatan Penting:**
- Sekolah TIDAK menjadi children dari Kecamatan
- Sekolah TIDAK menjadi parent dari apapun
- Sekolah adalah direct children dari Dinas Pendidikan
- Informasi kecamatan ada di nama sekolah itu sendiri

## Statistik

- **Total SD Negeri yang direname:** 542 sekolah
- **Format:** Semua include "Kecamatan [nama]" di akhir nama
- **Lokasi:** Semua tetap di Dinas Pendidikan
- **Kecamatan:** Tidak memiliki sekolah sebagai children

## Contoh Data dalam JSON

```json
{
  "name": "Dinas Pendidikan",
  "children": [
    {
      "name": "Sekretariat Dinas Pendidikan",
      "children": []
    },
    {
      "name": "Sekolah Dasar Negeri 1 Arcawinangun Kecamatan Purwokerto Timur",
      "children": []
    }
  ]
}
```

## Kecamatan yang Tercantum dalam Nama Sekolah

Total 27 kecamatan yang namanya muncul dalam nama sekolah:

1. Ajibarang (26 sekolah)
2. Banyumas (21 sekolah)
3. Baturraden (12 sekolah)
4. Cilongok (33 sekolah)
5. Gumelar (27 sekolah)
6. Jatilawang (29 sekolah)
7. Kalibagor (15 sekolah)
8. Karanglewas (8 sekolah)
9. Kebasen (15 sekolah)
10. Kedungbanteng (24 sekolah)
11. Kembaran (18 sekolah)
12. Kemranjen (18 sekolah)
13. Lumbir (34 sekolah)
14. Patikraja (13 sekolah)
15. Pekuncen (29 sekolah)
16. Purwojati (16 sekolah)
17. Purwokerto Barat (15 sekolah)
18. Purwokerto Selatan (23 sekolah)
19. Purwokerto Timur (11 sekolah)
20. Purwokerto Utara (15 sekolah)
21. Rawalo (16 sekolah)
22. Sokaraja (24 sekolah)
23. Somagede (19 sekolah)
24. Sumbang (29 sekolah)
25. Sumpiuh (26 sekolah)
26. Tambak (17 sekolah)
27. Wangon (9 sekolah)

**Total:** 542 sekolah

---

**Tanggal:** 12 Desember 2025  
**Status:** ✓ Selesai - Sekolah dengan nama kecamatan, bukan sebagai parent/child
