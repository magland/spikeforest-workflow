rule clone_recordings:
    output: directory('data/spikeforest_recordings')
    shell: f"git clone https://github.com/flatironinstitute/spikeforest_recordings" + " {output}"

rule recording:
    input: sr='data/spikeforest_recordings'
    params:
        study_set="{study_set}",
        study="{study}",
        recording="{recording}"
    output: 'data/recordings/{study_set}.{study}.{recording}.json'
    run:
        import json
        study_json_fname = f'{input.sr}/recordings/{params.study_set}/{params.study}/{params.study}.json'
        with open(study_json_fname, 'r') as f:
            study = json.load(f)
        recording = [r for r in study['recordings'] if r['name'] == params.recording][0]
        with open(output[0], 'w') as f:
            json.dump(recording, f, indent=4)

rule ground_truth_sorting:
    input: sr='data/spikeforest_recordings'
    params:
        study_set="{study_set}",
        study="{study}",
        recording="{recording}"
    output: 'data/ground_truth_sortings/{study_set}.{study}.{recording}.json'
    run:
        import json
        study_json_fname = f'{input.sr}/recordings/{params.study_set}/{params.study}/{params.study}.json'
        with open(study_json_fname, 'r') as f:
            study = json.load(f)
        recording = [r for r in study['recordings'] if r['name'] == params.recording][0]
        with open(output[0], 'w') as f:
            json.dump({'sortingUri': recording['sortingTrueUri']}, f, indent=4)