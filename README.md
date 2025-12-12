# Hierarchy Export Tool

Tool to export organizational hierarchy from JSON to XLSX format.

## Features

- Exports hierarchical structure to flat XLSX format
- Two columns: `nama_unit` (unit name) and `nama_parent` (parent name)
- Top-level units have empty parent names
- Preserves complete organizational hierarchy

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
3. Generate `hierarchy_export.xlsx` with two columns

## Output Format

The generated XLSX file contains:

| nama_unit | nama_parent |
|-----------|-------------|
| Sekretariat Daerah | (empty) |
| Sekretaris Daerah | Sekretariat Daerah |
| Asisten Administrasi Umum | Sekretariat Daerah |
| Bagian Umum, Protokol dan Komunikasi Pimpinan | Asisten Administrasi Umum |
| ... | ... |

- **nama_unit**: The name of the organizational unit
- **nama_parent**: The name of the parent unit (empty for top-level units)

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

| nama_unit | nama_parent |
|-----------|-------------|
| Sekretariat Daerah | |
| Asisten Administrasi Umum | Sekretariat Daerah |
