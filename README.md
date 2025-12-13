# Hierarchy Export Tool

Tool to export organizational hierarchy from JSON to XLSX format.

## Features

- Exports hierarchical structure to flat XLSX format
- Four columns: `nama_unit` (unit name), `nama_parent` (parent name), `eselon` (echelon level), and `jabatan` (position title)
- Top-level units have empty parent names
- Preserves complete organizational hierarchy
- Includes Indonesian government echelon levels for each organizational unit
- Includes position titles (jabatan) appropriate for each organizational type

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the export script:

```bash
python export_to_xlsx.py
```

This will:
1. Read `hierarchy.json` in the same directory
2. Flatten the hierarchical structure
3. Generate `hierarchy_export.xlsx` with four columns

## Output Format

The generated XLSX file contains:

| nama_unit | nama_parent | eselon | jabatan |
|-----------|-------------|--------|---------|
| Sekretariat Daerah | (empty) | II.b | Sekretaris Daerah |
| Sekretaris Daerah | Sekretariat Daerah | II.a | Sekretaris Daerah |
| Asisten Administrasi Umum | Sekretariat Daerah | II.b | Asisten Sekretaris Daerah |
| Bagian Umum, Protokol dan Komunikasi Pimpinan | Asisten Administrasi Umum | III.a | Kepala Bagian |
| ... | ... | ... | ... |

- **nama_unit**: The name of the organizational unit
- **nama_parent**: The name of the parent unit (empty for top-level units)
- **eselon**: The echelon level (I, II, IIa, IIb, IIIa, IIIb, IV) based on Indonesian government structure
- **jabatan**: The position title appropriate for the unit type (e.g., Sekretaris Daerah, Kepala Dinas, Direktur RSUD)

## Example

Given this hierarchy:

```json
[
  {
    "name": "Sekretariat Daerah",
    "children": [
      {
        "name": "Asisten Administrasi Umum",
        "children": []
      }
    ]
  }
]
```

The output will be:

| nama_unit | nama_parent | eselon | jabatan |
|-----------|-------------|--------|---------|
| Sekretariat Daerah | | II.b | Sekretaris Daerah |
| Asisten Administrasi Umum | Sekretariat Daerah | II.b | Asisten Sekretaris Daerah |
