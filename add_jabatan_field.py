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
        Appropriate jabatan title with full unit name
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
        
        # Other Badan (agencies) - include full name
        if name.startswith("Badan "):
            return f"Kepala {name}"
        
        # Dinas (departments) - include full name
        if name.startswith("Dinas ") or name.startswith("DINAS "):
            return f"Kepala {name}"
        
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
        
        # Sekretariat (within agencies/organizations, not "Sekretariat Daerah")
        if name.startswith("Sekretariat ") and name != "Sekretariat Daerah":
            # Remove "Sekretariat " prefix from the unit name to get parent organization name
            # e.g., "Sekretariat Badan X" -> "Sekretaris Badan X" (not "Sekretaris Sekretariat Badan X")
            parent_org_name = name.replace("Sekretariat ", "", 1)
            return f"Sekretaris {parent_org_name}"
        
        # Bagian (Section) - include full name
        if name.startswith("Bagian "):
            return f"Kepala {name}"
        
        # Bidang (Division) - include full name
        if name.startswith("Bidang "):
            return f"Kepala {name}"
        
        # Klinik - include full name
        if "klinik" in name_lower:
            return f"Kepala {name}"
        
        # RSUD at this level - include full name
        if "rsud" in name_lower or "rumah sakit" in name_lower:
            return f"Direktur {name}"
        
        # Puskesmas (Community Health Center) - include full name
        if "puskesmas" in name_lower:
            return f"Kepala {name}"
        
        # Laboratorium - include full name
        if "laboratorium" in name_lower:
            return f"Kepala {name}"
        
        # Kantor (Office) - include full name
        if "kantor" in name_lower:
            return f"Kepala {name}"
        
        # Kelurahan (Urban Village) - include full name
        if "kelurahan" in name_lower:
            return f"Lurah {name}"
    
    # Eselon IV (lower level)
    if eselon in ["IV.a", "IV.b"]:
        # Subbagian (Sub-section) - include full name
        if name.startswith("Subbagian ") or name.startswith("Sub Bagian "):
            return f"Kepala {name}"
        
        # Subbidang (Sub-division) - include full name
        if name.startswith("Subbidang ") or name.startswith("Sub Bidang "):
            return f"Kepala {name}"
        
        # Seksi (Section) - include full name
        if name.startswith("Seksi "):
            return f"Kepala {name}"
        
        # Desa (Village) - include full name
        if "desa" in name_lower or name.startswith("Desa "):
            return f"Kepala {name}"
    
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
    Also reorders fields so jabatan comes before eselon.
    
    Args:
        data: List of organizational units or single unit
        parent_name: Name of parent organization
    
    Returns:
        Modified data with jabatan field added and fields reordered
    """
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'name' in item:
                # Calculate jabatan
                name = item['name']
                eselon = item.get('eselon', '')
                jabatan = determine_jabatan(name, eselon, parent_name)
                
                # Recursively process children first
                children = item.get('children', [])
                if isinstance(children, list):
                    add_jabatan_recursive(children, item['name'])
                
                # Reorder fields: name, jabatan, eselon, children
                reordered_item = {
                    'name': item['name'],
                    'jabatan': jabatan
                }
                if 'eselon' in item:
                    reordered_item['eselon'] = item['eselon']
                if 'children' in item:
                    reordered_item['children'] = item['children']
                
                # Update the original item with reordered fields
                item.clear()
                item.update(reordered_item)
    
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
