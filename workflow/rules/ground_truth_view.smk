rule ground_truth_spikesortingview_data:
    input: r='data/recordings/{study_set}.{study}.{recording}.json', s='data/ground_truth_sortings/{study_set}.{study}.{recording}.json'
    output: 'data/ground_truth_views/{study_set}.{study}.{recording}.spikesortingview.h5'
    shell: "python workflow/scripts/create_spikesortingview_data.py {input.r} {input.s} {output}"

rule ground_truth_view:
    input: json='data/recordings/{study_set}.{study}.{recording}.json', h5='data/ground_truth_views/{study_set}.{study}.{recording}.spikesortingview.h5'
    output: 'data/ground_truth_views/{study_set}.{study}.{recording}.json'
    shell: "FIGURL_CHANNEL=flatiron1 python workflow/scripts/create_spikesortingview_url.py {input.json} {input.h5} {output} true"