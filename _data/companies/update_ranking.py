from csv import DictReader, DictWriter
from collections import defaultdict
from operator import itemgetter

with open('points.csv') as f:
    reader = DictReader(f)
    catpoints = {r['category']: int(r['points']) for r in reader}

points = defaultdict(int)
with open('contributions.csv') as f:
    reader = DictReader(f)
    for r in reader:
        points[r['company']] += catpoints[r['category']]

ranking = sorted(points.items(), key=itemgetter(1), reverse=True)

with open('ranking.csv', 'w') as f:
    writer = DictWriter(f, ['company', 'score'])
    writer.writeheader()
    writer.writerows({'company': c, 'score': s} for (c, s) in ranking)
