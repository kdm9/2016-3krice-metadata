import json
import random
import sys

with open(sys.argv[1]) as fh:
    gdict = json.load(fh)

supergroups = {
    'Indica': 'Indica',
    'Japoinca': 'Japonica',
    'Temperate Japonica': 'Japonica',
    'Tropical Japonica': 'Japoinca',
}

grouped_samples = {}

for grp, sample in gdict.items():
    try:
        supergroup = supergroups[grp]
    except KeyError:
        continue

    grouped_samples[supergroup] = sample


def make_file(fname):
    samples = {}

    for x in range(8):
        for grp in set(supergroups.values()):
            runs = []
            sample_name = ''
            while len(runs) != 6:
                sample_name = random.choice(grouped_samples[grp].keys())
                runs = grouped_samples[grp][sample_name]

            try:
                samples[grp][sample_name] = runs
            except KeyError:
                samples[grp] = {sample_name: runs}

    with open(fname, 'w') as ofh:
        for group, samples in sorted(samples.items()):
            for sample, runs in samples.items():
                for run in sorted(runs):
                    print >> ofh, run

for x in range(int(sys.argv[2])):
    fname = '96s/96-2groups-{:02d}.txt'.format(x)
    make_file(fname)


