rule output:
    input: gtv='data/output/ground_truth_views.json', sv='data/output/sorting_views.json', template='output.md.j2'
    output: 'output.md'
    run:
        import json
        from jinja2 import Template
        with open(input.template, 'r') as f:
            template_txt = f.read()
        with open(input.gtv, 'r') as f:
            ground_truth_views = json.load(f)
        with open(input.sv, 'r') as f:
            sorting_views = json.load(f)
        t = Template(template_txt, keep_trailing_newline=True)
        template_data = {
            'ground_truth_views': ground_truth_views,
            'sorting_views': sorting_views
        }
        gen_txt = t.render(**template_data)
        with open(output[0], 'w') as f:
            f.write(gen_txt)