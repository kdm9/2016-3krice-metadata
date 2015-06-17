import csv
import json
import sys

def parse_group(line):
    sa = line['sample_attribute']
    return sa.split(' || ')[-2].split(':')[-1].strip()

fh = open(sys.argv[1])
reader = csv.DictReader(fh)

group_dict = {}

for line in reader:
    group = parse_group(line).title()
    sample = line['sample']
    run = line['run']

    if group not in group_dict:
        group_dict[group] = {}
    if sample not in group_dict[group]:
        group_dict[group][sample] = []
    group_dict[group][sample].append(run)
    group_dict[group][sample].sort()

for key in sorted(group_dict.keys()):
    print >>sys.stderr, key, len(group_dict[key])
print json.dumps(group_dict, indent=1)

fh.close()
