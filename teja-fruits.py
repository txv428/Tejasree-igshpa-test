import json
from sets import *

with open('fruits.json') as f:
  read_data = f.read()


data = json.loads(read_data)

frequencies = {}

for it in data:
  k = frozenset(set(it['fruits_picked']))
  if k in frequencies:
    frequencies[k] += 1
  else:
    frequencies[k] = 1

index = 1
for key, value in sorted(frequencies.iteritems(), key=lambda(k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
    if index ==20:
      break
    else:
      index += 1