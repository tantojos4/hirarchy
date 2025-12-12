#!/usr/bin/env python3
"""
Script to fetch and update SD Negeri data from Didaksmen website.

This script fetches current school data from the official government education database
and updates the JSON files for each kecamatan in Banyumas.

Data source: https://referensi.data.kemendikdasmen.go.id/
Alternative: https://data.kemendikdasmen.go.id/

Requirements:
    pip install requests beautifulsoup4 pandas

Usage:
    python update_sd_data.py
    
Note: If websites are blocked, use manual mode by downloading CSV/Excel from:
    https://data.kemendikdasmen.go.id/data-induk
"""

import json
import sys
import os
from pathlib import Path
from typing import List, Dict, Any
import argparse

# Kecamatan mapping: filename -> display name
KECAMATAN_MAP = {
    "ajibarang": "Ajibarang",
    "banyumas": "Banyumas",
    "baturaden": "Baturaden",
    "cilongok": "Cilongok",
    "gumelar": "Gumelar",
    "jatilawang": "Jatilawang",
    "kalibagor": "Kalibagor",
    "karanglewas": "Karanglewas",
    "kebasen": "Kebasen",
    "kedung_banteng": "Kedungbanteng",
    "kembaran": "Kembaran",
    "kemranjen": "Kemranjen",
    "lumbir": "Lumbir",
    "patikraja": "Patikraja",
    "pekuncen": "Pekuncen",
    "purwojati": "Purwojati",
    "purwokerto_barat": "Purwokerto Barat",
    "purwokerto_selatan": "Purwokerto Selatan",
    "purwokerto_timur": "Purwokerto Timur",
    "purwokerto_utara": "Purwokerto Utara",
    "rawalo": "Rawalo",
    "sokaraja": "Sokaraja",
    "somagede": "Somagede",
    "sumbang": "Sumbang",
    "sumpiuh": "Sumpiuh",
    "tambak": "Tambak",
    "wangon": "Wangon",
}


