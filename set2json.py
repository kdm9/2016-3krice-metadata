#!/usr/bin/env python3
import metadata
from collections import defaultdict
import json
from os import path
import sys


md = metadata.load_csv("all_25228runs_raw.csv")
samples = {}
for run in md:
    samples[run['sra_id']] = run['sra_sample']

for setfile in sys.argv[1:]:
    jsonfn = setfile + '.json'
    with open(setfile) as fh, open(jsonfn, 'w') as jsonfh:
        js = defaultdict(list)
        for run in fh:
            run = run.strip()
            sample = samples[run]
            js[sample].append(run)
        json.dump(js, jsonfh, indent=1)
