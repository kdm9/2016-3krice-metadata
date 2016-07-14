import csv
import json
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats


def zfilter(df, by, zscore):
    return df.iloc[np.abs(stats.zscore(df[by])) < zscore]


def parse_attribute(line):
    sa = line['sample_attribute']
    attrs = dict(map(lambda x: x.split(': '), sa.split(' || ')))
    return attrs


def load_csv(csvpath):
    runs = []
    with open(csvpath) as fh:
        reader = csv.DictReader(fh)
        for line in reader:
            attrs = parse_attribute(line)
            run = {
                'source': attrs['Source'],
                'tissue': attrs['tissue_type'],
                'group': attrs['Variety_Group(Tree)'],
                'country': attrs['COUNTRY'],
                'varname': attrs['DNA_VARNAME_unicode'],
                'irri_accno': attrs['DNA_Accno_source'],
                'sra_sample': line['sample'],
                'taxid': line['taxon_id'],
                'run_date': line['run_date'],
                'sra_id': line['run'],
                'num_reads': int(line['spots']),
                'num_bases': int(line['bases']),
            }
            runs.append(run)
    return runs


def load_pd(csvpath):
    return pd.DataFrame(load_csv(csvpath))


def runs_groupby(runs, by='sra_sample'):
    groups = defaultdict(list)
    for run in runs:
        groups[run[by]].append(run)
    return groups
