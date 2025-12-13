#!/usr/bin/env python3
"""
Script to add 'jabatan' (position/title) field to hierarchy.json.

This script adds appropriate position titles based on the organization type
according to Indonesian government organizational structure.

Usage:
    python add_jabatan_field.py
"""

import json
import sys
from pathlib import Path


def determine_jabatan(name: str, eselon: str, parent_name: str = "") -> str:
    """
    Determine the appropriate jabatan (position title) based on organization name and type.
    
    Args:
        name: Organization/unit name
        eselon: Echelon level
        parent_name: Parent organization name (for context)
    
    Returns:
        Appropriate jabatan title
    """
    name_lower = name.lower()
    
    # Top-level organization titles (Eselon II.b and higher)
    if eselon in ["II.a", "II.b", "I"]:
        # Sekretariat Daerah
        if "sekretariat daerah" in name_lower:
            return "Sekretaris Daerah"
        
        # Sekretariat DPRD
        if "sekretariat dprd" in name_lower:
            return "Sekretaris DPRD"
        
        # BPBD - Kepala Pelaksana BPBD
        if "badan penanggulangan bencana daerah" in name_lower or "bpbd" in name_lower:
            return "Kepala Pelaksana BPBD"
        
        # Other Badan (agencies)
        if name.startswith("Badan "):
            return "Kepala Badan"
        
        # Dinas (departments)
        if name.startswith("Dinas ") or name.startswith("DINAS "):
            return "Kepala Dinas"
        
        # Inspektorat
        if "inspektorat" in name_lower:
            return "Inspektur Daerah"
        
        # Satpol PP
        if "satpol pp" in name_lower or "satuan polisi pamong praja" in name_lower:
            return "Kepala Satpol PP"
        
        # Kecamatan
        if name.startswith("Kecamatan "):
            return "Camat"
        
        # RSUD (Regional Public Hospital)
        if "rsud" in name_lower or "rumah sakit umum daerah" in name_lower:
            return "Direktur RSUD"
        
        # Asisten (Assistant)
        if name.startswith("Asisten "):
            return "Asisten Sekretaris Daerah"
    
    # Eselon III (mid-level)
    if eselon in ["III.a", "III.b"]:
        # Kecamatan (sub-district)
        if name.startswith("Kecamatan "):
            return "Camat"
        
        # Sekretariat
        if "sekretariat" in name_lower and ("daerah" not in name_lower):
            return "Sekretaris"
        
        # Bagian (Section)
        if name.startswith("Bagian "):
            return "Kepala Bagian"
        
        # Bidang (Division)
        if name.startswith("Bidang "):
            return "Kepala Bidang"
        
        # Klinik
        if "klinik" in name_lower:
            return "Kepala Klinik"
        
        # RSUD at this level
        if "rsud" in name_lower or "rumah sakit" in name_lower:
            return "Direktur RSUD"
        
        # Puskesmas (Community Health Center)
        if "puskesmas" in name_lower:
            return "Kepala Puskesmas"
        
        # Laboratorium
        if "laboratorium" in name_lower:
            return "Kepala Laboratorium"
        
        # Kantor (Office)
        if "kantor" in name_lower:
            return "Kepala Kantor"
        
        # Kelurahan (Urban Village)
        if "kelurahan" in name_lower:
            return "Lurah"
    
    # Eselon IV (lower level)
    if eselon in ["IV.a", "IV.b"]:
        # Subbagian (Sub-section)
        if name.startswith("Subbagian ") or name.startswith("Sub Bagian "):
            return "Kepala Subbagian"
        
        # Subbidang (Sub-division)
        if name.startswith("Subbidang ") or name.startswith("Sub Bidang "):
            return "Kepala Subbidang"
        
        # Seksi (Section)
        if name.startswith("Seksi "):
            return "Kepala Seksi"
        
        # Desa (Village)
        if "desa" in name_lower or name.startswith("Desa "):
            return "Kepala Desa"
    
    # Default fallback based on organizational hierarchy
    if eselon == "I":
        return "Pimpinan"
    elif eselon in ["II.a", "II.b"]:
        return "Kepala"
    elif eselon in ["III.a", "III.b"]:
        return "Kepala"
    elif eselon in ["IV.a", "IV.b"]:
        return "Kepala"
    
    # If no eselon, return generic title
    return "Pejabat"


def add_jabatan_recursive(data, parent_name=""):
    """
    Recursively add jabatan field to all nodes in the hierarchy.
    
    Args:
        data: List of organizational units or single unit
        parent_name: Name of parent organization
    
    Returns:
        Modified data with jabatan field added
    """
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'name' in item:
                # Add or update jabatan field
                name = item['name']
                eselon = item.get('eselon', '')
                jabatan = determine_jabatan(name, eselon, parent_name)
                item['jabatan'] = jabatan
                
                # Recursively process children
                if 'children' in item and isinstance(item['children'], list):
                    add_jabatan_recursive(item['children'], item['name'])
    
    return data


def main():
    """Main function to add jabatan field to hierarchy.json."""
    # Read hierarchy.json
    json_file = Path(__file__).parent / "hierarchy.json"
    
    if not json_file.exists():
        print(f"Error: {json_file} not found!")
        sys.exit(1)
    
    print(f"Reading {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        hierarchy_data = json.load(f)
    
    print(f"Processing {len(hierarchy_data)} top-level organizations...")
    
    # Add jabatan field to all nodes
    modified_data = add_jabatan_recursive(hierarchy_data)
    
    # Create backup
    backup_file = json_file.with_suffix('.json.bak')
    print(f"Creating backup at {backup_file}...")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(hierarchy_data, f, ensure_ascii=False, indent=2)
    
    # Write modified data
    print(f"Writing updated data to {json_file}...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(modified_data, f, ensure_ascii=False, indent=2)
    
    print("\n✓ Successfully added jabatan field to hierarchy.json")
    
    # Show some examples
    print("\nExamples of added jabatan:")
    for org in modified_data[:5]:
        print(f"  - {org['name']}: {org.get('jabatan', 'N/A')}")


if __name__ == "__main__":
    main()
