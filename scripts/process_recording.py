import os
import json
import sys
import kachery_client as kc
import figurl as fig
from sortingview.experimental.SpikeSortingView import SpikeSortingView

def main():
    recording_json_fname = sys.argv[1]
    spikesortingview_data_fname = sys.argv[2]
    output_fname = sys.argv[3]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    X = SpikeSortingView(spikesortingview_data_fname)
    a = X.create_summary()
    b = X.create_units_table(unit_ids=X.unit_ids)
    c = X.create_autocorrelograms(unit_ids=X.unit_ids)
    d = X.create_raster_plot(unit_ids=X.unit_ids)
    e = X.create_average_waveforms(unit_ids=X.unit_ids)
    
    F = X.create_mountain_layout(figures=[a, b, c, d, e], label=r['studyName'] + '/' + r['name'] + ' ground truth')
    url = F.url()
    r['viewUrl'] = url
    with open(output_fname, 'w') as f:
        json.dump(r, f, indent=4)

if __name__ == '__main__':
    main()