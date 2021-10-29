import json
import sys
import sortingview as sv

def main():
    recording_json_fname = sys.argv[1]
    output_fname = sys.argv[2]
    with open(recording_json_fname, 'r') as f:
        r = json.load(f)
    recording_uri = r['recordingUri']
    sorting_true_uri = r['sortingTrueUri']
    R = sv.LabboxEphysRecordingExtractor(recording_uri, download=True)
    S = sv.LabboxEphysSortingExtractor(sorting_true_uri)
    r['downloaded'] = True
    with open(output_fname, 'w') as f:
        json.dump(r, f, indent=4)

if __name__ == '__main__':
    main()