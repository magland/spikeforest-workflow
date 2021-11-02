import os
import yaml
from copy import deepcopy

def get_recordings():
    x = _load_recordings_yaml()
    return x['recordings']

def get_sortings():
    x = _load_recordings_yaml()
    ret = []
    for r in x['recordings']:
        for sorter in r['sorters']:
            a = deepcopy(r)
            a['sorter'] = sorter
            ret.append(a)
    return ret

def _load_recordings_yaml():
    thisdir = os.path.dirname(os.path.realpath(__file__))
    if os.getenv('SPIKEFOREST_WORKFLOW_TEST') == '1':
        fname = f'{thisdir}/recordings_test.yaml'
    else:
        fname = f'{thisdir}/recordings.yaml'
    with open(fname, 'r') as f:
        return yaml.safe_load(f)