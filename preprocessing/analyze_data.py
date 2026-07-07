import csv

prices = []
playtimes = []
positives = []
negatives = []

with open('dataset/steamgamesdataset.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        p = row['Price'].strip()
        if p:
            prices.append(float(p))
        pt = row['Average playtime forever'].strip()
        if pt:
            playtimes.append(float(pt))
        pos = row['Positive'].strip()
        if pos:
            positives.append(int(pos))
        neg = row['Negative'].strip()
        if neg:
            negatives.append(int(neg))

prices.sort()

print(f'Total records: {len(prices) + sum(1 for _ in open("dataset/steamgamesdataset.csv", "r", encoding="utf-8")) - 1}')
print(f'Records with price: {len(prices)}')
print(f'Price range: {prices[0]:.2f} - {prices[-1]:.2f}')
print(f'Price median: {prices[len(prices)//2]:.2f}')

low = sum(1 for p in prices if p < 5)
med = sum(1 for p in prices if 5 <= p < 20)
high = sum(1 for p in prices if p >= 20)
print(f'Price < 5: {low}')
print(f'Price 5-19.99: {med}')
print(f'Price >= 20: {high}')
print(f'Free (price=0): {sum(1 for p in prices if p == 0)}')

print()
print(f'Playtime data: {len(playtimes)} records')
if playtimes:
    print(f'Playtime range: {playtimes[0]:.2f} - {playtimes[-1]:.2f}')
    print(f'Playtime median: {playtimes[len(playtimes)//2]:.2f}')

print(f'Apps with positive reviews: {len(positives)}')
print(f'Apps with negative reviews: {len(negatives)}')
