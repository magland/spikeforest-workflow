rule ground_truth_view:
    input: r='data/recordings/{study_set}.{study}.{recording}.json', s='data/ground_truth_sortings/{study_set}.{study}.{recording}.json'
    output: 'data/ground_truth_views/{study_set}.{study}.{recording}.json'
    shell: "FIGURL_CHANNEL=spikeforest python workflow/scripts/create_spikesortingview_url.py {input.r} {input.s} {output} true"