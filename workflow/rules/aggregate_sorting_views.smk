from get_recordings import get_sortings

rule aggregate_sorting_views:
    input: [f'data/sorting_views/{r["study_set"]}.{r["study"]}.{r["recording"]}.{r["sorter"]}.json' for r in get_sortings()]
    output: 'data/output/sorting_views.json'
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