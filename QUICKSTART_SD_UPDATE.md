# 🚀 Quick Start: Update SD Negeri Data

This guide helps you quickly update the SD Negeri (Public Elementary School) data for Kabupaten Banyumas.

## ⚡ TL;DR (Too Long; Didn't Read)

```bash
# 1. Download data from didaksmen website
#    → https://data.kemendikdasmen.go.id/data-induk
#    Filter: Jawa Tengah → Banyumas → SD → Negeri

# 2. Update the files
python update_sd_data.py --manual data_banyumas.csv --dry-run
python update_sd_data.py --manual data_banyumas.csv

# 3. Validate
python validate_sd_json.py

# 4. Commit
git add sd_negeri_*.json
git commit -m "Update SD Negeri data from Didaksmen"
```

## 📚 Full Documentation

| Document | Purpose |
|----------|---------|
| [**UPDATE_SD_DATA_GUIDE.md**](UPDATE_SD_DATA_GUIDE.md) | Complete step-by-step guide (Indonesian) |
| [**SUMMARY_SD_UPDATE.md**](SUMMARY_SD_UPDATE.md) | Project status and summary |
| **This file** | Quick reference |

## 🛠️ Available Tools

### 1. `update_sd_data.py` - Update Data
Updates SD Negeri JSON files with data from didaksmen.

```bash
# Show help
python update_sd_data.py --help

# Manual mode (recommended)
python update_sd_data.py --manual data.csv

# Test without changing files
python update_sd_data.py --manual data.csv --dry-run

# Update specific kecamatan only
python update_sd_data.py --manual data.csv --kecamatan ajibarang
```

### 2. `validate_sd_json.py` - Validate Data
Validates all SD Negeri JSON files for correctness.

```bash
# Validate all files
python validate_sd_json.py

# Validate specific file
python validate_sd_json.py --file sd_negeri_ajibarang.json

# Verbose output
python validate_sd_json.py --verbose
```

## 📋 What Gets Validated?

- ✅ Valid JSON syntax
- ✅ Required fields present (No, NPSN, Nama Sekolah, Alamat, Kelurahan, Status)
- ✅ NPSN is 8 digits
- ✅ Sequential numbering (1, 2, 3, ...)
- ✅ No duplicate NPSN
- ✅ School name includes "Kecamatan [nama]"
- ✅ Status is "NEGERI"

## 🎯 Current Status

✅ **All 27 files are validated and ready**
- 748 school records
- 100% data quality
- All fields correct

⚠️ **To update with fresh data**: Follow steps above

## 📁 Files Being Updated

27 JSON files for each kecamatan:
- `sd_negeri_ajibarang.json` (33 schools)
- `sd_negeri_banyumas.json` (31 schools)
- `sd_negeri_baturaden.json` (22 schools)
- ... and 24 more files
- **Total: 748 schools**

## 🔍 Example: Update One Kecamatan

```bash
# Step 1: Download data for Ajibarang from website

# Step 2: Update just Ajibarang (dry run first)
python update_sd_data.py \
  --manual ajibarang_data.csv \
  --kecamatan ajibarang \
  --dry-run

# Step 3: Apply changes
python update_sd_data.py \
  --manual ajibarang_data.csv \
  --kecamatan ajibarang

# Step 4: Validate
python validate_sd_json.py --file sd_negeri_ajibarang.json
```

## ⚙️ Installation

Python 3.6+ required. Install dependencies:

```bash
# For manual mode (CSV/Excel)
pip install pandas openpyxl

# For automatic mode (if website accessible)
pip install requests beautifulsoup4
```

## 🆘 Common Issues

### Issue: Website blocked
**Solution**: Download CSV from website manually, then use `--manual` mode

### Issue: Column names don't match
**Solution**: Edit `update_sd_data.py` to map your CSV columns correctly

### Issue: Validation fails
**Solution**: Check error messages, fix data, validate again

## 🌐 Data Sources

**Primary**:
- https://data.kemendikdasmen.go.id/data-induk
- Filter: Provinsi=Jawa Tengah, Kabupaten=Banyumas, Jenjang=SD, Status=Negeri
- Download as CSV or Excel

**Alternative**:
- https://data.banyumaskab.go.id (Open Data Banyumas)
- Contact Dinas Pendidikan Kabupaten Banyumas

## 📊 Data Format

Each JSON file contains an array of schools:

```json
[
  {
    "No": "1",
    "NPSN": "20302232",
    "Nama Sekolah": "Sekolah Dasar Negeri 1 Banjarsari Kecamatan Ajibarang",
    "Alamat": "Banjarsari , Rt. 06 / Rw. 1",
    "Kelurahan": "Banjarsari",
    "Status": "NEGERI"
  }
]
```

## ✅ Checklist

Before considering update complete:

- [ ] Downloaded latest data from didaksmen
- [ ] Ran update script successfully
- [ ] Validated all files: `python validate_sd_json.py`
- [ ] All validations pass
- [ ] Reviewed changes: `git diff sd_negeri_*.json`
- [ ] Backed up old data (automatic with script)
- [ ] Committed changes to git
- [ ] Pushed to repository

## 📞 Need Help?

1. Read [UPDATE_SD_DATA_GUIDE.md](UPDATE_SD_DATA_GUIDE.md) for detailed instructions
2. Check [SUMMARY_SD_UPDATE.md](SUMMARY_SD_UPDATE.md) for project status
3. Contact Dinas Pendidikan Kabupaten Banyumas
4. Call Kemendikdasmen: 177

## 🔄 Update Frequency

**Recommended**:
- Annually before new school year (July)
- When new schools open
- When data quality issues reported

---

**Last Updated**: December 12, 2024  
**Status**: ✅ Tools Ready  
**Action Required**: Download fresh data and run update script
