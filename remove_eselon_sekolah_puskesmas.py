#!/usr/bin/env python3
"""
Script to remove eselon field from Puskesmas and Sekolah entries in hierarchy.json
According to the issue: schools and puskesmas should not have eselon levels
"""

import json
import sys

def remove_eselon_from_schools_and_puskesmas(data):
    """
    Recursively traverse the hierarchy and remove eselon field from
    any entry where the name contains 'Puskesmas' or 'Sekolah'
    """
    modified_count = 0
    
    if isinstance(data, list):
        for item in data:
            modified_count += remove_eselon_from_schools_and_puskesmas(item)
    elif isinstance(data, dict):
        # Check if this entry is a Puskesmas or Sekolah
        if 'name' in data and ('Puskesmas' in data['name'] or 'Sekolah' in data['name']):
            if 'eselon' in data:
                # Remove the eselon field
                del data['eselon']
                modified_count += 1
                print(f"Removed eselon from: {data['name']}")
        
        # Recursively process children
        if 'children' in data:
            modified_count += remove_eselon_from_schools_and_puskesmas(data['children'])
    
    return modified_count

def main():
    import shutil
    from datetime import datetime
    
    input_file = 'hierarchy.json'
    output_file = 'hierarchy.json'
    
    # Create backup before modifying
    backup_file = f'hierarchy.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    print(f"Creating backup: {backup_file}...")
    shutil.copy2(input_file, backup_file)
    
    print(f"Reading {input_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {input_file}: {e}")
        sys.exit(1)
    
    print("\nRemoving eselon field from Puskesmas and Sekolah entries...")
    modified_count = remove_eselon_from_schools_and_puskesmas(data)
    
    print(f"\nTotal entries modified: {modified_count}")
    
    if modified_count > 0:
        print(f"\nWriting updated data to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Done!")
    else:
        print("No entries were modified.")

if __name__ == '__main__':
    main()
