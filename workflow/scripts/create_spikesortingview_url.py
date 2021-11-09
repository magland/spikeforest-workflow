import os
import json
import sys
import sortingview as sv
import kachery_client as kc
import figurl as fig
from sortingview.experimental.SpikeSortingView import SpikeSortingView

def main():
    recording_json_fname = sys.argv[1]
    sorting_json_fname = sys.argv[2]
    output_fname = sys.argv[3]
    sorter_name = sys.argv[4]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    with open(sorting_json_fname, 'r') as f:
        s = json.load(f)
    recording_uri = r['recordingUri']
    sorting_uri = s['sortingUri']
    R = sv.LabboxEphysRecordingExtractor(recording_uri, download=True)
    S = sv.LabboxEphysSortingExtractor(sorting_uri)
    X = SpikeSortingView.create(
        recording=R,
        sorting=S,
        segment_duration_sec=60 * 20,
        snippet_len=(20, 20),
        max_num_snippets_per_segment=100,
        channel_neighborhood_size=7
    )

    f1 = X.create_summary()
    f2 = X.create_units_table(unit_ids=X.unit_ids, unit_metrics=None)
    f3 = X.create_autocorrelograms(unit_ids=X.unit_ids)
    f4 = X.create_raster_plot(unit_ids=X.unit_ids)
    f5 = X.create_average_waveforms(unit_ids=X.unit_ids)
    f6 = X.create_spike_amplitudes(unit_ids=X.unit_ids)
    f7 = X.create_electrode_geometry()
    f8 = X.create_live_cross_correlograms()

    mountain_layout = X.create_mountain_layout(
        figures=[f1, f2, f3, f4, f5, f6, f7, f8],
        label=r['studyName'] + '/' + r['name'] + ' ' + sorter_name
    )

    url = mountain_layout.url()

    r['viewUrl'] = url
    r['sorterName'] = sorter_name
    with open(output_fname, 'w') as f:
        json.dump(r, f, indent=4)

if __name__ == '__main__':
    main()