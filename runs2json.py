#!/usr/bin/env python3
import metadata
from collections import defaultdict
import json

samples = defaultdict(list)

md = metadata.load_csv("all_25228runs_raw.csv")

for run in md:
    samples[run['sra_sample']].append(run['sra_id'])

print(json.dumps(samples, indent=2))
