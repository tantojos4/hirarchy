# Contoh Output XLSX

Script `export_to_xlsx.py` menghasilkan file Excel dengan format berikut:

## Format Tabel

| nama_unit | nama_parent |
|-----------|-------------|
| Sekretariat Daerah | _(kosong)_ |
| Sekretaris Daerah | Sekretariat Daerah |
| Asisten Administrasi Umum | Sekretariat Daerah |
| Bagian Umum, Protokol dan Komunikasi Pimpinan | Asisten Administrasi Umum |
| Subbagian Tata Usaha Pimpinan, Staf Ahli dan Kepegawaian | Bagian Umum, Protokol dan Komunikasi Pimpinan |

## Penjelasan

- **nama_unit**: Nama unit organisasi
- **nama_parent**: Nama unit induk/parent
  - Jika unit adalah level tertinggi, maka nama_parent kosong
  - Jika unit memiliki parent, maka nama_parent diisi dengan nama unit induknya

## Contoh Lengkap

Dari struktur hierarki:
```
Sekretariat Daerah
├── Asisten Administrasi Umum
│   └── Bagian Umum, Protokol dan Komunikasi Pimpinan
│       └── Subbagian Tata Usaha Pimpinan
└── Asisten Perekonomian dan Pembangunan
```

Akan menghasilkan:

| nama_unit | nama_parent |
|-----------|-------------|
| Sekretariat Daerah | |
| Asisten Administrasi Umum | Sekretariat Daerah |
| Bagian Umum, Protokol dan Komunikasi Pimpinan | Asisten Administrasi Umum |
| Subbagian Tata Usaha Pimpinan | Bagian Umum, Protokol dan Komunikasi Pimpinan |
| Asisten Perekonomian dan Pembangunan | Sekretariat Daerah |

## Statistik

File yang dihasilkan:
- Total unit organisasi: 1,680 record
- Format file: XLSX (Excel)
- Ukuran file: ~32KB
- Nama file output: `hierarchy_export.xlsx`
