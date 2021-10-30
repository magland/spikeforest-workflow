import json
import sys
import sortingview as sv
from sortingview.experimental.SpikeSortingView import prepare_spikesortingview_data, SpikeSortingView

def main():
    recording_json_fname = sys.argv[1]
    output_fname = sys.argv[2]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    recording_uri = r['recordingUri']
    sorting_true_uri = r['sortingTrueUri']
    R = sv.LabboxEphysRecordingExtractor(recording_uri, download=True)
    S = sv.LabboxEphysSortingExtractor(sorting_true_uri)
    
    prepare_spikesortingview_data(
        recording=R,
        sorting=S,
        recording_description=r['studyName'] + '/' + r['name'],
        sorting_description='true',
        output_file_name=output_fname,
        segment_duration_sec=60 * 30,
        snippet_len=(20, 20),
        max_num_snippets_per_segment=100,
        channel_neighborhood_size=7
    )

if __name__ == '__main__':
    main()