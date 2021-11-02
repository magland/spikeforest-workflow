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
    sorter_name = sys.argv[4]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    X = SpikeSortingView(spikesortingview_data_fname)
    f1 = X.create_summary()
    f2 = X.create_units_table(unit_ids=X.unit_ids)
    f3 = X.create_autocorrelograms(unit_ids=X.unit_ids)
    f4 = X.create_raster_plot(unit_ids=X.unit_ids)
    f5 = X.create_average_waveforms(unit_ids=X.unit_ids)
    f6 = X.create_spike_amplitudes(unit_ids=X.unit_ids)
    
    F = X.create_mountain_layout(
        figures=[f1, f2, f3, f4, f5, f6],
        label=r['studyName'] + '/' + r['name'] + ' ' + sorter_name
    )
    url = F.url()
    r['viewUrl'] = url
    r['sorterName'] = sorter_name
    with open(output_fname, 'w') as f:
        json.dump(r, f, indent=4)

if __name__ == '__main__':
    main()