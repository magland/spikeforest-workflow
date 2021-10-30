import json
import sys
import yaml

def main():
    spikeforest_recordings_path = sys.argv[1]
    recording_str = sys.argv[2]
    output_fname = sys.argv[3]
    
    a = recording_str.split('.')
    study_set_name = a[0]
    study_name = a[1]
    recording_name = a[2]

    study_json_fname = f'{spikeforest_recordings_path}/recordings/{study_set_name}/{study_name}/{study_name}.json'
    with open(study_json_fname, 'r') as f:
        study = json.load(f)
    recording = [r for r in study['recordings'] if r['name'] == recording_name][0]
    with open(output_fname, 'w') as f:
        json.dump(recording, f, indent=4)

if __name__ == '__main__':
    main()