def fetch_schools_from_website(kecamatan_name: str) -> List[Dict[str, Any]]:
    """
    Fetch school data from didaksmen website for a specific kecamatan.
    
    Args:
        kecamatan_name: Name of the kecamatan
        
    Returns:
        List of school dictionaries with keys: No, NPSN, Nama Sekolah, Alamat, Kelurahan, Status
        
    Note:
        ⚠️ INCOMPLETE IMPLEMENTATION ⚠️
        This function is a TEMPLATE and requires website-specific implementation.
        
        The actual website structure needs to be inspected and parsing logic implemented.
        Until then, this function will return empty list and you should use --manual mode.
        
        To complete implementation:
        1. Access the website and inspect the HTML structure
        2. Identify the table/element containing school data
        3. Parse the NPSN, Nama, Alamat, Kelurahan fields
        4. Filter for SD Negeri in the specific kecamatan
        5. Format according to required JSON structure
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        
        # Base URL pattern for didaksmen
        # Example: https://referensi.data.kemendikdasmen.go.id/pendidikan/dikdas/030211/3/all/5/all
        # Where 030211 is kode wilayah for Banyumas
        
        # Kode wilayah mapping (this needs to be filled with actual codes)
        KODE_WILAYAH = "030211"  # Kabupaten Banyumas, Jawa Tengah
        
        print(f"⚠️  Attempting to fetch data for {kecamatan_name}...")
        print(f"⚠️  Note: Automatic fetching not fully implemented.")
        print(f"⚠️  Recommendation: Use --manual mode with downloaded CSV/Excel")
        
        # This is a template - actual implementation depends on website structure
        # Steps needed:
        # 1. GET the page with proper headers
        # 2. Parse the HTML table
        # 3. Extract NPSN, Nama Sekolah, Alamat, Kelurahan
        # 4. Filter for the specific kecamatan
        
        url = f"https://referensi.data.kemendikdasmen.go.id/pendidikan/dikdas/{KODE_WILAYAH}/3/all/5/all"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # IMPLEMENTATION NEEDED: Parse website and extract school data
        # The code below is incomplete and needs actual parsing logic
        
        # response = requests.get(url, headers=headers, timeout=30)
        # response.raise_for_status()
        # soup = BeautifulSoup(response.content, 'html.parser')
        # schools = parse_school_table(soup, kecamatan_name)  # Needs implementation
        
        schools = []  # Empty until implementation is complete
        
        print(f"  ℹ️  Automatic fetching returned {len(schools)} schools")
        print(f"  ℹ️  Please use --manual mode with downloaded data file")
        return schools
        
    except ImportError:
        print("Error: requests and beautifulsoup4 are required.")
        print("Install with: pip install requests beautifulsoup4")
        return []
    except Exception as e:
        print(f"Error fetching data: {e}")
        print(f"Recommendation: Use --manual mode instead")
        return []


def load_manual_data(csv_file: str, kecamatan_name: str) -> List[Dict[str, Any]]:
    """
    Load school data from a manually downloaded CSV/Excel file.
    
    Args:
        csv_file: Path to the CSV/Excel file
        kecamatan_name: Name of the kecamatan to filter
        
    Returns:
        List of school dictionaries
    """
    try:
        import pandas as pd
        
        print(f"Loading data from {csv_file}...")
        
        # Read the file
        if csv_file.endswith('.csv'):
            df = pd.read_csv(csv_file)
        elif csv_file.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(csv_file)
        else:
            print("Error: Unsupported file format. Use CSV or Excel.")
            return []
        
        # Filter for SD Negeri in the specific kecamatan
        # Adjust column names based on actual file structure
        df_filtered = df[
            (df['Bentuk Pendidikan'].str.contains('SD', case=False, na=False)) &
            (df['Status Sekolah'].str.contains('NEGERI', case=False, na=False)) &
            (df['Kecamatan'].str.contains(kecamatan_name, case=False, na=False))
        ]
        
        # Convert to expected format
        schools = []
        for idx, row in df_filtered.iterrows():
            school = {
                "No": str(idx + 1),
                "NPSN": str(row.get('NPSN', '')),
                "Nama Sekolah": row.get('Nama Sekolah', ''),
                "Alamat": row.get('Alamat', ''),
                "Kelurahan": row.get('Desa/Kelurahan', ''),
                "Status": "NEGERI"
            }
            schools.append(school)
        
        print(f"  Found {len(schools)} schools for {kecamatan_name}")
        return schools
        
    except ImportError:
        print("Error: pandas is required for manual mode.")
        print("Install with: pip install pandas openpyxl")
        return []
    except Exception as e:
        print(f"Error loading manual data: {e}")
        return []


def validate_school_data(school: Dict[str, Any]) -> bool:
    """
    Validate that a school record has all required fields.
    
    Args:
        school: School dictionary
        
    Returns:
        True if valid, False otherwise
    """
    required_fields = ['No', 'NPSN', 'Nama Sekolah', 'Alamat', 'Kelurahan', 'Status']
    
    for field in required_fields:
        if field not in school or not school[field]:
            return False
    
    return True


def update_json_file(kecamatan_key: str, schools: List[Dict[str, Any]], dry_run: bool = False):
    """
    Update the JSON file for a specific kecamatan with new school data.
    
    Args:
        kecamatan_key: Kecamatan key (filename without extension)
        schools: List of school dictionaries
        dry_run: If True, don't actually write files
    """
    filename = f"sd_negeri_{kecamatan_key}.json"
    filepath = Path(__file__).parent / filename
    
    if not schools:
        print(f"  Skipping {filename}: No data")
        return
    
    # Validate all schools
    valid_schools = [s for s in schools if validate_school_data(s)]
    invalid_count = len(schools) - len(valid_schools)
    
    if invalid_count > 0:
        print(f"  Warning: {invalid_count} invalid records skipped")
    
    if not valid_schools:
        print(f"  Skipping {filename}: No valid data")
        return
    
    # Re-number schools
    for idx, school in enumerate(valid_schools, 1):
        school['No'] = str(idx)
    
    if dry_run:
        print(f"  [DRY RUN] Would update {filename} with {len(valid_schools)} schools")
        return
    
    # Backup existing file
    if filepath.exists():
        backup_path = filepath.with_suffix('.json.bak')
        import shutil
        shutil.copy2(filepath, backup_path)
        print(f"  Backed up to {backup_path.name}")
    
    # Write new data
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(valid_schools, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ Updated {filename} with {len(valid_schools)} schools")


def main():
    parser = argparse.ArgumentParser(
        description='Update SD Negeri data from Didaksmen website'
    )
    parser.add_argument(
        '--manual',
        type=str,
        help='Path to manually downloaded CSV/Excel file'
    )
    parser.add_argument(
        '--kecamatan',
        type=str,
        help='Update only specific kecamatan (e.g., ajibarang)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be updated without actually updating'
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("SD Negeri Data Update Script")
    print("=" * 70)
    print()
    
    # Determine which kecamatan to process
    if args.kecamatan:
        if args.kecamatan not in KECAMATAN_MAP:
            print(f"Error: Unknown kecamatan '{args.kecamatan}'")
            print(f"Available: {', '.join(KECAMATAN_MAP.keys())}")
            sys.exit(1)
        kecamatan_list = [(args.kecamatan, KECAMATAN_MAP[args.kecamatan])]
    else:
        kecamatan_list = list(KECAMATAN_MAP.items())
    
    print(f"Processing {len(kecamatan_list)} kecamatan(s)...")
    print()
    
    # Process each kecamatan
    for kec_key, kec_name in kecamatan_list:
        print(f"Processing: {kec_name}")
        
        if args.manual:
            # Load from manual file
            schools = load_manual_data(args.manual, kec_name)
        else:
            # Fetch from website
            schools = fetch_schools_from_website(kec_name)
            
            if not schools:
                print(f"  No data fetched. Consider using --manual mode.")
                print(f"  Download data from: https://data.kemendikdasmen.go.id/data-induk")
                continue
        
        # Update the JSON file
        update_json_file(kec_key, schools, args.dry_run)
        print()
    
    print("=" * 70)
    print("Update complete!")
    print()
    
    if args.dry_run:
        print("This was a dry run. No files were modified.")
        print("Remove --dry-run to apply changes.")
    else:
        print("Backup files (.json.bak) have been created.")
        print("Review the changes and commit if everything looks good.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
