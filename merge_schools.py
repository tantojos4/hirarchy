#!/usr/bin/env python3
"""
Script to merge schools from sd_negeri_*.json files into hierarchy.json.
Adds missing schools to the Dinas Pendidikan section.
"""

import json
import glob
import sys

def find_dinas_pendidikan(data):
    """Find Dinas Pendidikan in the hierarchy"""
    if isinstance(data, list):
        for item in data:
            result = find_dinas_pendidikan(item)
            if result:
                return result
    elif isinstance(data, dict):
        if data.get('name') == 'Dinas Pendidikan':
            return data
        if 'children' in data:
            for child in data['children']:
                result = find_dinas_pendidikan(child)
                if result:
                    return result
    return None

def main():
    # Load hierarchy.json
    print("Loading hierarchy.json...")
    with open('/home/runner/work/hirarchy/hirarchy/hierarchy.json', 'r', encoding='utf-8') as f:
        hierarchy = json.load(f)
    
    # Find Dinas Pendidikan
    dinas = find_dinas_pendidikan(hierarchy)
    if not dinas:
        print("Error: Dinas Pendidikan not found in hierarchy.json!")
        sys.exit(1)
    
    # Get all existing school names in hierarchy
    existing_schools = set()
    if 'children' in dinas:
        for child in dinas['children']:
            name = child.get('name', '')
            if 'Sekolah Dasar' in name:
                existing_schools.add(name)
    
    print(f"Found {len(existing_schools)} existing schools in hierarchy.json")
    
    # Get all schools from sd_negeri files
    all_schools_data = {}
    for file in sorted(glob.glob('/home/runner/work/hirarchy/hirarchy/sd_negeri_*.json')):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for school in data:
                school_name = school.get('Nama Sekolah', '')
                if school_name:
                    all_schools_data[school_name] = school
    
    print(f"Found {len(all_schools_data)} total schools in sd_negeri files")
    
    # Find missing schools
    missing_schools = set(all_schools_data.keys()) - existing_schools
    print(f"Found {len(missing_schools)} missing schools")
    
    if missing_schools:
        # Add missing schools to Dinas Pendidikan children
        for school_name in sorted(missing_schools):
            new_school = {
                "name": school_name,
                "children": []
            }
            dinas['children'].append(new_school)
            print(f"  + Added: {school_name}")
        
        # Save updated hierarchy.json
        print(f"\nSaving updated hierarchy.json...")
        with open('/home/runner/work/hirarchy/hirarchy/hierarchy.json', 'w', encoding='utf-8') as f:
            json.dump(hierarchy, f, ensure_ascii=False, indent=2)
        
        print(f"Successfully added {len(missing_schools)} schools to hierarchy.json")
        print(f"Total schools now: {len(existing_schools) + len(missing_schools)}")
    else:
        print("No missing schools found. hierarchy.json is up to date.")

if __name__ == "__main__":
    main()
