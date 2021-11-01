from get_recordings import get_recordings

rule aggregate_ground_truth_views:
    input: [f'data/ground_truth_views/{r["study_set"]}.{r["study"]}.{r["recording"]}.json' for r in get_recordings()]
    output: 'data/output/ground_truth_views.json'
    run:
        import json
        def read_json(fname):
            with open(fname, 'r') as f:
                return json.load(f)
        def write_json(x, fname):
            with open(fname, 'w') as f:
                return json.dump(x, f, indent=4)
        out = [read_json(fname) for fname in input]
        write_json(out, output[0])