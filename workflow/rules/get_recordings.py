import os
import yaml
from copy import deepcopy

def get_recordings():
    thisdir = os.path.dirname(os.path.realpath(__file__))
    fname = f'{thisdir}/recordings.yaml' 
    with open(fname, 'r') as f:
        x = yaml.safe_load(f)
        return x['recordings']

def get_sortings():
    thisdir = os.path.dirname(os.path.realpath(__file__))
    fname = f'{thisdir}/recordings.yaml' 
    with open(fname, 'r') as f:
        x = yaml.safe_load(f)
    ret = []
    for r in x['recordings']:
        for sorter in r['sorters']:
            a = deepcopy(r)
            a['sorter'] = sorter
            ret.append(a)
    return ret