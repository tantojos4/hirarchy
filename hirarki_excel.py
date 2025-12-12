#!/usr/bin/env python3
"""
generate_hierarchy_with_excel.py

Baca pasted.txt (default) dan hasilkan:
 - hierarchy.json   (struktur pohon)
 - relationships.csv (parent,child)
 - relationships.xlsx (Excel file)

Usage:
  python3 generate_hierarchy_with_excel.py
  python3 generate_hierarchy_with_excel.py -i pasted.txt -j hierarchy.json -c relationships.csv -x relationships.xlsx

Depends:
  pip install pandas openpyxl
"""
import re
import json
import csv
import argparse
from collections import defaultdict
import pandas as pd

def normalize(s: str) -> str:
    return ' '.join(s.strip().split())

def parse_file(path: str):
    all_nodes = set()
    parent_to_children = defaultdict(set)
    children_set = set()
    split_re = re.compile(r'\s*-\s*')

    with open(path, encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            parts = [normalize(p) for p in split_re.split(line) if p.strip()]
            if not parts:
                continue
            for p in parts:
                all_nodes.add(p)
            for i in range(len(parts) - 1):
                child = parts[i]
                parent = parts[i + 1]
                parent_to_children[parent].add(child)
                children_set.add(child)

    return {
        'all_nodes': all_nodes,
        'parent_to_children': parent_to_children,
        'children_set': children_set
    }

def build_tree(parent_to_children, root):
    children = sorted(parent_to_children.get(root, []))
    return {
        'name': root,
        'children': [build_tree(parent_to_children, c) for c in children]
    }

def main():
    parser = argparse.ArgumentParser(description='Generate hierarchy JSON, CSV and Excel from pasted.txt')
    parser.add_argument('-i', '--input', default='pasted.txt', help='Input text file (default pasted.txt)')
    parser.add_argument('-j', '--json', default='hierarchy.json', help='Output JSON file')
    parser.add_argument('-c', '--csv', default='relationships.csv', help='Output CSV file')
    parser.add_argument('-x', '--excel', default='relationships.xlsx', help='Output Excel file (.xlsx)')
    parser.add_argument('--print-summary', action='store_true', help='Print summary')
    args = parser.parse_args()

    data = parse_file(args.input)
    all_nodes = data['all_nodes']
    parent_to_children = data['parent_to_children']
    children_set = data['children_set']

    roots = sorted(all_nodes - children_set)
    trees = [build_tree(parent_to_children, r) for r in roots]

    # write JSON
    with open(args.json, 'w', encoding='utf-8') as jf:
        json.dump(trees, jf, ensure_ascii=False, indent=2)

    # prepare relations list (parent, child)
    relations = []
    for parent in sorted(parent_to_children.keys()):
        for child in sorted(parent_to_children[parent]):
            relations.append({'parent': parent, 'child': child})

    # write CSV (comma separated)
    with open(args.csv, 'w', newline='', encoding='utf-8') as cf:
        writer = csv.DictWriter(cf, fieldnames=['parent', 'child'])
        writer.writeheader()
        for r in relations:
            writer.writerow(r)

    # write Excel using pandas
    try:
        df = pd.DataFrame(relations)
        # If DataFrame is empty, create columns
        if df.empty:
            df = pd.DataFrame(columns=['parent', 'child'])
        df.to_excel(args.excel, index=False)
    except Exception as e:
        print('Gagal menulis Excel (.xlsx):', e)
        print('Pastikan pandas & openpyxl ter-install: pip install pandas openpyxl')

    if args.print_summary:
        print(f'Input: {args.input}')
        print(f'Nodes: {len(all_nodes)}')
        print(f'Relations: {len(relations)}')
        print(f'Roots: {len(roots)}')
        for r in roots[:20]:
            print(' -', r)
        print('Wrote:', args.json, args.csv, args.excel)

if __name__ == '__main__':
    main()