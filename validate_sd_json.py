#!/usr/bin/env python3
"""
Validation script for SD Negeri JSON files.

This script validates that all JSON files:
1. Are valid JSON format
2. Have all required fields
3. Have proper data types and formats
4. Have sequential numbering
5. Have valid NPSN format

Usage:
    python validate_sd_json.py
    python validate_sd_json.py --file sd_negeri_ajibarang.json
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
import re
import argparse


def validate_npsn(npsn: str) -> Tuple[bool, str]:
    """
    Validate NPSN format.
    
    Args:
        npsn: NPSN string
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not npsn:
        return False, "NPSN is empty"
    
    if not isinstance(npsn, str):
        return False, f"NPSN must be string, got {type(npsn)}"
    
    if len(npsn) != 8:
        return False, f"NPSN must be 8 digits, got {len(npsn)}"
    
    if not npsn.isdigit():
        return False, f"NPSN must contain only digits, got '{npsn}'"
    
    return True, ""


def validate_school_record(school: Dict[str, Any], expected_no: int) -> List[str]:
    """
    Validate a single school record.
    
    Args:
        school: School dictionary
        expected_no: Expected sequential number
        
    Returns:
        List of error messages (empty if valid)
    """
    errors = []
    
    # Check required fields exist
    required_fields = ['No', 'NPSN', 'Nama Sekolah', 'Alamat', 'Kelurahan', 'Status']
    for field in required_fields:
        if field not in school:
            errors.append(f"Missing required field: {field}")
    
    # Validate No field
    if 'No' in school:
        if not isinstance(school['No'], str):
            errors.append(f"'No' must be string, got {type(school['No'])}")
        elif school['No'] != str(expected_no):
            errors.append(f"'No' should be '{expected_no}', got '{school['No']}'")
    
    # Validate NPSN
    if 'NPSN' in school:
        is_valid, error_msg = validate_npsn(school['NPSN'])
        if not is_valid:
            errors.append(f"Invalid NPSN: {error_msg}")
    
    # Validate Nama Sekolah
    if 'Nama Sekolah' in school:
        if not school['Nama Sekolah']:
            errors.append("'Nama Sekolah' is empty")
        elif not isinstance(school['Nama Sekolah'], str):
            errors.append(f"'Nama Sekolah' must be string")
        elif 'Kecamatan' not in school['Nama Sekolah']:
            errors.append(f"'Nama Sekolah' should include 'Kecamatan [nama]': {school['Nama Sekolah']}")
    
    # Validate Alamat
    if 'Alamat' in school:
        if not school['Alamat']:
            errors.append("'Alamat' is empty")
        elif not isinstance(school['Alamat'], str):
            errors.append(f"'Alamat' must be string")
    
    # Validate Kelurahan
    if 'Kelurahan' in school:
        if not school['Kelurahan']:
            errors.append("'Kelurahan' is empty")
        elif not isinstance(school['Kelurahan'], str):
            errors.append(f"'Kelurahan' must be string")
    
    # Validate Status
    if 'Status' in school:
        if school['Status'] != 'NEGERI':
            errors.append(f"'Status' must be 'NEGERI', got '{school['Status']}'")
    
    return errors


