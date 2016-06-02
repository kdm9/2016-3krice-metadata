import csv
import json
import pandas as pd


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
                'num_reads': line['spots'],
                'num_bases': line['bases'],
            }
            runs.append(run)
    return runs


def load_pd(csvpath):
    return pd.read_json(json.dumps(load_csv(csvpath)))
