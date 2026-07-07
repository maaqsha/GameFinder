import csv

with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines in file: {len(lines)}')
print(f'Header: {lines[0].strip()!r}')
print()

# --- Check row lengths (comma count) ---
lengths = {}
for i, line in enumerate(lines):
    if i == 0:
        continue
    l = len(line.split(','))
    lengths[l] = lengths.get(l, 0) + 1

print('Row length distribution (comma count):')
for l in sorted(lengths):
    print(f'  {l} commas: {lengths[l]} rows')

print('\nHeader columns: 10')
print(f'Expected: 9 commas per row')
print()

# --- Find rows where naive split gives 10 fields ---
# These rows MIGHT be properly formatted
proper = 0
improper = 0
for i, line in enumerate(lines[1:], 1):
    if len(line.split(',')) == 10:
        proper += 1
    else:
        improper += 1
print(f'Rows with exactly 10 fields (naive): {proper}')
print(f'Rows with != 10 fields (naive): {improper}')
print()

# --- Check for quoted fields ---
qcount = 0
for i, line in enumerate(lines[1:], 1):
    if '"' in line:
        qcount += 1
print(f'Rows containing double quotes: {qcount}')

# --- Check for multiline fields ---
# If a field is quoted and contains a newline, csv.reader would handle it
# Let's check if lines starting with non-numeric might be continuations
non_numeric_start = 0
for i, line in enumerate(lines[1:], 1):
    first_col = line.split(',')[0].strip()
    if not first_col.isdigit():
        non_numeric_start += 1
        if non_numeric_start <= 3:
            print(f'Line {i} starts with non-numeric: {line[:80]!r}')
print(f'Lines with non-numeric first field: {non_numeric_start}')