def validate_json_file(filepath: Path) -> Tuple[bool, List[str], Dict[str, Any]]:
    """
    Validate a single JSON file.
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        Tuple of (is_valid, list of errors, stats dict)
    """
    errors = []
    stats = {
        'total_schools': 0,
        'valid_schools': 0,
        'invalid_schools': 0,
        'duplicate_npsn': [],
    }
    
    # Check file exists
    if not filepath.exists():
        return False, [f"File not found: {filepath}"], stats
    
    # Try to load JSON
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON format: {e}"], stats
    except Exception as e:
        return False, [f"Error reading file: {e}"], stats
    
    # Check data is a list
    if not isinstance(data, list):
        return False, ["JSON root must be an array"], stats
    
    if len(data) == 0:
        return False, ["JSON array is empty"], stats
    
    stats['total_schools'] = len(data)
    
    # Track NPSN for duplicates
    npsn_map = {}
    
    # Validate each school
    for idx, school in enumerate(data, 1):
        if not isinstance(school, dict):
            errors.append(f"Record {idx}: Must be an object, got {type(school)}")
            stats['invalid_schools'] += 1
            continue
        
        # Validate this school
        school_errors = validate_school_record(school, idx)
        
        if school_errors:
            errors.append(f"Record {idx}:")
            for err in school_errors:
                errors.append(f"  - {err}")
            stats['invalid_schools'] += 1
        else:
            stats['valid_schools'] += 1
        
        # Check for duplicate NPSN
        if 'NPSN' in school:
            npsn = school['NPSN']
            if npsn in npsn_map:
                duplicate_info = f"NPSN {npsn} appears in records {npsn_map[npsn]} and {idx}"
                stats['duplicate_npsn'].append(duplicate_info)
                if duplicate_info not in errors:
                    errors.append(f"Duplicate NPSN found: {duplicate_info}")
            else:
                npsn_map[npsn] = idx
    
    is_valid = len(errors) == 0
    return is_valid, errors, stats


def print_validation_result(filename: str, is_valid: bool, errors: List[str], stats: Dict[str, Any]):
    """
    Print validation result for a file.
    """
    status_symbol = "✓" if is_valid else "✗"
    status_text = "VALID" if is_valid else "INVALID"
    
    print(f"\n{status_symbol} {filename}: {status_text}")
    print(f"   Total schools: {stats['total_schools']}")
    print(f"   Valid: {stats['valid_schools']}")
    
    if stats['invalid_schools'] > 0:
        print(f"   Invalid: {stats['invalid_schools']}")
    
    if stats['duplicate_npsn']:
        print(f"   Duplicates: {len(stats['duplicate_npsn'])}")
    
    if not is_valid and errors:
        print(f"\n   Errors ({len(errors)}):")
        for error in errors[:10]:  # Show first 10 errors
            print(f"   {error}")
        
        if len(errors) > 10:
            print(f"   ... and {len(errors) - 10} more errors")


def main():
    parser = argparse.ArgumentParser(
        description='Validate SD Negeri JSON files'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Validate specific file (default: all sd_negeri_*.json files)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed validation information'
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("SD Negeri JSON Validation")
    print("=" * 70)
    
    # Determine which files to validate
    base_path = Path(__file__).parent
    
    if args.file:
        files = [base_path / args.file]
    else:
        files = sorted(base_path.glob('sd_negeri_*.json'))
    
    if not files:
        print("\nNo JSON files found to validate.")
        sys.exit(1)
    
    print(f"\nValidating {len(files)} file(s)...\n")
    
    # Validate each file
    all_valid = True
    total_stats = {
        'files': 0,
        'valid_files': 0,
        'invalid_files': 0,
        'total_schools': 0,
        'valid_schools': 0,
        'invalid_schools': 0,
    }
    
    for filepath in files:
        is_valid, errors, stats = validate_json_file(filepath)
        print_validation_result(filepath.name, is_valid, errors, stats)
        
        total_stats['files'] += 1
        total_stats['total_schools'] += stats['total_schools']
        total_stats['valid_schools'] += stats['valid_schools']
        total_stats['invalid_schools'] += stats['invalid_schools']
        
        if is_valid:
            total_stats['valid_files'] += 1
        else:
            total_stats['invalid_files'] += 1
            all_valid = False
    
    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Files validated: {total_stats['files']}")
    print(f"  ✓ Valid: {total_stats['valid_files']}")
    if total_stats['invalid_files'] > 0:
        print(f"  ✗ Invalid: {total_stats['invalid_files']}")
    print(f"\nSchool records: {total_stats['total_schools']}")
    print(f"  ✓ Valid: {total_stats['valid_schools']}")
    if total_stats['invalid_schools'] > 0:
        print(f"  ✗ Invalid: {total_stats['invalid_schools']}")
    
    print("\n" + "=" * 70)
    
    if all_valid:
        print("✓ All files are valid!")
        sys.exit(0)
    else:
        print("✗ Some files have validation errors.")
        print("Please fix the errors and run validation again.")
        sys.exit(1)


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
