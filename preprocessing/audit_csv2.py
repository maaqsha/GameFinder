import csv, sys

def safe(s):
    if isinstance(s, str):
        return s.encode('ascii', 'replace').decode('ascii')
    return str(s)

with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print('Header:', header)
    print()

    numeric_playtime = 0
    text_playtime = 0
    empty_playtime = 0
    sample_numeric = []
    sample_text = []

    for i, row in enumerate(reader):
        if len(row) < 10:
            continue
        pt = row[8].strip()
        if not pt:
            empty_playtime += 1
        else:
            try:
                v = float(pt)
                numeric_playtime += 1
                if len(sample_numeric) < 5:
                    sample_numeric.append((i, v, row[0], safe(row[1][:40])))
            except ValueError:
                text_playtime += 1
                if len(sample_text) < 5:
                    clean_pt = safe(pt[:80])
                    clean_name = safe(row[1][:40])
                    sample_text.append((i, clean_pt, row[0], clean_name))

    print('Playtime column analysis:')
    print(f'  Numeric: {numeric_playtime}')
    print(f'  Text (non-numeric): {text_playtime}')
    print(f'  Empty: {empty_playtime}')
    print()
    print('Sample text playtime rows:')
    for s in sample_text:
        print(f'  Row {s[0]}: text={s[1]!r}, AppID={s[2]}, Name={s[3]}')
    print()

    # Show raw line of first text-playtime row
    if sample_text:
        print('=== RAW LINE OF FIRST TEXT PLAYTIME ROW ===')
        line_idx = sample_text[0][0]
        with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f2:
            for j, line in enumerate(f2):
                if j == line_idx + 1:
                    r = csv.reader([line]).__next__()
                    print(f'Row {line_idx} has {len(r)} csv fields')
                    for k in range(len(r)):
                        val = safe(r[k][:60])
                        print(f'  csv[{k}] = {val!r}')
                    break
