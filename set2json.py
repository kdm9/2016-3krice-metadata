#!/usr/bin/env python3
import metadata
from collections import defaultdict
import json
from os import path
import sys

supergroups = {
    'indica':               'Indica',
    'japonica':             'Japonica',
    'temperate japonica':   'Japonica',
    'tropical japonica':    'Japonica',
}
md = metadata.load_csv("all_25228runs_raw.csv")
samples = {}
groups = {}
for run in md:
    samples[run['sra_id']] = run['sra_sample']
    grp = supergroups.get(run['group'].lower(), 'other')
    groups[run['sra_id']] = grp

for setfile in sys.argv[1:]:
    jsonfn = setfile + '.json'
    with open(setfile) as fh, open(jsonfn, 'w') as jsonfh:
        js = defaultdict(lambda: defaultdict(list))
        for run in fh:
            run = run.strip()
            sample = samples[run]
            group = groups[run]
            js[group][sample].append(run)
        json.dump(js, jsonfh, indent=1)
