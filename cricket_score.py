from pycricbuzz import Cricbuzz
i=Cricbuzz()
matches = i.matches()

print(matches)
for p in matches:
    print(i.livescore(p['id']))
    print(p['id'])
    print(p['srs'])
    print(p['status'])
    break