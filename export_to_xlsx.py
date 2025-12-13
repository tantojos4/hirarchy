#!/usr/bin/env python3
"""
Script to export hierarchy.json to XLSX format with nama_unit, nama_parent, and eselon columns.

Usage:
    python export_to_xlsx.py
"""

import json
import sys
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
except ImportError:
    print("Error: openpyxl library is required. Install it with: pip install openpyxl")
    sys.exit(1)


def flatten_hierarchy(data, parent_name=""):
    """
    Flatten hierarchical JSON structure into a list of (unit_name, parent_name, eselon) tuples.
    
    Args:
        data: List of organizational units with nested children
        parent_name: Name of the parent unit (empty string for top-level)
    
    Returns:
        List of tuples (unit_name, parent_name, eselon)
    """
    result = []
    
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'name' in item:
                unit_name = item['name']
                eselon = item.get('eselon', '')
                result.append((unit_name, parent_name, eselon))
                
                # Recursively process children
                if 'children' in item and isinstance(item['children'], list):
                    children_results = flatten_hierarchy(item['children'], unit_name)
                    result.extend(children_results)
    
    return result


def create_xlsx(data, output_file="hierarchy_export.xlsx"):
    """
    Create XLSX file with nama_unit, nama_parent, and eselon columns.
    
    Args:
        data: List of tuples (unit_name, parent_name, eselon)
        output_file: Path to output XLSX file
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Hierarchy"
    
    # Set column headers
    ws['A1'] = "nama_unit"
    ws['B1'] = "nama_parent"
    ws['C1'] = "eselon"
    
    # Style headers
    header_font = Font(bold=True, size=12, color="FFFFFF")
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center")
    
    for cell in ['A1', 'B1', 'C1']:
        ws[cell].font = header_font
        ws[cell].fill = header_fill
        ws[cell].alignment = header_alignment
    
    # Write data
    for idx, (unit_name, parent_name, eselon) in enumerate(data, start=2):
        ws[f'A{idx}'] = unit_name
        ws[f'B{idx}'] = parent_name if parent_name else ""
        ws[f'C{idx}'] = eselon if eselon else ""
    
    # Adjust column widths
    ws.column_dimensions['A'].width = 80
    ws.column_dimensions['B'].width = 80
    ws.column_dimensions['C'].width = 15
    
    # Save workbook
    wb.save(output_file)
    print(f"Successfully created {output_file}")
    print(f"Total records: {len(data)}")


def main():
    """Main function to export hierarchy to XLSX."""
    # Read hierarchy.json
    json_file = Path(__file__).parent / "hierarchy.json"
    
    if not json_file.exists():
        print(f"Error: {json_file} not found!")
        sys.exit(1)
    
    print(f"Reading {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        hierarchy_data = json.load(f)
    
    print("Flattening hierarchy...")
    flattened_data = flatten_hierarchy(hierarchy_data)
    
    # Create XLSX file
    output_file = Path(__file__).parent / "hierarchy_export.xlsx"
    print(f"Creating {output_file}...")
    create_xlsx(flattened_data, str(output_file))
    
    print("\nFirst 5 records:")
    for i, (unit, parent, eselon) in enumerate(flattened_data[:5], 1):
        print(f"{i}. Unit: {unit}")
        print(f"   Parent: {parent if parent else '(kosong)'}")
        print(f"   Eselon: {eselon if eselon else '(kosong)'}")


if __name__ == "__main__":
    main()
